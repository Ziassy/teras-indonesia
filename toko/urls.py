from django.urls import path
from django.conf import settings
from django.urls import path, include
from django.views.static import serve
from . import views

app_name = 'toko'

urlpatterns = [
     path('', views.HomeListView.as_view(), name='home-produk-list'),
     path('carousel/', views.ProductList.as_view(), name='produk-list'),
     path('product/<slug>/', views.ProductDetailView.as_view(), name='produk-detail'),
     path('contact', views.ContactPageView.as_view(), name='contact'),
     path('contact/success/', views.contact_success, name='contact_success'),
     path('about/', views.about_view, name='about'),
     path('checkout/', views.CheckoutView.as_view(), name='checkout'),
     path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
     path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
     path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
     path('empty-order-summary/', views.empty_view_order_summary, name='empty-order-summary'),
     path('payment/<payment_method>', views.PaymentView.as_view(), name='payment'),
     path('paypal-return/', views.paypal_return, name='paypal-return'),
     path('paypal-cancel/', views.paypal_cancel, name='paypal-cancel'),
]

if settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]