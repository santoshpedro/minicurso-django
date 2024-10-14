from django.contrib import admin
from .models import Post

# Registrando o modelo Post no admin
admin.site.register(Post)