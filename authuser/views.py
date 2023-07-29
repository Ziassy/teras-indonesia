# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect
import re

@csrf_protect
def signup(request):
    if request.method=="POST": 
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.error(request,"Kata sandi tidak cocok. Silakan coba lagi.")
            return render(request,'account/signup.html') 
        
        # Password validation
        if len(password) < 8 or not re.search('\d', password) or not re.search('[!@#$%^&*]', password):
            messages.error(request, "Silakan masukkan setidaknya 8 karakter, sebuah angka, dan sebuah karakter khusus.")
            return render(request, 'account/signup.html')
                          
        try:
            if User.objects.get(email=email) or User.objects.get(username=username):
                # return HttpResponse("email and username already exist")
                messages.error(request,"Silahkan menggunakan email atau username lain")
                return render(request,'account/signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(username,email,password)
        user.is_active=True #yang baru signi[, isactive = false
        user.is_superuser=True #for access permission detail produk
        user.save()
        # If everything is successful, set a message and redirect to the success page
        messages.success(request, "Halo sahabat Nusantara, selamat akun kamu sudah berhasil dibuat. Silahkan masuk untuk melanjutkan")
        return redirect('success') 
    return render(request,"account/signup.html")

def successSignup(request):
    if not messages.get_messages(request):
        # If the user tries to access the success page directly without the required message,
        # redirect them back to the signup page or any other page you prefer.
        return redirect('signup')

    return render(request, 'account/success-signup.html')


@csrf_protect
def handlelogin(request):
    if request.method=="POST":

        username=request.POST['username']
        password=request.POST['password']
        myuser = authenticate(request, username=username, password=password)

        if myuser is not None and myuser.is_active:
            login(request,myuser)
            return redirect('/')

        else:
            messages.error(request,"Wrong Username or Password. Please try again.")
            return redirect('/auth/login')

    return render(request,'account/login.html')   

@csrf_protect #Prevention CSRF (Cross-Site Request Forgery)
def handle_logout(request):
    logout(request)
    # Untuk redirect ke page home ( / ) setelah logout
    return redirect('/')


