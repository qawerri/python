from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_at', 'created_date']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_true', 'make_auction_false']

    @admin.action(description='Перевести auction в True')
    def make_auction_true(self, request, query):
        query.update(auction=True)

    @admin.action(description='Перевести auction в False')
    def make_auction_false(self, request, query):
        query.update(auction=False)

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

admin.site.register(Advertisement, AdvertisementAdmin)