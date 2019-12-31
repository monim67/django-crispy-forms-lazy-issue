from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Button
from django import forms
from django.utils.translation import gettext_lazy as _


class DemoForm(forms.Form):
    name = forms.CharField(label=_('Name'))
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Reset('reset', _('Reset')))
        self.helper.add_input(Button('btn', _('Button')))
        self.helper.add_input(Submit('submit', _('Submit')))
