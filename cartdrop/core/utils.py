import os


def category_images(instance, filename):
    path = os.path.join("Category_Media", instance.category.slug, filename)
    return path


def subcategory_images(instance, filename):
    path = os.path.join(
        "Subcategory_Media",
        instance.subcategory.category.slug,
        instance.subcategory.slug,
        filename,
    )
    return path


def brand_photo_location(instance, filename):
    path = os.path.join("Brand_images", instance.slug, filename)
    return path


def review_image_location(instance, filename):
    path = os.path.join(
        "Reviews_Images", instance.review.user.username, instance.product.slug, filename
    )
    return path


def category_images_placeholder(instance, filename):
    path = os.path.join(
        "Placeholders", "Category_Media", instance.category.slug, filename
    )
    return path


def subcategory_images_placeholder(instance, filename):
    path = os.path.join(
        "Placeholders",
        "Subcategory_Media",
        instance.subcategory.category.slug,
        instance.subcategory.slug,
        filename,
    )
    return path


def brand_photo_placeholder_location(instance, filename):
    path = os.path.join("Placeholders", "Brand_images", instance.slug, filename)
    return path


def review_image_placeholder_location(instance, filename):
    path = os.path.join(
        "Placeholders",
        "Reviews_Images",
        instance.review.user.username,
        instance.product.slug,
        filename,
    )
    return path
