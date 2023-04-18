from django.db import models

from django.contrib.auth.models import User,AbstractUser

# Create your models here.




class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    options=(("female","female"),("male","male"))
    gender=models.CharField(max_length=100,choices=options)
    is_active=models.BooleanField(default=True)
    address=models.CharField(max_length=100)
    profilepic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name
    

# ======================email===========================================
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {{request.user}}".format(title="Epmloyee crm"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )