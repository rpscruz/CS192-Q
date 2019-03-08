import random

first_names = ['Sophia',  'Olivia',  'Emma',  'Ava',  'Isabella',  'Mia',  'Aria',  'Riley',  'Zoe',  'Amelia',  'Layla',  'Charlotte',  'Aubrey',  'Lily',  'Chloe',  'Harper',  'Evelyn',  'Adalyn',  'Emily',  'Abigail',  'Madison',  'Aaliyah',  'Avery',  'Ella',  'Scarlett',  'Maya',  'Mila',  'Nora',  'Camilla',  'Arianna',  'Eliana',  'Hannah',  'Leah',  'Ellie',  'Kaylee',  'Kinsley',  'Hailey',  'Madelyn',  'Paisley',  'Elizabeth',  'Addison',  'Isabelle',  'Anna',  'Sarah',  'Brooklyn',  'Mackenzie',  'Victoria',  'Luna',  'Penelope',  'Grace',  'Jackson',  'Liam',  'Noah',  'Aiden',  'Lucas',  'Caden',  'Grayson',  'Mason',  'Elijah',  'Logan',  'Oliver',  'Ethan',  'Jayden',  'Muhammad',  'Carter',  'Michael',  'Sebastian',  'Alexander',  'Jacob',  'Benjamin',  'James',  'Ryan',  'Matthew',  'Daniel',  'Jayce',  'Mateo',  'Caleb',  'Luke',  'Julian',  'Jack',  'William',  'Wyatt',  'Gabriel',  'Connor',  'Henry',  'Isaiah',  'Isaac',  'Owen',  'Levi',  'Cameron',  'Nicholas',  'Josiah',  'Lincoln',  'Dylan',  'Samuel',  'John',  'Nathan',  'Leo',  'David',  'Adam']

last_names = ['Santos',  'Reyes ',  'Cruz ',  'Bautista ',  'Lopez ',  'Gonzales ',  'Ramos ',  'Aquino ',  'Garcia ',  'Dela Cruz ',  'Del Rosario ',  'Fernandez ',  'Mendoza ',  'Morales ',  'Marquez ',  'Hernandez ',  'Navarro',  'Sanchez',  'Delos Reyes',  'Delos Santos',  'Martinez ',  'Torres ',  'Perez ',  'Rodriguez ',  'Diaz ',  'Villanueva ',  'De Leon ',  'Santiago ',  'Ramirez ',  'Soriano ']

dumpfile = open("dump.sql", "w")
dumpfile.write("-- populated from a python script")


def insertInto(table, form, n):
    for i in range (0, n):
        dumpfile.write("insert into {} (".format(table))
        for col, type in form.items():
            dumpfile.write(col)

            if col != list(form)[-1]: # ie. col != the last column of table structure
                dumpfile.write(", ")

        dumpfile.write(") values (")

        for col, type in form.items():
            if type == "varchar":
                if col == "first_name":
                    insert = random.choice(first_names)
                elif col == "last_name":
                    insert = random.choice(last_names)
                elif col == "venue_name":
                    insert = str(random.choice(last_names) + " Sports Center")
                elif col == "court_name":
                    insert = str(random.choice(last_names) + " Court")
                else:
                    insert = "asdfghjk"
            elif type == "smallint":
                insert = random.randint(1, 100)

            dumpfile.write("\'{}\'".format(str(insert)))

            if col != list(form)[-1]: # ie. col != the last column of table structure
                dumpfile.write(", ")

        dumpfile.write(");\n")

def insertIntoReferencing(table, form, n, **kwargs):
    print(kwargs)
    for i in range (0, n):
        dumpfile.write("insert into {} (".format(table))
        for col, type in form.items():
            dumpfile.write(col)

            if col != list(form)[-1]: # ie. col != the last column of table structure
                dumpfile.write(", ")

        dumpfile.write(") values (")

        for col, type in form.items():
            if type == "varchar":
                if col == "first_name":
                    insert = random.choice(first_names)
                elif col == "last_name":
                    insert = random.choice(last_names)
                elif col == "venue_name":
                    insert = str(random.choice(last_names) + " Sports Center")
                elif col == "court_name":
                    insert = str(random.choice(last_names) + " Court")
                else:
                    insert = "asdfghjk"
            elif type == "smallint":
                insert = random.randint(1, 3)

            dumpfile.write("\'{}\'".format(str(insert)))

            if col != list(form)[-1]: # ie. col != the last column of table structure
                dumpfile.write(", ")

        dumpfile.write(");\n")

venue_col = {
    "venue_name" : "varchar"
}

player_col = {
    "last_name": "varchar",
    "first_name": "varchar", 
    "player_level": "smallint",
    "total_games": "smallint",
    "total_win": "smallint"
}

court_col = {
    "court_name" : "varchar",
    "venue_id"   : "smallint"
}

venues = 5

insertInto("Venue", venue_col, venues)
# insertInto("Player", player_col, 3)
insertIntoReferencing(table = "Court", form = court_col, n = 2, keynums = venues)

dumpfile.close()
# dumpfile.write(player_col)


