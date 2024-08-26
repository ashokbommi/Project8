from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from . models import Reg
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegisterInput(View):
    def get(selfself,request):
        return render(request,'register.html')
class Register(View):
    def post(self,request):
        r1=Reg(
            fname=request.POST["fname"],
            lname=request.POST["lname"],
            email=request.POST["email"],
            mobile=request.POST["mobile"],
            dob=request.POST["dob"],
            username=request.POST["username"],
            password=request.POST["password"],
            cpassword=request.POST["cpassword"],
        )
        r1.save()
        return HttpResponse('Your successfully registered')
class LoginInput(View):
    def get(self,request):
        return render(request,'login.html')
class Login(View):
    def post(self,request):
        qs=Reg.objects.filter(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if qs:
            return HttpResponse("Login Successul")
        else:
            return HttpResponse("Login Faild")