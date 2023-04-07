from django.contrib import admin

from blog.models import Blog, Author

admin.site.register(Blog)
admin.site.register(Author)