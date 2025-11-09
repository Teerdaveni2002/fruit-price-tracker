from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Fruit, SearchHistory


class FruitListView(ListView):
    """Class-based view to display list of fruits"""
    model = Fruit
    template_name = 'tracker/index.html'
    context_object_name = 'fruits'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_history'] = SearchHistory.objects.all()[:10]
        return context


@csrf_exempt
@require_http_methods(["POST"])
def search_fruit(request, fruit_id):
    """AJAX endpoint to search for a fruit and increment its price"""
    fruit = get_object_or_404(Fruit, id=fruit_id)
    
    # Record search history with current price
    SearchHistory.objects.create(
        fruit=fruit,
        price_at_search=fruit.current_price
    )
    
    # Increment price if search count is less than 5
    price_incremented = fruit.increment_price()
    
    return JsonResponse({
        'success': True,
        'fruit_name': fruit.name,
        'new_price': float(fruit.current_price),
        'search_count': fruit.search_count,
        'price_incremented': price_incremented,
        'message': f'Price updated! Search count: {fruit.search_count}/5' if price_incremented else 'Max searches reached. Price will not increase further.'
    })
