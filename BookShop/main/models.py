from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name='Имя товара')
    slug = models.SlugField(unique=True,max_length=55)
    description = models.TextField(blank=True, null=True, max_length=5000,verbose_name='Описание')
    photo = models.ImageField(upload_to='products-photo/',blank=True, null=True,verbose_name='Фото')

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлено')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Стоимость товара')
    stock = models.PositiveIntegerField()  # количество на складе
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='category_products',verbose_name='Категория')
    genre = models.ManyToManyField('Genre',  related_name='genre_products',verbose_name='Жанр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True, max_length=55)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True, max_length=55)
    def __str__(self):
        return self.name




