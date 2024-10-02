from django.contrib import admin
from .models import Post
# if we want to see a model data on admin url then
# we have to register our model here
admin.site.register(Post)