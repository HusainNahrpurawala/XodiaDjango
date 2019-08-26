from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, User
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse


# Create your views here.


class HomeView(View):
    template_name = 'register/home.html'

    def get(self, request):
        return render(request, self.template_name)


class SignUpView(View):
    template_name = 'register/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        person = Profile()
        user = User()
        usern = request.POST['username']
        passw = request.POST['password']
        email = request.POST['email']
        mobile = request.POST['mobile']
        college = request.POST['college']
        if usern != "" and passw != "" and email != "" and mobile != "" and college != "":
            user.set_password(passw)
            user.username = usern
            user.email = email
            user.save()
            person.user = user
            person.college = college
            person.mobile = mobile
            person.save()
            context = {"profiles": person}
            auth = authenticate(username=usern, password=passw)
            login(request, auth)
            return render(request, 'register/success.html', context)
        else:
            return render(request, self.template_name)


class LoginView(View):
    template_name = 'register/login.html'

    def get(self, request):
        if request.user.is_authenticated():
            user = request.user.pk
            profiles = Profile.objects.get(pk=user)
            context = {
                "profiles": profiles,
            }
            return render(request, 'register/success.html', context)
        else:
            return render(request, self.template_name)

    def post(self, request):
        usern = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username=usern, password=passw)
        if user is not None:
            to_activate = Profile.objects.get(user__username=usern)
            login(request, user)
            return render(request, 'register/success.html', {"profiles": to_activate})
        else:
            return render(request, "register/failed.html")


class LogoutView(View):
    template_name = 'register/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)

        return render(request, self.template_name)
