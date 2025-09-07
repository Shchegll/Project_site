from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Profile, Profile_address

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'surname', 'phone', 'document_type', 'id_document', 'inn', 'get_document_photo']
    list_filter = ['document_type', 'type_of_purchase', 'can_edit']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'surname', 'phone', 'inn']
    readonly_fields = ['get_document_photo_preview']
    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'surname', 'phone', 'birth_date')
        }),
        ('Документы', {
            'fields': ('document_type', 'id_document', 'date_of_issue', 'inn', 'document_photo', 'get_document_photo_preview')
        }),
        ('Информация о покупке', {
            'fields': ('type_of_purchase', 'price', 'price_in_queue')
        }),
        ('Партнерская информация', {
            'fields': ('parther_name', 'parther_phone', 'id_coor')
        }),
        ('Настройки', {
            'fields': ('can_edit', 'agree_to_terms')
        }),
    )
    
    def get_document_photo(self, obj):
        if obj.document_photo:
            return "Есть фото"
        return "Нет фото"
    get_document_photo.short_description = 'Фото документа'
    
    def get_document_photo_preview(self, obj):
        if obj.document_photo:
            return mark_safe(f'<img src="{obj.document_photo.url}" width="350" />')
        return "Нет изображения"
    get_document_photo_preview.short_description = 'Предпросмотр фото'

@admin.register(Profile_address)
class ProfileAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'reg_country', 'reg_city', 'reg_address', 'is_approved']
    list_filter = ['reg_country', 'is_approved']
    search_fields = ['user__email', 'reg_city', 'reg_address']
    fieldsets = (
        ('Адрес регистрации', {
            'fields': (
                'reg_country', 'reg_region', 'reg_city', 
                'reg_address', 'reg_street', 'reg_house',
                'reg_apartament', 'reg_postal_code'
            )
        }),
        ('Адрес проживания', {
            'fields': (
                'act_country', 'act_region', 'act_city', 
                'act_address', 'act_street', 'act_house',
                'act_apartament', 'act_postal_code', 'is_approved'
            )
        }),
    )