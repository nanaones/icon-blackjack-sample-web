from django import forms

from .models import Article

from .models import Network

from .models import Makegameroom

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title','contents','url','email']


class NetForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ['url']


class GameroomlistForm(forms.ModelForm):
    class Meta :
        model = Makegameroom
        fields = ['useraddress', 'prize_per_game']
