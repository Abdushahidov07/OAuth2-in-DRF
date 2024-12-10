from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cars
from .serializers import CarsSerializer

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [IsAuthenticated]


from django.http import JsonResponse
import requests

def github_callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)

    token_url = 'https://github.com/login/oauth/access_token'
    payload = {
        'client_id': 'Ov23likRD6uson2BCAHq',
        'client_secret': '024fe8a603ac9b02ef5dc816e9fc6ab53225cdc4',
        'code': code,
        'redirect_uri': 'http://localhost:8000/oauth/callback/',
    }
    headers = {'Accept': 'application/json'}

    response = requests.post(token_url, data=payload, headers=headers)
    token_data = response.json()
    return JsonResponse(token_data)
