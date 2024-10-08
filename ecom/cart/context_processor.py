#define this context processor for our cart in the settings.py under templates


from .cart import Cart

#create a context processor so that our cart can work on all pages
def cart(request):
    #Return the default data form the cart
    return {'cart': Cart(request)}