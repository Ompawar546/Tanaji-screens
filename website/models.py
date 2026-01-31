from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="products"
    )
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
