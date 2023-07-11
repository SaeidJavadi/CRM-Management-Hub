from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from crm.models import Common60


@login_required
def home(request):
    return render(request, 'crm/home.html')


@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')


class C60sListView(ListView):
    queryset = Common60.objects.all()
    context_object_name = "commons"
    template_name = "crm/c60_list.html"
