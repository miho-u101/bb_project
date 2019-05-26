from django.db import models

# Create your models here.

class Cruiser(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)
    charge1 = models.IntegerField(default=0)
    charge2 = models.IntegerField(default=0)

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)

#データ型
#CharField(max_length=100)
#IntegerField(default=0)
#DateField
#BooleanField
#EmailField(max_length=200)