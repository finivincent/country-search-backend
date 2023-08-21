from django.http import JsonResponse
from .models import Country


def search_countries(request):
    query = request.GET.get("query", "").lower()
    matching_countries = Country.objects.filter(name__icontains=query)
    country_names = [country.name for country in matching_countries]

    return JsonResponse(country_names, safe=False)



