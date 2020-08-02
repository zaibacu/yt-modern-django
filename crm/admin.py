from django.contrib import admin
from .models import Customer, Category, Event

admin.site.register(Customer)
admin.site.register(Category)


class EventAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj) + ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)
