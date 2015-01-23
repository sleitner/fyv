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
             'zipcode': TextInput(attrs={
                 'placeholder': 'zip code',
                  'class': 'form-control input-lg'
             }),
             'lastname': TextInput(attrs={
                 'placeholder': 'last name',
                 'class': 'form-control input-lg'
             }),
         }
        error_messages = {
            'firstname': {'required': 'first name is currently required'},
            'lastname': {'required': 'last name is required'},
            'zipcode': {'required': 'zip code is required'}
        }


class NewListForm(ItemForm):
    def save(self, owner):
        if owner.is_authenticated():
            return List.create_new(item_firstname=self.cleaned_data['firstname'], 
                                   item_lastname=self.cleaned_data['lastname'],
                                   item_zipcode=self.cleaned_data['zipcode'],
                                   owner=owner)
        else:
            return List.create_new(item_firstname=self.cleaned_data['firstname'], 
                                   item_lastname=self.cleaned_data['lastname'],
                                   item_zipcode=self.cleaned_data['zipcode']
                                   )

class ExistingListItemForm(ItemForm):
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

        
    # def validate_unique(self):
    #     try:
    #         self.instance.validate_unique()
    #     except ValidationError as e:
    #         e.error_dict = {'text': ["You've already got this in your list"]}
    #         self._update_errors(e)

