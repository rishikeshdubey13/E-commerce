from Estore.models import Product

class Cart():
    def __init__(self, request):#initializes the cart   
        self.session = request.session

        #GEt the current session key if exists:
        cart = self.session.get('session_key')

        # if the user is new, create new sesion key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure that cart is available on the pages of the website
        self.cart = cart

    
    def add(self, product,quantity):#allows to add things to cart
        product_id = str(product.id)
        product_qty =str(quantity)

        #logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        
        self.session.modified = True

    def __len__(self):#returns the length of the cart
        return len(self.cart)
    
    def get_prods(self): #Lookup stuff in the cart
        #get the product IDs from the cart
        product_ids = self.cart.keys()
        #use ids to lookup product in database
        products= Product.objects.filter(id__in = product_ids)
        #return looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #get cart
        ourcart = self.cart

        #update dictionary(cart)
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart 
        return thing
    
    def delete(self,product):
        product_id = str(product)

        #delete product from Dcictionary(cart)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
    
    def cart_total(self):
        #Get the product IDs from the cart
        product_ids = self.cart.keys()
        #use ids to lookup product in database
        products= Product.objects.filter(id__in = product_ids)
        #get quantities
        quantities = self.cart
        # start counting form 0
        total = 0
        for key, value in quantities.items():
            #convert key string into int fro calculation
            key  = int(key)

            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total  =total+  (product.sale_price * value)
                    else:
                        total  =total+  (product.price * value)
  
        return total
        