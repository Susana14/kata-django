from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "created_date"]
	list_filter= ["created_date"]
	search_fields = ["title", "text"]

admin.site.register(Post,PostAdmin)


# Register your models here.
