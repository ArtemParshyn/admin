from django.contrib import admin

from api.models import Courier, Mail, ApiUser

# Register your models here.

admin.site.register(Courier)
admin.site.register(ApiUser)


class MailAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer')  # Поля для отображения в списке
    list_filter = ('user',)  # Фильтрация по пользователю
    search_fields = ('question', 'answer')  # Поля для поиска
    ordering = ('user',)  # Поля для сортировки


admin.site.register(Mail, MailAdmin)
