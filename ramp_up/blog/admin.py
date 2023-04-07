from django.contrib import admin

from ramp_up.blog.models import Blog, Author

admin.site.register(Blog)
admin.site.register(Author)