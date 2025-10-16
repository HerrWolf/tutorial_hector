from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User
from .forms import UserForm
from django.core.paginator import Paginator
from django.contrib import messages


@login_required
def users_view(request):
    users_list = User.objects.order_by('-id')
    paginator = Paginator(users_list, 10)  # Show 10 users per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Users',
        'entity': 'Users',
        'page_name': 'List of Users',
        'url_list': reverse('users-view'),
        'users': page_obj,
    }

    return render(request, "users/users.html" , context)

@login_required
def user_update_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('users-view')
    else:
        form = UserForm(instance=user)

    context = {
        'title': 'Update User',
        'entity': 'Users',
        'page_name': 'Update User',
        'url_list': reverse('users-view'),
        'form': form,
    }

    return render(request, "users/create.html" , context)