from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework.response import Response



def sent_details_via_email (email ,username,password):
    subject = "your Account HAs Been Created "
    message = f" Your Accout has been created ,Username={username} email={email} password={password}"
    email_from = settings.EMAIL_HOST
    
    send_mail(subject ,message, email_from ,[email])
    # user_obj = User.objects.get(email = email,username=username,password=password)
    # user_obj.save()

    return Response({'msg': sent_details_via_email}, status=200)
   







# def sent_details_via_email (email):
#     subject = "your Account HAs Been Created "
#     message = "Username={{request.user}} password={{request.user.password}}"
#     email_from = settings.EMAIL_HOST
    
#     send_mail(subject ,message, email_from ,[email])
#     user_obj = User.objects.get(email = email)
#     user_obj.save()








# def sent_details_via_email (email):
#     subject = "your Account HAs Been Created "
#     message = "Username={{request.user}} password={{request.user.password}}"
#     email_from = settings.EMAIL_HOST.USER
#     to_list=[email]
#     user_obj = User.objects.get(to_list = email)
#     user_obj.save()
    
#     send_mail(subject ,message, email_from ,to_list,fail_silently=True)
    

#     return Response({'msg': sent_details_via_email}, status=200)
























# def sent_details_via_email(subject, message, recipients):
# 	send_mail(
#     		subject="your Account HAs Been Created ",
#     		message="Username={{request.user}} password={{request.user.password}}",
#     		from_email=settings.EMAIL_HOST,
#     		recipient_list=recipients)