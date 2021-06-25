from django import forms

from lists.models import Item, List


EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
            'placeholder': 'Enter a to-do item',
            'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }


class NewListForm(object):
    def save(self, owner):
        if owner.is_authenticated:
            return List.create_new(first_item_text=self.cleaned_data['text'], owner=owner)
        else:
            return List.create_new(first_item_text=self.cleaned_data['text'])


class ExistingListItemForm(ItemForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
            'placeholder': 'Enter a to-do item',
            'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }