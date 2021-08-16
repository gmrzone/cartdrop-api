import os


def product_images(instance, filename):
    path = os.path.join(
        "Product Image",
        instance.product_variation.product.slug,
        instance.product_variation.color.name,
        filename,
    )
    return path
