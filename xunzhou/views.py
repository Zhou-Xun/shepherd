from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from .models import *

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode

class cats(View):
    def get(self, request):
        response = """
            cats
        """
        return HttpResponse(response)

class cat(View):
    def get(self, request, guess):
        response = """
            <main><body>
            <p>Your cat was """+escape(guess)+"""</p></body></main>
        """
        return HttpResponse(response)

class login(View):
    def get(self, request):
        return render(request, 'main/login.html')

    def post(self, request):
        # usr = get_object_or_404(user, pk=request.POST['name'])
        try:
            usr = user.objects.get(pk=request.POST['account'])
        except (KeyError, user.DoesNotExist):
            return render(request, "main/login.html")
        else:
            return HttpResponseRedirect(reverse('blogs:all_blogs'))

class loginV2(View):
    def get(self, request):
        # resp = "<pre>\nUser Data in Python:\n\n"
        # resp += "Login url: "+reverse('login')+"\n"
        # resp += "Logout url: "+reverse('logout')+"\n\n"
        # return HttpResponse(resp)
        return render(request, 'registration/login.html')

class OpenView(View) :
    def get(self, request):
        return render(request, 'xunzhou/loginV2.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'xunzhou/loginV2.html')

class ManualProtect(View) :
    def get(self, request):
        if not request.user.is_authenticated :
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'xunzhou/loginV2.html')

class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'xunzhou/loginV2.html')