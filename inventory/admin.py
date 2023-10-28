from django.contrib import admin
from .models import EquipmentCategory,Products,Transactions
#Equipment Admin View 
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display= ('category_name','date_created',  )#Display Data in A List
    list_filter=('date_created',)
    search_fields = ('category_name',)#Add A search Field
#Products Display Admin
class ProductsAdmin(admin.ModelAdmin):
    exclude=('available_stock',)
    list_display= ('category_id','product_name','unit_price','available_stock','unit_measure','date_updated'  )#Display Data in A List
    list_filter=('date_updated',)
    search_fields = ('product_name','category_id')#Add A search Field
#Transactions Display Admin
class TransactionsAdmin(admin.ModelAdmin):
    list_display= ('product_id','transaction_type','stock_taken','transaction_amount','transaction_date' )#Display Data in A List
    list_filter=('transaction_date',)
    search_fields = ('product_id','transaction_type')#Add A search Field
#Register Models
admin.site.register(EquipmentCategory,EquipmentCategoryAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Transactions,TransactionsAdmin)
