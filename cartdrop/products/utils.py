import os


def product_images(instance, filename):
    summary = instance.image_summary
    product_name = summary.split(" ")[0]
    path = os.path.join(
        "Product Image",
        product_name,
        summary,
        filename,
    )
    return path
