from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _


class Cart:
    def __init__(self, request) -> None:
        """
        Initialize the cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart


    def add(self, product, quantity=1, replace_corrent_quantity=False):
        """
        Add the specified product to the cart if it exist
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : quantity}
        else : 
            if replace_corrent_quantity:
                self.cart[product_id]['quantity'] = quantity
            else: 
                self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, _('Product successfully added to cart'))

        self.save()


    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            messages.warning(self.request, _('Product successfully remove from cart'))
            self.save()
        


    def save(self):
        """
        Mark sesstion as modified to save changes
        """
        self.session.modified = True 


    def __iter__(self):
        prosuct_ids = self.cart.keys()
        products = Product.objects.filter(id__in=prosuct_ids)
        cart = self.cart.copy()

        for product in products :
            cart[str(product.id)]['product_obj'] = product


        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    
    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())
