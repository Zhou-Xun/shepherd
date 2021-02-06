from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
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