from django.contrib import admin
from .models import ProdukItem, Category, CulturalOrigin, OrderProdukItem, Order, AlamatPengiriman, Payment

class MasterCategoryAdmin(admin.ModelAdmin):
    list_display = ['code_category','nama_category', 'banner_category', 'desc_category' ]

class MasterCultureAdmin(admin.ModelAdmin):
    list_display = ['nama_asal_budaya','code_budaya' ]
class ProdukItemAdmin(admin.ModelAdmin):
       list_display = ['nama_produk', 'harga', 'harga_diskon', 'slug', 'deskripsi', 'gambar', 'gambar_detail',
                    'main_banner_detail', 'label', 'kategori', 'asal_budaya', 'lokasi',
                    'jumlah_orang', 'max_stok', 'current_stok', 'rating', 'banner_history_prod',
                    'desc_history_one', 'desc_history_two', 'desc_history_three',
                    'is_popular', 'is_recomended']

# class OrderProdukItemAdmin(admin.ModelAdmin):
#     list_display = ['user', 'ordered', 'produk_item', 'quantity']

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['user', 'tanggal_mulai', 'tanggal_order', 'ordered']

# class AlamatPengirimanAdmin(admin.ModelAdmin):
#     list_display = ['user', 'alamat_1', 'alamat_2', 'kode_pos', 'negara']

# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'amount', 'timestamp', 'payment_option', 'charge_id']

admin.site.register(ProdukItem, ProdukItemAdmin)
admin.site.register(Category, MasterCategoryAdmin)
admin.site.register(CulturalOrigin, MasterCultureAdmin)
# admin.site.register(OrderProdukItem, OrderProdukItemAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(AlamatPengiriman, AlamatPengirimanAdmin)
# admin.site.register(Payment, PaymentAdmin)
