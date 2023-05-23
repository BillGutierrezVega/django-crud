from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profesor, Task, User, Product


# Create your views here.
def task(request):
    tasks = Task.objects.all()
    return render(request, 'list_task.html', {'tasks': tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect(reverse('tareas:task'))

def delete_task(_request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')

# usuarios
def usuarios(request):
    users = User.objects.all()
    return render(request, 'user_form.html', {'users': users})

def create_user(request):
    user = User(username=request.POST['username'], password=request.POST['password'])
    user.save()
    return redirect('/tasks/user/')

def delete_user(_request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/tasks/user/')

# productos
def list_products(request):
    productos = Product.objects.all()
    return render(request, 'list_product.html', {'productos': productos})

def create_product(request):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    image = request.FILES['image']
    
    product = Product(name=name, description=description, price=price, image=image)
    
    product.save()
    return redirect('/tasks/products/')

def delete_product(_request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('/tasks/products/')

# Profesores
def list_teachers(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'profesores':profesores})

def create_teacher(request):
    teacher = Profesor(name=request.POST['name'], last_name=request.POST['last_name'], sueldo=request.POST['sueldo'])
    teacher.save()
    return redirect('/tasks/profesor/')

def delete_profesor(_request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    profesor.delete()
    return redirect('/tasks/profesor/')