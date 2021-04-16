from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import LifeForm
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse

class BlogListView(View):
    def get(self, request, section=""):
        study_search = request.GET.get("study_search", False)
        print(study_search)
        if study_search :
            query = Q(title__icontains=study_search)
            query.add(Q(text__icontains=study_search), Q.OR)
            study_list = Study.objects.filter(query).select_related().order_by('-created_timestamp')[:10]
        else:
            study_list = Study.objects.all()
        life_list = Life.objects.all()
        for obj in study_list:
            obj.natural_updated = naturaltime(obj.last_edit_timestamp)
        for obj in life_list:
            obj.natural_updated = naturaltime(obj.last_edit_timestamp)

        cntx = {'study_list': study_list, 'life_list': life_list}

        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

        if is_ajax:
            html = render_to_string(
                template_name="blogs/studies-results-partial.html",
                context=cntx
            )
            data_dict = {"html_from_view": html}
            return JsonResponse(data=data_dict, safe=False)

        return render(request, 'blogs/main.html', cntx)


class TypeListView(View):
    def get(self, request, pk):
        return render(request, 'blogs/type_list.html')


class LifeListView(ListView):
    model = Life


class StudyListView(ListView):
    model = Study


class LifeCreate(LoginRequiredMixin, CreateView):
    model = Life
    fields = ['name', 'text', 'picture']
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