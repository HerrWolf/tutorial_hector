from django.shortcuts import render
from django.urls import reverse


def homeView(request):

    context = {
        'title': 'Home Page',
        'entity': 'Dashboard',
        'page_name': 'Home',
        'url_list': reverse('home'),
    }

    return render(request, 'home.html', context)