from django.shortcuts import render


# Create your views here.
def homeView(request):

    context = {
        'page_title': 'Dashboard',
    }

    return render(request, 'home.html', context)