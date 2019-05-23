from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from datetime import datetime
import random
from django.core.exceptions import ValidationError

from . models import Queue, Player, Match, Winner

queue_created = False

@receiver(m2m_changed, sender=Winner.players.through)
def winnerPlayer_handler(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        players = Player.objects.filter(pk__in=pk_set)
        for player in players:
            player.total_wins += 1
            player.save()
        match = instance.match
        players = match.players.all()
        for player in players:
            player.total_games += 1
            player.save()

        match.endDT = datetime.now()
        match.onGoing = False
        match.save()


@receiver(m2m_changed, sender=Match.players.through)
def matchPlayer_handler(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        players = Player.objects.filter(pk__in=pk_set)
        for player in players:
            player.inMatch = True
            player.save()

    if action == "post_remove":
        players = Player.objects.filter(pk__in=pk_set)
        for player in players:
            player.inMatch = False
            player.save()



@receiver(m2m_changed, sender=Queue.players.through)
def queuePlayer_handler(sender, instance, action, pk_set, **kwargs):
    global queue_created
    if action == "post_add":    
        players = Player.objects.filter(pk__in=pk_set)
        for player in players:
            player.inQueue = True
            player.save()
    
        if queue_created:
            count = instance.court
            
            while count > 0:
                instance.match_set.create(user=instance.user, court_num=count)
                count = count - 1

    elif action == "post_remove":
        players = Player.objects.filter(pk__in=pk_set)
        for player in players:
            player.inQueue = False
            player.inMatch = False
            player.save()
    
    elif action == "pre_remove":
        players = Player.objects.filter(pk__in=pk_set)
        for player in players:
            if player.inMatch:
                pk_set.remove(player.player_id)
        # if playerInMatch:
        #     raise ValidationError('Player may be in match.')
        
        





@receiver(post_save, sender=Queue)
def queueHandler_postsave(sender, instance, created, **kwargs):
    global queue_created
    queue_created = created    
    #________handles Change of Court Number_____
    if not created:
        matches = instance.match_set.filter(user=instance.user, endDT=None) #Matches that were already generated
        match_count = matches.count()   #Count of matches already generated

        #Need to add matches
        if instance.court > match_count:
            counter = instance.court - match_count  #get the number of matches to add

            while ( counter > 0 ):
                instance.match_set.create(user=instance.user, court_num=(instance.court + counter-1))
                counter = counter - 1
        elif instance.court < match_count:
            matches = matches.filter(onGoing=False).order_by('-court_num')   #get the matches that haven't been started
            counter = match_count - instance.court  #get the number of matches to subtract

            while ( counter > 0 ):
                match = matches.first()
                players = match.players.all()
                for player in players:
                    player.inMatch = False
                    player.save()
                match.delete()
                counter = counter - 1
    #________handles End Queues_________
    
    if not instance.onGoing:
        print("Got in")
        instance.endQueue()
        matches = instance.match_set.filter(user=instance.user, onGoing=False, endDT=None)
        for match in matches:
            match.delete()

        


@receiver(post_save, sender=Match)
def matchHandler_postsave(sender, instance, created, **kwargs):
    #Handles match creation
    if created:
        # Get players from associated Queue that are not in a match already
        # Get IDs from said players and generate a list of random IDs from it
        # Add the players with the generated random IDs to match
        players = instance.queuedAt.players.filter(user=instance.user, inMatch=False)      
        playerIDs = players.values_list('player_id', flat=True)
        playerIDs = list(playerIDs)
        rand_ids = random.sample(playerIDs, 2)

        if instance.queuedAt.match_type == 'D':
            rand_ids = random.sample(playerIDs, 4)
        
        rand_players = players.filter(player_id__in=rand_ids)

        for player in rand_players:
            instance.players.add(player)

        #Create a winner instance to associate it to this match
        Winner.objects.create(user=instance.user, match=instance)

        instance.save()
    #Handles Start of Matches
    elif (instance.startDT == None) and (instance.umpire != None):
            instance.onGoing = True
            instance.startDT = datetime.now()
            instance.save()
    
    
    #____Handles End of matches____
    elif (instance.endDT != None):
        
        instance.queuedAt.match_set.create(user=instance.user, court_num=instance.court_num,)
        players = instance.players.all()

        for player in players:
            player.inMatch = False
            player.save()
        







# Automatic listing of a number of matches per court in a queue
# 