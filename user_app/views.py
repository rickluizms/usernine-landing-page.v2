from django.shortcuts import render

import requests

def home(request):
    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'phone': request.POST.get('phone'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),     
                   
        }

        message = {
            'subject': request.POST.get('subject'),
            'message': request.POST.get('message'),     
        }

        # Enviar para API Gateway
        response = requests.post('http://localhost:8080/consumer/', json=data)

        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            return render(request, 'index.html', {'status': 1})
        else:
            return render(request, 'index.html', {'status': 0})

    return render(request, 'index.html', {'status': -1})

def portfolio(request):
    return render(request, 'portfolio-details.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def inner_page(request):
    return render(request, 'inner-page.html')