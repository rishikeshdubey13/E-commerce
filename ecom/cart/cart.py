class Cart():
    def __init__(self, request):
        self.session = request.session

        #GEt the current session key if exists:
        cart = self.session.get('session_key')

        # if the user is new, create new sesion key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure that cart is available on the pages of the website
        self.cart = cart