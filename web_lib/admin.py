from django.contrib import admin
from django.utils.html import format_html
from web_lib.models import Author, Book, Product, Store, ExtUser


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age','email', 'info']

    def info(self, obj):
        return format_html("<br>".join(obj.info()))
    info.short_description = "Информация об авторе"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','description','page_num']

@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ['desc','is_logged']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

