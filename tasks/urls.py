from django.urls import path
from tasks.views import (
    task, 
    create_task,
    delete_task, 
    
    usuarios, 
    create_user,
    delete_user,
    
    list_products, 
    create_product,
    delete_product,
    
    list_teachers,
    create_teacher,
    delete_profesor
    )

urlpatterns = [
    path('', task),
    path('new/', create_task, name='create_task'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),
    
    path('user/', usuarios),
    path('user/create', create_user, name='create_user'),
    path('delete_user/<int:user_id>', delete_user, name='delete_user'),
    
    path('products/', list_products),
    path('products/create', create_product, name='create_product'),
    path('delete_products/<int:product_id>', delete_product, name='delete_product'),
    
    path('profesor/', list_teachers),
    path('profesor/create', create_teacher, name='create_teacher'),
    path('delete_profesor/<int:profesor_id>', delete_profesor, name='delete_profesor'),
]
