from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render

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