from django import forms

from .models import Article

from .models import Network

from .models import MakeGameRoom

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title','contents','url','email']


class NetForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ['url']


class GameRoomlistForm(forms.ModelForm):
    class Meta :
        model = MakeGameRoom
        fields = ['user_address', 'prize_per_game']
