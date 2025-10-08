from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from urllib.parse import urlencode
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Product # Ganti dengan model Anda

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    elif filter_type == "featured":
        product_list = Product.objects.filter(is_featured=True)
    else:
        product_list = Product.objects.filter(user=request.user)

    # Tambahkan baris ini untuk membuat instance form
    form = ProductForm()

    context = {
        'name': 'Gionado Gunawan',
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'form': form  # Tambahkan form ke context
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        
        # Redirect dengan toast message
        params = urlencode({
            'toast': 'Product created successfully!',
            'toast_type': 'success'
        })
        return redirect(f"{reverse('main:show_main')}?{params}")
    
    context = {
        'form': form
    }
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:    
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            # Tambahkan baris ini untuk mendapatkan username penjual
            'user_username': product.user.username if product.user else 'Anonymous'
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             # Redirect ke login dengan toast message
#             params = urlencode({
#                 'toast': 'Your account has been successfully created! Please login.',
#                 'toast_type': 'success'
#             })
#             return redirect(f"{reverse('main:login')}?{params}")
    
#     context = {'form': form}
#     return render(request, 'register.html', context)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Account created successfully!',
                'redirect_url': '/login/'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors,
                'message': 'Registration failed. Please check your input.'
            })
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# def login_user(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)

#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             response = HttpResponseRedirect(reverse("main:show_main"))
#             response.set_cookie('last_login', str(datetime.datetime.now()))
            
#             params = urlencode({
#                 'toast': f'Welcome back, {user.username}!',
#                 'toast_type': 'success'
#             })
#             response = HttpResponseRedirect(f"{reverse('main:show_main')}?{params}")
#             response.set_cookie('last_login', str(datetime.datetime.now()))
#             return response
#         else:
#             params = urlencode({
#                 'toast': 'Invalid username or password. Please try again.',
#                 'toast_type': 'error'
#             })
#             return redirect(f"{reverse('main:login')}?{params}")

#     else:
#         form = AuthenticationForm(request)
    
#     context = {'form': form}
#     return render(request, 'login.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({
                'success': True,
                'message': f'Welcome back, {user.username}!',
                'redirect_url': reverse('main:show_main')
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            # kirim error form
            return JsonResponse({
                'success': False,
                'errors': form.errors,
                'message': 'Invalid username or password.'
            }, status=400)
    return render(request, 'login.html', {'form': AuthenticationForm()})

def logout_user(request):
    """
    Logs the user out and returns a JSON response for AJAX calls.
    """
    user_name = request.user.username
    logout(request)
    
    # Prepare the JSON response
    response = JsonResponse({
        'success': True,
        'message': f'You have been logged out successfully. See you again, {user_name}!',
        'redirect_url': reverse('main:login') # Provide the URL to redirect to
    })
    
    # Delete the cookie from the response object before sending it
    response.delete_cookie('last_login')
    
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == 'POST':
        form.save()
        
        # Redirect dengan toast message
        params = urlencode({
            'toast': 'Product updated successfully!',
            'toast_type': 'success'
        })
        return redirect(f"{reverse('main:show_main')}?{params}")

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    
    # Redirect dengan toast message
    params = urlencode({
        'toast': 'Product deleted successfully!',
        'toast_type': 'success'
    })
    return HttpResponseRedirect(f"{reverse('main:show_main')}?{params}")

@csrf_exempt # Hanya digunakan untuk contoh, lebih baik gunakan token
def add_product_entry_ajax(request):
    if request.method == 'POST':
        try:
            name = strip_tags(request.POST.get("name"))
            description = strip_tags(request.POST.get("description"))
            price = int(request.POST.get('price'))
            category = request.POST.get('category')
            thumbnail = request.POST.get('thumbnail')
            is_featured = request.POST.get('is_featured') == 'on'
            
            # Asumsi pengguna sudah login
            user = request.user if request.user.is_authenticated else None

            new_product = Product.objects.create(
                user=user,
                name=name,
                description=description,
                price=price,
                category=category,
                thumbnail=thumbnail,
                is_featured=is_featured
            )
            
            return JsonResponse({"status": "success", "message": "Product created successfully"}, status=201)
        
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    
    return HttpResponse("Invalid request method", status=405)

@csrf_exempt
@login_required
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if product.user != request.user:
        return HttpResponseForbidden(json.dumps({"status": "error", "message": "Anda tidak memiliki izin untuk mengedit produk ini."}), content_type="application/json")

    if request.method == 'POST':
        try:
            # Mengambil data dari body request
            data = json.loads(request.body)
            
            product.name = data.get('name', product.name)
            product.description = data.get('description', product.description)
            product.price = int(data.get('price', product.price))
            product.category = data.get('category', product.category)
            product.thumbnail = data.get('thumbnail', product.thumbnail)
            product.is_featured = data.get('is_featured', product.is_featured)
            product.save()
            
            return JsonResponse({"status": "success", "message": "Produk berhasil diperbarui."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Terjadi kesalahan: {e}"}, status=400)

    return JsonResponse({"status": "error", "message": "Metode permintaan tidak valid."}, status=405)

@login_required
@require_POST  
@csrf_exempt   
def delete_product_ajax(request, id):
    try:
        product = Product.objects.get(pk=id)
        if product.user != request.user:
            return HttpResponseForbidden(json.dumps({
                "status": "error", 
                "message": "You do not have permission to delete this product."
            }), content_type="application/json")
        
        product.delete()
        return JsonResponse({"status": "success", "message": "Product deleted successfully!"})
    
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)