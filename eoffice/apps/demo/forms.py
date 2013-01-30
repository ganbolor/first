#coding:utf-8
from django import forms
from apps.setting.models import Config, AppModule
from django.utils.translation import ugettext_lazy as _

class ActionForm(forms.Form):
    action = forms.ChoiceField(label=_('Action:'))
    select_across = forms.BooleanField(label='', required=False, initial=0,
        widget=forms.HiddenInput({'class': 'select-across'}))

checkbox = forms.CheckboxInput({'class': 'action-select'}, lambda value: False)

class AppModuleAddForm(forms.ModelForm):
    class Meta:
        model = AppModule
        #fields = ('name', 'code')
        exclude = ('link', 'insert_user', 'insert_date', 'update_user', 'update_date' )

class ConfigAddForm(forms.ModelForm):
    class Meta:
        model = Config
        #fields = ('name', 'code')
    
            
