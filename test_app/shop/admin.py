from django.contrib import admin


from .models import Shop


class ShopAdmin(admin.ModelAdmin):

    readonly_fields = ('shop_id',)
    list_display = ('__str__', 'shop_id', 'name',)
    search_fields = ('shop_id', 'name',)
    fields = ('shop_id', 'name',)


admin.site.register(Shop, ShopAdmin)
