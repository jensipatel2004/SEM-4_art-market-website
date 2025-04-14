from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import * 
import datetime
import json
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def store(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	
	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store.html', context)

@login_required
def cart(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

@login_required
def art_FSD(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'art_FSD.html', context)

@login_required
def artist(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'artist.html', context)

@login_required
def artwork(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'artwork.html', context)

@login_required
def contact(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'contact.html', context)


@login_required
def currentEvent(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'currentEvent.html', context)

@login_required
def pastEvent(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'pastEvent.html', context)

@login_required
def upcomingEvent(request):

	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'upcomingEvent.html', context)

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('art_FSD')  # Redirect to the home page or any other desired page
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def signup(request):
    
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # Save the new user
#             login(request, user)  # Automatically log the user in after signup
#             return redirect('login')  # Redirect to the login page

#     context = {'form': form}
#     return render(request, 'signup.html', context)

# def user_login(request):
	
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)  # login is the django method
#             return redirect('art_FSD')  # Redirect to the home page or any other desired page
			
    
#     context = {}        
#     return render(request, 'login.html',context)

# def user_logout(request):
#     logout(request)
#     return redirect('login')  # Redirect to the login page or any other desired page

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally create a Customer instance
            Customer.objects.create(user=user)
            login(request, user)
            return redirect('login')  # Redirect to your desired page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Changed from password1 to password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('art_FSD')  # Redirect to your desired page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to your desired page

@login_required
def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product  = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created=OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('item was added', safe=False)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)

		
	else:
		customer, order = guestOrder(request, data)
		
	total = float(data['form']['total'])
	order.transaction_id=transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
				customer=customer,
				order=order,
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				state=data['shipping']['state'],
				zipcode=data['shipping']['zipcode'],
			)
		
	return JsonResponse('payment complete', safe=False)