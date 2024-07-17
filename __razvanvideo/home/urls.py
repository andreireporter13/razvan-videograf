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
    path('video-nunta-constanta', views.PortofoliuNuntaPageView.as_view(), name="video-nunta-constanta"),
    path('video-botez-constanta', views.PortofoliuBotezPageView.as_view(), name="video-botez-constanta"),
    path('alte-evenimente-constanta', views.PortofoliuAlteEvenimentePageView.as_view(), name="alte-evenimente-constanta"),
    path('despre-mine', views.DespreMinePageView.as_view(), name="despre-mine"),
    path('contact-constanta', views.ContactPageView.as_view(), name="contact-constanta"),
]