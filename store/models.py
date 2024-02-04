from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model) : 
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(User, on_delete = models.CASCADE , related_name = "products") #  add produced : this product added by who ? 
    name = models.CharField(max_length = 200 , null = False , blank  = False) 
    image = models.ImageField(null=True ,  default= "/placeholder.png")
    brand = models.CharField(max_length = 200 , null = True , blank = True)
    category = models.CharField(max_length = 200 , null = True , blank = True)
    description = models.TextField()
    # rating = models.FloatField()
    rating = models.DecimalField(max_digits = 7 , decimal_places = 2 , null = True, default = 0  )
    num_reviews  = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits = 7 , decimal_places = 2 , default = 0  )
    count_in_stock  = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self): 
        return self.name 
    
    class Meta : 
        db_table = "products"




class Order (models.Model) : 
    is_paid = models.BooleanField(default = False)

