from django.db import models

"""
Все объкты таблицы -- Post.objects.all() --> select - from posts

один объект по условию -- Post.objects.get(id=1)

объекты по условию не уникальному(несколько) -- Post.objects.filter(title='title')

создать объект -- Post.objects.create(title='title', content='content')

"""
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1024)
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey (Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True, )



    def __str__(self):
        return f'{self.title} - {self.content}'
