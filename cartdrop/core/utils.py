import os


def category_images(instance, filename):
    path = os.path.join("Category Media", instance.category.slug, filename)
    return path


def subcategory_images(instance, filename):
    path = os.path.join(
        "Subcategory Media", instance.category.slug, instance.slug, filename
    )
    return path


def product_images(instance, filename):
    path = os.path.join(
        "Product Image", instance.product.category.slug, instance.product.slug, filename
    )
    return path


def brand_photo_location(instance, filename):
    path = os.path.join("Brand images", instance.slug, filename)
    return path


def review_image_location(instance, filename):
    path = os.path.join(
        "Reviews Images", instance.review.user.username, instance.product.slug, filename
    )
    return path
