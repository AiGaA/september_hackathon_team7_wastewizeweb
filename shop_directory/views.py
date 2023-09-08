from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Shop
from .forms import ShopForm

# Create your views here.


def view_shop_directory(request):
    return render(request, 'shop_directory/shop.html')


def add_shop(request):
    form = ShopForm(request.POST, request.FILES)

    if request.method == "POST":
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return redirect(reverse('home'))
    else:
        form = ShopForm()
    return render(request, 'shop_directory/add_shop.html', {'form': form})
