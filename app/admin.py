from django.contrib import admin
from . import models
# Register your models here.=
admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.SoldProduct)
admin.site.register(models.Sales)
admin.site.register(models.OtherIncome)
admin.site.register(models.Expense)
admin.site.register(models.Purchase)