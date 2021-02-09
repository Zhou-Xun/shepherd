from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.html import escape
from django.views import View
from django.shortcuts import render

class GameView(View):
    def get(self, request, guess):
        x = {'guess': int(guess)}
        return render(request, '../templates/note/cond2.html', x)

class FirstView(View):
    def get(self, request):
        response = """
            Test First View
        """
        return HttpResponse(response)

class SecondView(View):
    def get(self, request):
        u = reverse_lazy('xunzhou:cats')
        u2 = reverse('xunzhou:cat', args=[42])
        ctx = {'x1': u, 'x2': u2}
        return render(request, '../templates/note/second.html', ctx)

