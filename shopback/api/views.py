from django.http import JsonResponse




products=[{
        'id':i,
        'name': f'product{i}',
        'price': i*1000
    }for i in range (1,5)
]
categories=[{
    'id':j,
    'name':f'category{j}'
}for j in range (1.5)]


def product_list(request):
    return JsonResponse(products, safe=False)

def product_detail(request, product_id):
    for product in products:
        if product['id']==product_id:
             return JsonResponse(product)
    return JsonResponse({'error':'product does not exist'})

def category_list(request):
    return JsonResponse(categories, safe=False)

def category_detail(request, category_id):
    for category in categories:
        if category['id']==category_id:
             return JsonResponse(category)
    return JsonResponse({'error':'category does not exist'})

def category_products(request, category_id):
    for category in categories:
        if category['id']==category_id:
             return JsonResponse(category)
    return JsonResponse({'error':'product does not exist'})
