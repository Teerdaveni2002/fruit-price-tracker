from django.urls import path
from .views import FruitListView, search_fruit

app_name = 'tracker'

urlpatterns = [
    path('', FruitListView.as_view(), name='index'),
    path('search/<int:fruit_id>/', search_fruit, name='search_fruit'),
]
