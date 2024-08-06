from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth. forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
# Home page
@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

# @login_required(login_url='login')
# def detail(request):
#     return render(request, "store/detail.html")


# product lists and details
def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {'product': product})



# cart views
# def cart_item(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     return render(request, 'store/cart.html', {'cart_items': cart_items})

# add/remove to cart
# def add_to_cart(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#         messages.success(request, "Item has been added to Cart")
#     return redirect('cart')

# def remove_from_cart(request, pk):
#     cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
#     cart_item.delete()
#     messages.success(request, "Item has been removed from Cart")
#     return redirect('cart')



# product review
# def review_create(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#     if request.method == 'POST':
#         form  = ProductReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.product = product
#             review.user = request.user
#             review.save()
#             return redirect('product_detail', pk=product_pk)
#     else:
#         form = ProductReviewForm()
#     return render(request, 'store/review_form.html', {"form": form, "product":product})










#  User account authentication and profile details
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
        else:
            messages.error(request, "Please correct the error below")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'store/profile.html', {'user_form': user_form, 'profile_form': profile_form})


# signup page
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'store/register.html', {'form': form})

# login page
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)    
                # redirect tin the default page
                next_url = request.POST.get('next', reverse('home'))
                return redirect(next_url)
            else:
                return HttpResponse("Invalid  login credentials", status=401)
        else:
            return render(request, 'store/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# logout page
def logout(request):
    auth_logout(request)
    return redirect(reverse('login'))
