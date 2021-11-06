from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import *
from django.utils import timezone

class schooldetails(TemplateView):
    template_name = "schooladmin/schooldetails.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_det = SchoolDetails.objects.get(school_name="Lucky Driving School")
        context = {"Details": school_det}
        return context

class addschooldetails(TemplateView):
    template_name = "schooladmin/addschooldetails.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_det = SchoolDetails.objects.get(school_name="Lucky Driving School")
        context = {"Details": school_det}
        return context

    def post(self,request):
        address = request.POST.get("address")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        openingdays = request.POST.get("opening")
        time = request.POST.get("time")
        details = SchoolDetails.objects.filter(school_name="Lucky Driving School")
        details.update(address=address, city=city, phone=phone, email=email, opening_days=openingdays, time=time)
        return HttpResponseRedirect("/schooldetails/")

# ========================= trainer===============
class trainerdetails(ListView):
    model = Trainer
    template_name = "schooladmin/trainerdetails.html"
    context_object_name = "Trainer"


def addtrainerdetails(request):
    if request.method == "POST":
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
        date = request.POST.get("date")
        experience = request.POST.get("experience")

        if len(password) < 8:
            messages.error(request, "Password must be >8")
            return redirect("addtrainee")
        if not username.isalnum():
            messages.error(request, "Trainer accountname must be alpha numberic")
            return redirect("addtrainee")

        user = CustomUser.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.is_Trainer = True
        user.save()

        trainer_det = Trainer(user.pk, city=city, address=address, phone=phone, gender=gender, dateofjoin=date, photo=photo, experience=experience)
        trainer_det.save()

        messages.success(request, "Trainee Admission Done  Successfully")
    return render(request, 'schooladmin/addtrainer.html')


def assigntrainer(request):
    if request.method == "POST":
        trainerid = request.POST.get("cmbtrainer")
        traineeid = request.POST.getlist("chk")

        for t in traineeid:
            Trainee.objects.filter(trainee_id_id=t).update(trainer_id=trainerid)


    trainer_det = CustomUser.objects.all().filter(is_Trainer=True)
    print(trainer_det)
    trainee_det = Trainee.objects.all().filter(trainer_id__isnull=True,Status="Confirm")
    param = {
        "Trainee": trainee_det,
        "Trainer": trainer_det
    }

    return render(request, 'schooladmin/assigntrainer.html',param)

# ============================= trainee =====================

def traineedetails(request):
    if request.method == "POST":
        traineeid = request.POST.getlist("chk")
        for id in traineeid:
            CustomUser.objects.get(id=id).delete()
    trainee_det = Trainee.objects.all()
    param={
        "Trainee":trainee_det
    }
    return render(request, 'schooladmin/traineedetails.html', param)


def addtrainee(request):
    if request.method == "POST":
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

    return render(request, 'schooladmin/addtrainee.html')

def confirmtrainee(request):
    if request.method == "POST":
        traineeid = request.POST.getlist("chk")
        for t in traineeid:
            Trainee.objects.filter(trainee_id_id=t).update(Status='Confirm')

    trainee_det = Trainee.objects.filter(Status="not Confirm")
    param = {
        "Trainee": trainee_det
    }
    return render(request, 'schooladmin/confirmtrainee.html',param)

# ========================== feedback ===================
class viewfeedback(ListView):
    model = Feedback
    template_name = 'schooladmin/feedback.html'
    context_object_name = "Feedback"

    def post(self,request):
        feedid = request.POST.getlist("chk")
        for id in feedid:
            Feedback.objects.get(id=id).delete()
        return HttpResponseRedirect("/viewfeedback/")


# ======================== contactus ==================
class viewcontactus(ListView):
    model = Contactus
    template_name = 'schooladmin/viewcontactus.html'
    context_object_name = "Contact"

    def post(self,request):
        contact = request.POST.getlist("chk")
        for id in contact:
            Contactus.objects.get(id=id).delete()
        return HttpResponseRedirect("/viewcontactus/")

