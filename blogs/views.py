from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render
from .models import *

class BlogListView(View):
    def get(self, request):
        blog_list = Blog.objects.all()
        cntx = {'blog_list': blog_list}
        return render(request, 'blogs/main.html', cntx)

class LifeListView(View):
    model = Life
    def get(self, request):
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = {modelname+'_list': stuff}
        return render(request, 'blogs/'+modelname+'_list.html', cntx)

from django.views import generic
class StudyListView(generic.ListView):
    model = Study

class IndexView(View):
    def get(self, request, pk):
        modelName = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.get(pk=pk)
        return render(request, 'blogs/'+modelName+'_detail.html', {modelName:stuff})

class BlogDetailView(IndexView):
    model = Blog

class LifeDetailView(IndexView):
    model = Life

class StudyDetailView(IndexView):
    model = Study

