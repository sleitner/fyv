from django.forms import ModelForm
from django.forms.fields import TextInput
from django.core.exceptions import ValidationError

from lists.models import Person, Voter, List

class ItemForm(ModelForm):

    class Meta:
        model = Person
        fields = ['firstname','lastname']
        widgets = {
             'firstname': TextInput(attrs={
                 'placeholder': 'Enter voter\'s first name',
                  'class': 'form-control input-lg'
             }),
             'lastname': TextInput(attrs={
                 'placeholder': 'Enter voter\'s last name',
                 'class': 'form-control input-lg'
             }),
         }
        error_messages = {
            'firstname': {'required': 'first name is currently required'},
            'lastname': {'required': 'last name is required'}
        }
#        Voter.object.create(firstname, lastname, byr=111)


class NewListForm(ItemForm):
    def save(self, owner):
        if owner.is_authenticated():
            return List.create_new(first_item_firstname=self.cleaned_data['firstname'], 
                                   first_item_lastname=self.cleaned_data['lastname'],
                                   owner=owner)
        else:
            return List.create_new(first_item_firstname=self.cleaned_data['firstname'], 
                                   first_item_lastname=self.cleaned_data['lastname'])

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

