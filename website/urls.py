from django.urls import path
from . import views

urlpatterns = [
    # ================= PUBLIC PAGES =================
    path('', views.home, name='home'),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("career/", views.career, name="career"),
    path('services/', views.services, name='services'),

    # ================= PRODUCTS (PUBLIC) =================
    path("products/", views.products, name="products"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path(
        "products/category/<slug:category_slug>/",
        views.products_by_category,
        name="products_by_category"
    ),

    # ================= ADMIN AUTH =================
    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),

    # ================= ADMIN PANEL =================
    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-panel/add-product/", views.add_product, name="add_product"),
    path("admin-panel/add-category/", views.add_category, name="add_category"),
    path("admin-panel/products/", views.admin_products, name="admin_products"),
    path(
        "admin-panel/products/edit/<int:product_id>/",
        views.edit_product,
        name="edit_product"
    ),
    path(
        "admin-panel/products/delete/<int:product_id>/",
        views.delete_product,
        name="delete_product"
    ),



]
