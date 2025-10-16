from django.shortcuts import render

import requests
from datetime import datetime
from django.http import JsonResponse

def profile_data(request):
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

