from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),

    url(r'^login', views.LoginView.as_view(), name='login'),

    url(r'^logout/(?P<userId>[0-9]+)/$', views.LogoutView.as_view(), name='logout'),
]
