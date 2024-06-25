from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("name", "email", "message")
    ordering = ("-timestamp",)
    readonly_fields = ("name", "email", "message", "timestamp")

    fieldsets = (
        (None, {"fields": ("name", "email", "message")}),
        (
            "Дата и время",
            {
                "fields": ("timestamp",),
                "classes": ("collapse",),
            },
        ),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
