from django.contrib import admin
from .models import Fruit, SearchHistory


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'current_price', 'search_count', 'updated_at']
    list_filter = ['search_count', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['fruit', 'price_at_search', 'search_timestamp']
    list_filter = ['fruit', 'search_timestamp']
    readonly_fields = ['search_timestamp']
