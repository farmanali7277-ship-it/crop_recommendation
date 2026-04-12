from django.contrib import admin
from .models import UserProfile, Prediction


# UserProfile Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')


# Prediction Admin
@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'predicted_label',
        'N', 'P', 'K',
        'temperature',
        'humidity',
        'ph',
        'rainfall',
        'created_at'
    )
    list_filter = ('predicted_label', 'created_at')
    search_fields = ('user__username', 'predicted_label')