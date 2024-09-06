from django.contrib import admin
from .models import Category, Customer, Product, Order,Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)


#Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile
    

#Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']

    inlines = [ProfileInline]

#in django unregister and register again

#unregister
admin.site.unregister(User)

#register
admin.site.register(User, UserAdmin)