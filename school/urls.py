from django.urls import path
from . import views, adminviews, traineeviews, trainerviews

urlpatterns = [
    path("", views.home.as_view(), name="homepage"),
    path("login/",views.login, name="login"),
    path("dologout/", views.dologout, name="logout"),
    # path("contactus/", views.contactus, name="contactus"),
    path('addtraineeofline/', views.addtraineeofline.as_view(), name="addtraineeofline"),

    # ======================= Admin Tasks ===========
    path("schooldetails/", adminviews.schooldetails.as_view(), name="schooldetails"),
    path("addschooldetails/", adminviews.addschooldetails.as_view(), name="addschooldetails"),

    path("trainerdetails/", adminviews.trainerdetails.as_view(), name="trainerdetails"),
    path("addtrainerdetails/", adminviews.addtrainerdetails, name="addtrainerdetails"),
    path("assigntrainer/", adminviews.assigntrainer, name="assigntrainer"),

    path("traineedetails/", adminviews.traineedetails, name="traineedetails"),
    path("addtrainee/", adminviews.addtrainee, name="addtrainee"),
    path("confirmtrainee/", adminviews.confirmtrainee, name="confirmtrainee"),

    path("viewfeedback/", adminviews.viewfeedback.as_view(), name="viewfeedback"),
    path("viewcontactus/", adminviews.viewcontactus.as_view(), name="viewcontactus"),
    # path("", adminviews., name=""),
    # path("", adminviews., name=""),

    # ============================ trainee ==========================
    path("ridedetails/", traineeviews.ridedetails, name="ridedetails"),
    path("postfeedback/", traineeviews.postfeedback, name="postfeedback"),
    path("mytrainer/", traineeviews.mytrainer, name="mytrainer"),
    path("traineeProfile/", traineeviews.traineeProfile, name="traineeProfile"),

    # =========================== trainer ===========================
    path("viewtrainee/", trainerviews.viewtrainee, name="viewtrainee"),
    path("trainerProfile/", trainerviews.trainerProfile, name="trainerProfile"),
    path("addtips/", trainerviews.addtips, name="addtips"),
    path("viewride/", trainerviews.viewride, name="viewride"),
    path("addridedetails/", trainerviews.addridedetails, name="addridedetails")
    # path("", trainerviews., name="")
]