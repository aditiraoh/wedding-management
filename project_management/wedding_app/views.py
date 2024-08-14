from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from .models import Category, Item

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('categories')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def category_items(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = Item.objects.filter(category=category)
    return render(request, 'category_items.html', {'category': category, 'items': items})
from django.shortcuts import redirect, get_object_or_404
from .models import Item

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # Implement logic to add item to cart (you may use session for simplicity)
    cart = request.session.get('cart', [])
    cart.append(item.id)
    request.session['cart'] = cart
    return redirect(view_orders)

def view_orders(request):
    cart = request.session.get('cart', [])
    items_in_cart = Item.objects.filter(pk__in=cart)
    return render(request, 'view_orders.html', {'items_in_cart': items_in_cart})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        if item.id in cart:
            cart.remove(item.id)
        request.session['cart'] = cart
        return redirect('view_orders')
    return render(request, 'confirm_delete.html', {'item': item})

def order_placed(request):
    request.session['cart'] = []  # Clear the cart
    return render(request, 'order_placed.html')
