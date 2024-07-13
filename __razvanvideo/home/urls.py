#
#
#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('toate-videoclipurile-constanta', views.ToateVideoclipurilePageView.as_view(), name="toate-videoclipurile-constanta"),
]