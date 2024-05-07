from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Reg(AbstractUser):
    
    def __str__(self):
        return self.username


class bloom(models.Model):
    types=[
    ('Romantic','Romantic'),
    ('Birthday','Birthday'),
    ('Grand Opening','Grand Opening'),
    ('Condolence','Condolence'),
    ('Anniversary','Anniversary')
]

    name=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    price=models.IntegerField()
    category=models.CharField(choices=types,max_length=200)
    image=models.ImageField(upload_to ='media/')

    def __str__(self):
        return self.name
    



# class CartItem(models.Model):
#     bloom_item = models.ForeignKey(bloom, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     # You might want to associate this with a user as well, depending on your requirements
#     user = models.ForeignKey(Reg, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.quantity} x {self.bloom_item.name}"
