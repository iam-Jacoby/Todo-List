from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from api.views import TaskViewsetView,SignupView
from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path

router.register("v2/task",TaskViewsetView,basename="task")

urlpatterns = [
    path("token",ObtainAuthToken.as_view()),
    path("regiser/",SignupView.as_view()),
] + router.urls