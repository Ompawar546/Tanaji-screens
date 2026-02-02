from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Product, ProductCategory
from .forms import ProductForm, ProductCategoryForm



# ===================== PUBLIC STATIC PAGES =====================

from .models import Product

def home(request):
    products = Product.objects.order_by('-id')[:4]  # latest 4 products
    return render(request, 'website/home.html', {
        'products': products
    })


from django.shortcuts import render

def services(request):
    return render(request, 'website/services.html')




def contact(request):
    return render(request, 'website/contact.html')


def about(request):
    return render(request, 'website/about.html')


# ===================== CAREER =====================

def career(request):
    if request.method == "POST":
        data = request.POST

        message = f"""
Name: {data['name']}
Position: {data['role']}
Expected Salary: {data['expected_salary']}
Email: {data['email']}
Contact: {data['contact']}
Age: {data['age']}
Qualification: {data['qualification']}

Experience:
{data['experience']}
"""

        send_mail(
            subject="New Career Application",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["tanaji.screens@gmail.com"],
        )

        return render(request, "website/career.html", {"success": True})

    return render(request, "website/career.html")


# ===================== PRODUCTS (PUBLIC) =====================

def products(request):
    products = Product.objects.select_related("category").all()
    categories = ProductCategory.objects.all()

    return render(
        request,
        "website/products.html",
        {
            "products": products,
            "categories": categories
        }
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "website/product_detail.html", {"product": product})


def products_by_category(request, category_slug):
    category = get_object_or_404(ProductCategory, slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(
        request,
        "website/products.html",
        {
            "products": products,
            "selected_category": category,
        }
    )


# ===================== ADMIN AUTH =====================

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            return redirect("admin_dashboard")

        return render(
            request,
            "website/admin_login.html",
            {"error": "Invalid admin credentials"}
        )

    return render(request, "website/admin_login.html")


@login_required
def admin_logout(request):
    logout(request)
    return redirect("admin_login")


# ===================== ADMIN PANEL =====================

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, "website/admin_dashboard.html")


@login_required
@user_passes_test(lambda u: u.is_staff)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(
                request,
                "website/add_product.html",
                {
                    "form": ProductForm(),
                    "success": True
                }
            )
    else:
        form = ProductForm()

    return render(
        request,
        "website/add_product.html",
        {"form": form}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def add_category(request):
    if request.method == "POST":
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "website/add_category.html",
                {
                    "form": ProductCategoryForm(),
                    "success": True
                }
            )
    else:
        form = ProductCategoryForm()

    return render(
        request,
        "website/add_category.html",
        {"form": form}
    )



@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    products = Product.objects.select_related("category").all()

    return render(
        request,
        "website/admin_products.html",
        {
            "products": products
        }
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("admin_products")
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "website/edit_product.html",
        {
            "form": form,
            "product": product
        }
    )



@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.delete()
        return redirect("admin_products")

    return render(
        request,
        "website/delete_product.html",
        {"product": product}
    )
