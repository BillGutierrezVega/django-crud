from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

def product_image_path(instance, filename):
    return f'static/img/{filename}'
        
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    price = models.FloatField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
class Profesor(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sueldo = models.FloatField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'