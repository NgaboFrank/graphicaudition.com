from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path("admin/", admin.site.urls),

    # Main website
    path("", views.home, name="home"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Pesapal payments
    path("payment/", views.payment, name="payment"),
    path("payment/start/", views.start_payment, name="start_payment"),
    path("payment/callback/", views.payment_callback, name="payment_callback"),
    path("payment/cancelled/", views.payment_cancelled, name="payment_cancelled"),
    path("payment/ipn/", views.pesapal_ipn, name="pesapal_ipn"),
]
