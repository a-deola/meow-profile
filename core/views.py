from django.shortcuts import render
import requests
from datetime import datetime
from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from django.views.decorators.csrf import csrf_exempt
import requests
from datetime import datetime

@csrf_exempt
@ratelimit(key='ip', rate='5/m', block=False)
def profile_data(request):

    if getattr(request, 'limited', False):
        return JsonResponse({
            "status": "error",
            "message": "Rate limit exceeded. Try again later."
        }, status=429)

    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        fact = response.json().get("fact", "Cats are awesome!")
    except Exception:
        fact = "Could not fetch a cat fact at this time."

    data = {
        "status": "success",
        "user": {
            "email": "meetprecious1403@gmail.com",
            "name": "Adeola Samuel",
            "stack": "Python/Django"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fact": fact
    }
    return JsonResponse(data)

