from django import forms

from .models import Player

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'first_name',
			'last_name', 
			'player_level'
		]