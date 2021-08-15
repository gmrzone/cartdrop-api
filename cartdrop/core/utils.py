import os


def category_images(instance, filename):
    path = os.path.join("Category Media", instance.category.slug, filename)
    return path


def subcategory_images(instance, filename):
    path = os.path.join(
        "Subcategory Media",
        instance.subcategory.category.slug,
        instance.subcategory.slug,
        filename,
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
