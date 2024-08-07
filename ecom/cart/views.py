from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Estore.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_details(request):

    #get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    return render(request,'cart_details.html',{"cart_products":cart_products, "quantities":quantities})


def cart_add(request):

    #get the cart
    cart = Cart(request)

    #test for the post 
    if request.POST.get('action') == 'post': #here the (action)'post' is for jquery used in product.html  || while the POST is for the webpage django understands.  

        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        #lookup product in models(db)
        product = get_object_or_404(Product, id= product_id)

        #Save to session
        cart.add(product=product,quantity =product_qty )

        cart_quantity =  cart.__len__()

        # response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response
    

def cart_delete(request):
    pass
def cart_update(request):
    pass    