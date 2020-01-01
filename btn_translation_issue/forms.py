from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Reset, Button
from django import forms
from django.utils.translation import gettext_lazy as _


common_buttons = Layout(
    Reset('reset', _('Reset')),
    Button('btn', _('Button')),
    Submit('submit', _('Submit')),
)


class DemoForm(forms.Form):
    name = forms.CharField(label=_('Name'))
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'message',
            common_buttons,
        )
