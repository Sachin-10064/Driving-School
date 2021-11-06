from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from .models import Trainer, Trainee, CustomUser, Feedback, ridedetail



def ridedetails(request):
    username = request.session['userinfo']
    trainee = CustomUser.objects.get(username=username)
    traineeid =trainee.id
    ride_det = ridedetail.objects.filter(trainee=traineeid)
    param = {
        "details": ride_det
    }
    return render(request, 'trainee/ridedetails.html', param)


def postfeedback(request):
    username = request.session["userinfo"]
    if request.method == "POST":
        rating = request.POST.get("rating")
        feedback = request.POST.get("feedback")

        feed = Feedback(username=username, feedback_text=feedback, rating=rating, date=timezone.now())
        feed.save()
    return render(request, 'trainee/postfeedback.html')


def mytrainer(request):
    username = request.session["userinfo"]
    trainee = CustomUser.objects.get(username=username)
    traineeid = trainee.id

    traineedetails = Trainee.objects.get(trainee_id_id=traineeid)
    trainerid = traineedetails.trainer_id
    print(trainerid)

    if trainerid == None:
        return render(request, 'trainee/mytrainer.html')
    else:
        trainerdetails = Trainer.objects.get(trainer_id_id=trainerid)
        print(trainerdetails.photo)
        trainer = CustomUser.objects.get(id=trainerid)
        param = {
             "Tra":trainer,
             "Trainer":trainerdetails
        }
        return render(request, 'trainee/mytrainer.html',param)

def traineeProfile(request):
    username = request.session["userinfo"]
    trainee = CustomUser.objects.get(username=username)
    traineeid = trainee.id
    trainee_det = Trainee.objects.get(trainee_id_id=traineeid)
    param ={
        "Trainee":trainee_det
    }
    return render(request, 'trainee/traineeProfile.html',param)