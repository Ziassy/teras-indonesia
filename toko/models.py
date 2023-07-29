from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

PILIHAN_LABEL = (
    ('NEW', 'primary'),
    ('SALE', 'info'),
    ('BEST', 'danger'),
)

PILIHAN_PEMBAYARAN = (
    ('P', 'Paypal'),
    ('S', 'Stripe'),
)

User = get_user_model()

class CulturalOrigin(models.Model):
    nama_asal_budaya = models.CharField(max_length=100)
    code_budaya = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.nama_asal_budaya

class Category(models.Model):
    code_category = models.CharField(max_length=5, unique=True)
    nama_category = models.CharField(max_length=100)
    banner_category = models.ImageField(upload_to='category_banners')
    desc_category = models.TextField()

    def __str__(self):
        return self.nama_category

class ProdukItem(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.FloatField()
    harga_diskon = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product_pics')
    gambar_detail = models.ImageField(upload_to='product_detail', blank=True, null=True)
    main_banner_detail = models.ImageField(upload_to='product_banners', blank=True, null=True)
    label = models.CharField(choices=PILIHAN_LABEL, max_length=4)
    kategori = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    asal_budaya = models.ForeignKey(CulturalOrigin, on_delete=models.SET_NULL, null=True)
    lokasi = models.CharField(max_length=100, default="")
    jumlah_orang = models.TextField(blank=True, null=True)
    max_stok = models.PositiveIntegerField(default=0)
    current_stok = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    banner_history_prod = models.ImageField(upload_to='product_detail_banners', blank=True, null=True)
    desc_history_one = models.TextField(blank=True, null=True)
    desc_history_two = models.TextField(blank=True, null=True)
    desc_history_three = models.TextField(blank=True, null=True)
    is_popular = models.BooleanField(default=False)
    is_recomended = models.BooleanField(default=False)

    # New fields
    
    def __str__(self):
        return f"{self.nama_produk} - ${self.harga}"

    def get_absolute_url(self):
        return reverse("toko:produk-detail", kwargs={
            "slug": self.slug
            })

    def get_add_to_cart_url(self):
        return reverse("toko:add-to-cart", kwargs={
            "slug": self.slug
            })
    
    def get_remove_from_cart_url(self):
        return reverse("toko:remove-from-cart", kwargs={
            "slug": self.slug
            })
    
class OrderProdukItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    produk_item = models.ForeignKey(ProdukItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.produk_item.nama_produk}"

    def get_total_harga_item(self):
        return self.quantity * self.produk_item.harga
    
    def get_total_harga_diskon_item(self):
        return self.quantity * self.produk_item.harga_diskon

    def get_total_hemat_item(self):
        return self.get_total_harga_item() - self.get_total_harga_diskon_item()
    
    def get_total_item_keseluruan(self):
        if self.produk_item.harga_diskon:
            return self.get_total_harga_diskon_item()
        return self.get_total_harga_item()
    
    def get_total_hemat_keseluruhan(self):
        if self.produk_item.harga_diskon:
            return self.get_total_hemat_item()
        return 0


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produk_items = models.ManyToManyField(OrderProdukItem)
    tanggal_mulai = models.DateTimeField(auto_now_add=True)
    tanggal_order = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    alamat_pengiriman = models.ForeignKey('AlamatPengiriman', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

     
    def get_total_harga_order(self):
        total = 0
        for order_produk_item in self.produk_items.all():
            total += order_produk_item.get_total_item_keseluruan()
        return total
    
    def get_total_hemat_order(self):
        total = 0
        for order_produk_item in self.produk_items.all():
            total += order_produk_item.get_total_hemat_keseluruhan()
        return total

class AlamatPengiriman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alamat_1 = models.CharField(max_length=100)
    alamat_2 = models.CharField(max_length=100)
    negara = models.CharField(max_length=100)
    kode_pos = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.alamat_1}"

    class Meta:
        verbose_name_plural = 'AlamatPengiriman'

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_option = models.CharField(choices=PILIHAN_PEMBAYARAN, max_length=1)
    charge_id = models.CharField(max_length=50)

    def __self__(self):
        return self.user.username
    
    def __str__(self):
        return f"{self.user.username} - {self.payment_option} - {self.amount}"
    
    class Meta:
        verbose_name_plural = 'Payment'
        
        
class Contact(models.Model):
    ART_CATEGORIES = (
        ('ST', 'Seni Tari'),
        ('STR', 'Seni Teater'),
        ('SM', 'Seni Musik'),
        ('SR', 'Seni Rupa'),
        # Add other art categories as needed
    )

    name = models.CharField(max_length=100, default="")  # Default value for name field
    email = models.EmailField(default="")  # Default value for email field
    phone = models.CharField(max_length=15, default="+62")  # Default value for phone field
    art_category = models.CharField(choices=ART_CATEGORIES, max_length=20, default='ST')  # Default value for art_category field
    portfolio = models.CharField(max_length=200, default="")  # Default value for portfolio field
    address = models.CharField(max_length=200, default="Alamat default")  # Default value for address field
    experience = models.TextField(default="")  # Default value for experience field


    def __str__(self):
        return self.name