from django import forms
from .models import MakeGameRoom


class GameRoomListForm(forms.ModelForm):

    class meta:
        model = MakeGameRoom
        fields = ['game_room_address']
