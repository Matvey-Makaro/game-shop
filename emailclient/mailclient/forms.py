from django import forms
from .models import *


class SendEmailForm(forms.Form):
    # from_email = forms.ModelChoiceField(queryset=Email.objects.filter(user__pk=self.c), label="mailboxes", empty_label="select mailbox")
    from_email = forms.EmailField()
    to_email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))



# class GetMailBox(forms.Form):
#     class Meta:
#         model = Mailbox
#         fields = ['address', 'password']
#         widgets = {
#             'address': forms.TextInput(attrs=)
#         }


class GetMailBox(forms.Form):
    address = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
