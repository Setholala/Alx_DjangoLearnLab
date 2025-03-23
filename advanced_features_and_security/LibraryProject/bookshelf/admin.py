from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from yourapp.models import Article

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("author")

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

content_type = ContentType.objects.get_for_model(Article)

permissions = [
    "can_view",
    "can_create",
    "can_edit",
    "can_delete"
]

for codename in permissions:
    perm, created = Permission.objects.get_or_create(codename=codename, content_type=content_type)

    if codename in ["can_view"]:
        group, _ = Group.objects.get_or_create(name="Viewers")
        group.permissions.add(perm)

    if codename in ["can_create", "can_edit"]:
        group, _ = Group.objects.get_or_create(name="Editors")
        group.permissions.add(perm)

    if codename in ["can_view", "can_create", "can_edit", "can_delete"]:
        group, _ = Group.objects.get_or_create(name="Admins")
        group.permissions.add(perm)

# Register your models here.
admin.site.register(Book)
admin.site.register(CustomUser, CustomUserAdmin)
