import os


def product_images(instance, filename):
    path = os.path.join(
        "Product Image",
        instance.product.subcategory.slug,
        instance.product.slug,
        filename,
    )
    return path
