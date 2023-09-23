from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Category, Product

# from django.shortcuts import render
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# import numpy as np
# from PIL import Image as PILImage
# import tensorflow as tf
# from .models import ProductImage


def product_all(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(regular_price__icontains=q))
        products = Product.objects.prefetch_related("product_image").filter(multiple_q, is_active=True)
    else:
        products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "store/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "store/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/single.html", {"product": product})



# def search_by_image(request):
#     if request.method == 'POST':
#         # Get the uploaded image
#         image_file = request.FILES['image']
        
#         # Save the image to the storage
#         filename = default_storage.save('temp.jpg', ContentFile(image_file.read()))

#         # Open the image and resize it to the input size of the model
#         img = PILImage.open(default_storage.path(filename))
#         img = img.resize((224, 224))

#         # Convert the image to a numpy array
#         img_array = np.array(img)

#         # Load the machine learning model
#         model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False, pooling='avg')

#         # Get the features of the image
#         features = model.predict(np.expand_dims(img_array, axis=0))[0]

#         # Get all images in the database
#         images = ProductImage.objects.all()

#         # Calculate the similarity of each image to the uploaded image
#         similarity = {}
#         for image in images:
#             image_features = np.load(image.features.path)
#             distance = np.linalg.norm(features - image_features)
#             similarity[image.id] = distance

#         # Sort the images by similarity
#         sorted_images = sorted(similarity.items(), key=lambda x: x[1])

#         # Get the top 10 most similar images
#         top_images = [Image.objects.get(id=image[0]) for image in sorted_images[:10]]

#         return render(request, 'search_results.html', {'images': top_images})

#     return render(request, 'base.html')

# def search(request):
#     products = Product.objects.all()
#     return (request. '/store/search_results.html'products:'products')
