from django.http import HttpResponse ,  JsonResponse
from .models import Product
from django.views import View


class ProductsList(View) : 
    def get(self , request ) : 
        products = list(Product.objects.values())
        return JsonResponse({"data" : products})
    def post(self , request) : 
        # TODO create product with data 

        pass
class ProductList(View) :
    def get(self , request , id ) : 
        # TODO get product associated with id
        pass
    def put(self , request) :
        # TODO update product associated with id
        pass
    def delete(self , request) : 
        # TODO delete product associated with id

        pass 
# GET 
# POST : Create New Record on database 
# PUT, PATCH : Update Database 
# DELETE : delete record from database 

import json
def list_products(request) : 
    if request.method not in ["GET" , "POST"] : 
        return JsonResponse({'error' : "Bad Method"})
    
    if request.method == "POST" : 
        data = request.body 
        data_dict = json.loads(data)
        Product.objects.create(user_id = data_dict["user_id"] , name = data_dict["name"] , brand = data_dict["brand"] , category = data_dict["category"] , description  = data_dict["description"], 
                               rating = data_dict["rating"] , num_reviews = data_dict["num_reviews"] , count_in_stock = data_dict["count_in_stock"])
        return JsonResponse({"detail" : "Created Successfully"})
    # print(request.body)
    # print(request.method)
    products =  list(Product.objects.values())
    # print(products)

    return JsonResponse({"data" : products})
    # return HttpResponse("<h1>Hello From Django </h1>")
def get_product(request , id) : 

    if request.method not in ["GET" , "PUT" , "DELETE"] : 
        return JsonResponse({'error' : "Bad Method"})
    
    if request.method == "PUT" : 
        data = request.body 
        data_dict = json.loads(data) 
        Product.objects.filter(id = id).update(**data_dict)
        return JsonResponse({"detail" : "Updated Successfully"})
    if request.method == "DELETE" : 
        Product.objects.filter(id = id).delete()
        return JsonResponse({"detail" : "Deleted Successfully"})
    try :
        product = Product.objects.get(id = id)


        data = {
            "name" : product.name, 
            "brand" : product.brand ,
            "user" : product.user.username
        }
        # print(product)
        return JsonResponse(data)
    except Product.DoesNotExist : 
        return JsonResponse({"detail" : "Product does not exist"})
    
