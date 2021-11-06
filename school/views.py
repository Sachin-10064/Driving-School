from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as dj_login, logout
from .models import Contactus, SchoolDetails,CustomUser, Trainee

# Create your views here.

class home(TemplateView):
    template_name = "school/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_det = SchoolDetails.objects.get(school_name="Lucky Driving School")
        context = {"Details": school_det}
        return context
    def post(self,request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        messages = request.POST.get("message")

        contact_det = Contactus(name=name, email=email, query=messages, date=timezone.now())
        contact_det.save()
        return HttpResponseRedirect("/")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        # print(username, pass1)
        user = authenticate(username=username, password=pass1)
        if user is not None:
            request.session["userinfo"] = username
            dj_login(request, user)

            if user.is_SchoolAdmin == True:
                messages.success(request, "Successfully Logged In")
                return redirect('schooldetails')

            elif user.is_Trainer == True:
                messages.success(request, "Successfully Logged In")
                return redirect('viewtrainee')

            elif user.is_Trainee == True:
                messages.success(request, "Successfully Logged In")
                return redirect('ridedetails')
        else:
            messages.warning(request, "Invalid credential, Please Signup First")
            return redirect('/')

    return render(request, "school/login.html")

def dologout(request):
    if 'userinfo' in request.session:
        del (request.session['userinfo'])
    logout(request)
    messages.success(request, "You have successfully logout")

    return redirect("homepage")


class addtraineeofline(TemplateView):

    def post(self,request):
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        photo = request.FILES["photo"]
        username = request.POST.get("userid")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        admissionmode = request.POST.get("admissionmode")
        transaction = request.POST.get("tranNum")
        fee = request.POST.get("fee")

        if admissionmode == "online":
            status = "not Confirm"
        else:
            status = "Confirm"

        if len(password) < 8:
            messages.error(request, "Password must be >8")
            return redirect("addtrainee")
        if not username.isalnum():
            messages.error(request, "Trainer accountname must be alpha numberic")
            return redirect("addtrainee")

        user = CustomUser.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.is_Trainee = True
        user.save()

        trainee_det = Trainee(user.pk, City=city, Address=address, Phone=phone, Gender=gender, DateOfAdmission=timezone.now(), Photo=photo, Admissionmode=admissionmode, Transactionnumber=transaction, Fees=fee, Status=status)
        trainee_det.save()

        messages.success(request, "Trainee Admission Done  Successfully")
        return HttpResponseRedirect("/")