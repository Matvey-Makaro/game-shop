from django.contrib.auth.models import AbstractUser
from django.db import models
from pkg_resources import _
from django.urls import reverse


class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'


class Mailbox(models.Model):
    address = models.EmailField()
    password = models.CharField(_('password'), max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mailbox')
    last_email_id = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('mailbox', kwargs={'mailbox_id': self.pk})


class Email(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emails')
    from_address = models.EmailField()
    # sender = models.ForeignKey(Mailbox, on_delete=models.CASCADE, related_name='emails_sender')
    recipient = models.ForeignKey(Mailbox, on_delete=models.CASCADE, related_name='emails_recipient', null=True,
                                  blank=True)
    # recipients = models.ManyToManyField(Mailbox, related_name='emails_received')
    recipients = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=False)
    read = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('mail', kwargs={'mail_id': self.pk})
