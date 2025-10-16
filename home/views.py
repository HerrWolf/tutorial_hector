from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def homeView(request):

    context = {
        'title': 'Home Page',
        'entity': 'Dashboard',
        'page_name': 'Home',
        'url_list': reverse('home'),
    }

    return render(request, 'home.html', context)