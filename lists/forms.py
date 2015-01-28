from django.forms import ModelForm
from django.forms.fields import TextInput
from django.core.exceptions import ValidationError

from lists.models import Person, Voter, List

class ItemForm(ModelForm):

    class Meta:
        model = Person
        fields = ['firstname','lastname','zipcode']
        widgets = {
             'firstname': TextInput(attrs={
                 'placeholder': 'first name',
                  'class': 'form-control input-lg'
             }),
             'lastname': TextInput(attrs={
                 'placeholder': 'last name',
                 'class': 'form-control input-lg'
             }),
             'zipcode': TextInput(attrs={
                 'placeholder': 'zip code',
                  'class': 'form-control input-lg'
             }),
         }
        error_messages = {
            'firstname': {'required': 'first name is currently required'},
            'lastname': {'required': 'last name is required'},
            'zipcode': {'required': 'zip code is required'}
        }


class NewListForm(ItemForm):
    def save(self, owner=''):
        return List.create_new(item_firstname=self.cleaned_data['firstname'], 
                               item_lastname=self.cleaned_data['lastname'],
                               item_zipcode=self.cleaned_data['zipcode']
                               )


