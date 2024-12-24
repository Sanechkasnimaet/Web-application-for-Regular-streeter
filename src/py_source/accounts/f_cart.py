from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# ��������� ������ � ���������
product_data = []

@csrf_exempt
def cart(request, product_id=None):
    if request.method == "DELETE" and product_id is not None:
        product_to_delete = next((p for p in product_data if p["id"] == product_id), None)
        if product_to_delete:
            product_data.remove(product_to_delete)
            return JsonResponse({"message": f"ID {product_id} "}, status=200)
        else:
            return JsonResponse({"error": " "}, status=404)

    elif request.method == "POST":
        try:
            # ���������� JSON �� ���� �������
            data = json.loads(request.body)
            product = data.get("product")  # �������� ������ 'product' �� �������
            
            if not product:
                return JsonResponse({"error": "No product provided"}, status=400)
            
            # ��������� ������� � ������
            product_data.append(product)
            print(f"Add: {product}")  # �������� ������� �� �������
            
            return JsonResponse({"products": product_data})  # ���������� ����������� ������ ���������
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    # ���� ����� GET, ���������� ������� ������ ���������
    return JsonResponse({"products": product_data})
