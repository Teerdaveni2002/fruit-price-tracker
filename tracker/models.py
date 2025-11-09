from django.db import models


class Fruit(models.Model):
    """Model to represent a fruit with its pricing information"""
    name = models.CharField(max_length=100, unique=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    search_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - ₹{self.current_price}"
    
    def increment_price(self):
        """Increment price by 2 rs if search count is less than 5"""
        if self.search_count < 5:
            self.current_price += 2
            self.search_count += 1
            self.save()
            return True
        return False


class SearchHistory(models.Model):
    """Model to track search history"""
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE, related_name='searches')
    price_at_search = models.DecimalField(max_digits=10, decimal_places=2)
    search_timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-search_timestamp']
        verbose_name_plural = "Search histories"
    
    def __str__(self):
        return f"{self.fruit.name} searched at ₹{self.price_at_search} on {self.search_timestamp}"
