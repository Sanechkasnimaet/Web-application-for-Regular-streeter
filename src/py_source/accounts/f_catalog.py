from accounts.models import Product
import json
from django.http import JsonResponse

def products(request):

    # ��������� ���� ������� �� ���� ������
    products = Product.objects.all()

    # ������������ ������ ������� � ���� ��������
    product_data = [
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "image_url": product.image_url
            # �������� ������ ���� �� �������������
        }
        for product in products
    ]

    # ������� JSON-������
    return JsonResponse({"products": product_data})
