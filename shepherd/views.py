from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello xunzhou !")

def funky(request):
    response = """
        <html><body><p>This is the funky function sample</p>
        <p>This sample code is available at 
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>
    """
    return HttpResponse(response)

def danger(request):
    response = """
        <html><body>
        <p>Your guess was """+escape(request.GET['guess'])+"""</p></body></html>
    """
    return HttpResponse(response)

def rest(request, guess):
    response = """
            <html><body>
            <p>Your guess was """ + escape(guess) + """</p></body></html>
        """
    return HttpResponse(response)

class RestMainView(View):
    def get(self, request, guess):
        response = """
            <html><body>
            <p>Your guess was """+escape(guess)+"""</p></body></html>
        """
        return HttpResponse(response)

def bounce(request):
    return HttpResponseRedirect('https://www.baidu.com/')

class GameView(View):
    def get(self, request, guess):
        x = {'guess': int(guess)}
        return render(request, '../templates/html/cond.html', x)