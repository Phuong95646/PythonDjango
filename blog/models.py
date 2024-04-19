import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # file = models.FileField(null=True, blank=True, upload_to='Files')
    content = models.TextField()

    class Meta:
        db_table = "product"
        

    def __str__(self):
        return self.name
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)
