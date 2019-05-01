from django.contrib import admin

# Register your models here.

from .models import Categories, Product, Stock, Order

class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Data Information', {'fields': ['title', 'description']}),
        ('Set Sorting Order', {'fields':['display_order']})
    ]

    list_display  = ('title','description', 'display_order')

    list_filter = ['title']

    search_fields = ['title', 'description']

admin.site.register(Categories, QuestionAdmin)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Order)
