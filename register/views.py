from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, User
from django.views.generic import View
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse


# Create your views here.


class HomeView(View):
    template_name = 'register/home.html'

    def get(self, request):
        return render(request, self.template_name)


class BoardView(View):
    template_name = 'register/success.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs['userId']
        profiles = get_object_or_404(Profile, pk=id)

        return render(request, self.template_name, {'profiles': profiles})


class FailedView(View):
    template_name = 'register/failed.html'

    def get(self, request):
        return render(request, self.template_name)


class SignUpView(View):
    template_name = 'register/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        person = Profile()
        user = User()
        check = 0
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
            person.is_active = True
            person.save()
            check = 1
            context = {"profiles": person}
        if check == 1:
            return render(request, 'register/success.html', context)
        else:
            return render(request, 'register/signup.html')


class LoginView(View):
    template_name = 'register/login.html'

    def get(self, request):

        try:
            LoggedInUser = Profile.objects.get(is_active=True)
            return render(request, 'register/success.html', {"profiles": LoggedInUser})
        except ObjectDoesNotExist:
            return render(request, self.template_name)

    def post(self, request):
        usern = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username=usern, password=passw)
        if user is not None:
            to_activate = Profile.objects.get(user__username=usern)
            to_activate.is_active = True
            to_activate.save()
            return render(request, 'register/success.html', {"profiles": to_activate})
        else:
            return render(request, "register/failed.html")


class LogoutView(View):
    template_name = 'register/logout.html'

    def get(self, request, *args, **kwargs):
        Id = self.kwargs['userId']
        profiles = get_object_or_404(Profile, pk=Id)
        profiles.is_active = False
        profiles.save()

        return render(request, self.template_name)
