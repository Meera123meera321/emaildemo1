from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def email(request):
    if request.method == "POST":
        mail = request.POST.get('id')
        message = request.POST.get('info')
        name = request.POST.get('name')

        send_mail(
            "Hi",
            "hi"+name+"Your request has been received"+message,
            settings.EMAIL_HOST_USER,
            [mail]


        )
    return  render(request, 'EMAILAPP/email.html')


