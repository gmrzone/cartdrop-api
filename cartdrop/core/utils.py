import os

def category_images(instance, filename):
    path = os.path.join('Category Media', instance.slug, filename)
    return path

def subcategory_images(instance, filename):
    path = os.path.join('Subcategory Media', instance.category.slug ,instance.slug, filename)
    return path
