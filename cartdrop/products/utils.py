import os


def product_images(instance, filename):
    path = os.path.join(
        "Product Image", instance.product.category.slug, instance.product.slug, filename
    )
    return path