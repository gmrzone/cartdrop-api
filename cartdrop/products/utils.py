import os


def product_images(instance, filename):
    path = os.path.join(
        "Product Image",
        instance.image_summary,
        filename,
    )
    return path
