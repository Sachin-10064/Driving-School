from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from .models import Trainer, Trainee, Tips, CustomUser,ridedetail


def viewtrainee(request):
    username = request.session['userinfo']
    trainer= CustomUser.objects.get(username=username)
    trainerid = trainer.id
    trainee_details = Trainee.objects.filter(trainer_id=trainerid)
    param ={
        "Trainee":trainee_details
    }
    return render(request, 'trainer/viewtrainee.html',param)

def trainerProfile(request):
    username = request.session['userinfo']
    trainer = CustomUser.objects.get(username=username)
    trainerid = trainer.id
    trainerDet = Trainer.objects.get(trainer_id_id=trainerid)

    param ={
        "Trainer": trainerDet
    }

    return render(request, 'trainer/trainerProfile.html',param)

def addtips(request):
    username = request.session['userinfo']
    if request.method == "POST":
        tips = request.POST.get("tips")

        tip_det = Tips(tipstext=tips,username=username,postdate=timezone.now())
        tip_det.save()

    return render(request, 'trainer/addtips.html')

def viewride(request):
    username = request.session['userinfo']
    trainer = CustomUser.objects.get(username=username)
    trainerid = trainer.id
    ride_det = ridedetail.objects.filter(trainer_id=trainerid)
    param ={
        "Details": ride_det
    }
    return render(request, 'trainer/trainer_ridedetails.html',param)

def addridedetails(request):
    username = request.session['userinfo']
    trainer = CustomUser.objects.get(username=username)
    trainerid = trainer.id
    traineeDetails = Trainee.objects.filter(trainer_id=trainerid)
    if request.method == "POST":
        traineeid = request.POST.get("id")
        fromto = request.POST.get("fromto")
        durations = request.POST.get("duration")
        performance = request.POST.get("performance")

        details = ridedetail(trainer_id=trainerid, trainee=traineeid, getdate=timezone.now(), from_to=fromto, timeduration=durations, traineeperformance=performance)
        details.save()

    param = {
        "trainee":traineeDetails
    }
    return render(request, 'trainer/addridedetails.html',param)