import os
from django.utils.text import slugify


def product_images(instance, filename):
    summary = instance.image_summary
    product_name = summary.split(" ")[0]
    path = os.path.join(
        "Product_Image",
        product_name,
        slugify(summary),
        filename,
    )
    return path
