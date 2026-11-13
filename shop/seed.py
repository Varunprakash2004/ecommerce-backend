import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from shop.models import Category, Product


# Create categories
casual, _ = Category.objects.get_or_create(
    name="Casual",
    slug="casual"
)

formal, _ = Category.objects.get_or_create(
    name="Formal",
    slug="formal"
)


products = [
    {
        "name": "T-shirt with Tape Details",
        "brand": "ZARA",
        "price": 120,
        "original_price": 150,
        "rating": 4.5,
        "review_count": 120,
        "description": "A premium quality t-shirt featuring unique tape detail accents.",
        "is_new": True,
        "discount": 20,
        "category": casual,
    },

    {
        "name": "Courage Graphic T-shirt",
        "brand": "ZARA",
        "price": 150,
        "original_price": 180,
        "rating": 4.0,
        "review_count": 80,
        "description": "Graphic printed casual t-shirt.",
        "is_new": True,
        "discount": 15,
        "category": casual,
    },

    {
        "name": "Skinny Fit Jeans",
        "brand": "LEVIS",
        "price": 200,
        "original_price": 250,
        "rating": 4.6,
        "review_count": 90,
        "description": "Comfortable slim fit denim jeans.",
        "is_new": False,
        "discount": 20,
        "category": casual,
    },

    {
        "name": "Formal Shirt",
        "brand": "ZARA",
        "price": 180,
        "original_price": 220,
        "rating": 4.3,
        "review_count": 70,
        "description": "Classic formal shirt.",
        "is_new": False,
        "discount": 10,
        "category": formal,
    }
]


for item in products:
    Product.objects.get_or_create(
        name=item["name"],
        defaults=item
    )


print("Products created successfully")