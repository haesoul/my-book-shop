from django.contrib import admin

from cart.models import *
from main.models import *
from orders.models import *
from users.models import *

admin.site.register(Product)
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Location)

admin.site.register(OrderItem)
admin.site.register(Order)

