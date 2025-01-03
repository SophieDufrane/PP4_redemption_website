from django.contrib import admin
from .models import Reward

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):

    list_display = ('reward_name', 'points_cost', 'stock_quantity')
    search_fields = ('reward_name',)  # A search bar for names
    list_filter = ('points_cost',)  # Filter by points cost

# Register your models here.