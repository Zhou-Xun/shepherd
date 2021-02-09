from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello xunzhou !")

def funky(request):
    response = """
        <main><body><p>This is the funky function sample</p>
        <p>This sample code is available at 
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></main>
    """
    return HttpResponse(response)

def danger(request):
    response = """
        <main><body>
        <p>Your guess was """+escape(request.GET['guess'])+"""</p></body></main>
    """
    return HttpResponse(response)

def rest(request, guess):
    response = """
            <main><body>
            <p>Your guess was """ + escape(guess) + """</p></body></main>
        """
    return HttpResponse(response)

class RestMainView(View):
    def get(self, request, guess):
        response = """
            <main><body>
            <p>Your guess was """+escape(guess)+"""</p></body></main>
        """
        return HttpResponse(response)

def bounce(request):
    return HttpResponseRedirect('https://www.baidu.com/')

class GameView(View):
    def get(self, request, guess):
        x = {'guess': int(guess)}
        return render(request, '../templates/main/cond.html', x)

def simple(request):
    context = {'zap': '42',
               'txt': '<b>bold</b>',
               'outer': {'inner': '38'}}
    return render(request, '../templates/main/simple.html', context)

def loop(request):
    f = ['Apple', 'Orange', 'Banana', 'Lychee']
    n = ['peanut', 'cashew']
    x = {'fruits': f, 'nuts': n, 'zap': '42'}
    return render(request, '../templates/main/loop.html', x)

