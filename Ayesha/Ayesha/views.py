from django.shortcuts import render
from django.core.mail import send_mail
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
      subject,message, email,
    ["Write your mail here"],
    )
    return render(request,"index.html")


    
    
