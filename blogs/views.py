from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import LifeForm


class BlogListView(View):
    def get(self, request):
        blog_list = Blog.objects.all()
        cntx = {'blog_list': blog_list}
        return render(request, 'blogs/main.html', cntx)


class LifeListView(ListView):
    model = Life


class StudyListView(ListView):
    model = Study


class LifeCreate(LoginRequiredMixin, CreateView):
    model = Life
    fields = ['lifeName', 'lifeText', 'picture']
    success_url = reverse_lazy('blogs:lives')


class LifeUpdate(LoginRequiredMixin, UpdateView):
    model = Life
    fields = '__all__'
    success_url = reverse_lazy('blogs:lives')


class LifeDelete(LoginRequiredMixin, DeleteView):
    model = Life
    fields = '__all__'
    success_url = reverse_lazy('blogs:lives')


class StudyCreate(LoginRequiredMixin, CreateView):
    model = Study
    fields = '__all__'
    success_url = reverse_lazy('blogs:lives')


class StudyUpdate(LoginRequiredMixin, UpdateView):
    model = Study
    fields = '__all__'
    success_url = reverse_lazy('blogs:lives')


class StudyDelete(LoginRequiredMixin, DeleteView):
    model = Study
    fields = '__all__'
    success_url = reverse_lazy('blogs:lives')



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

# class LifeListView(View):
#     model = Life
#     def get(self, request):
#         modelname = self.model._meta.verbose_name.title().lower()
#         stuff = self.model.objects.all()
#         cntx = {modelname+'_list': stuff}
#         return render(request, 'blogs/'+modelname+'_list.html', cntx)
#
#     def post(self, request):
#         if request.POST['hidden'] == 1:
#             return HttpResponseRedirect(reversed('blogs:lives'))
#         else:
#             return render(request, 'blogs/life_list.html', {'life_list': Life.objects.all()})