import uuid, os, json
from bson import ObjectId
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import redirect, render
from myAdmin.views.decorators import session_login_required
from product.models import ProductTable
from product.serializers import ProductSerializer
@session_login_required
def addProduct(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        # Save the image with UUID
        ext = image.name.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        file_path = os.path.join('media', filename)
        saved_path = default_storage.save(file_path, ContentFile(image.read()))
        image_url = default_storage.url(saved_path)

        # Price data
        price_titles = request.POST.getlist('price_title[]')
        price_values = request.POST.getlist('price_value[]')

        price_json = []
        for i in range(len(price_titles)):
            price_json.append({
                "title": price_titles[i],
                "price": float(price_values[i])
            })

        print({
            "title": title,
            "image": image_url,
            "price_json": price_json
        })
        serializer = ProductSerializer(data={
            "title": title,
            "image": image_url,
            "price_json": price_json
        })
        if serializer.is_valid():
            serializer.save()
            return redirect('allproducts')
        # You can save this to MongoDB or wherever
        return redirect('allproducts')  # Or render success page

    return render(request, 'addProduct.html')
@session_login_required
def allProducts(request):
  # Replace with your model
    products = ProductTable.objects.all().order_by('-id')  # MongoEngine query
    return render(request, 'allproducts.html', {'products': products})
@session_login_required
def deleteProduct(request, id):
    banner = ProductTable.objects.get(id=ObjectId(str(id)))
    
    # You can also remove the file from media storage here if needed
    banner.delete()
    return redirect('allproducts')

@session_login_required
def editProduct(request, id):
    product = ProductTable.objects.get(id=ObjectId(str(id)))

    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        # If new image is uploaded, save it
        if image:
            ext = image.name.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            file_path = os.path.join('media', filename)
            saved_path = default_storage.save(file_path, ContentFile(image.read()))
            image_url = default_storage.url(saved_path)
        else:
            image_url = product.image  # Keep existing

        price_titles = request.POST.getlist('price_title[]')
        price_values = request.POST.getlist('price_value[]')
        price_json = []
        for i in range(len(price_titles)):
            price_json.append({
                "title": price_titles[i],
                "price": float(price_values[i])
            })

        product.title = title
        product.image = image_url
        product.price_json = price_json
        product.save()

        return redirect('allproducts')

    return render(request, 'addProduct.html', {'product': product})
