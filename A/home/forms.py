from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField() #title = forms.CharField(label='Title', required=False)
    body = forms.CharField()
    created = forms.DateTimeField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__' #fields = ['title', 'body', 'created']
