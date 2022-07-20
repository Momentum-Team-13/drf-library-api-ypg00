from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Book, TrackedBook, Note

admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(TrackedBook)
admin.site.register(Note)
