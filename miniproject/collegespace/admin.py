from django.contrib import admin
from .models import Posts, ImagePost, Friends, Profile, TextPost, Comments

# Register your models here.
admin.site.register(Posts)
admin.site.register(ImagePost)
admin.site.register(Friends)
admin.site.register(Profile)
admin.site.register(TextPost)
admin.site.register(Comments)


