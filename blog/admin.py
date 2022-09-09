from django.contrib import admin
from blog.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','update','timestamp','price','currency','make_response','response','url_instruction')
    list_display_links = ('update','url_instruction')
    list_editable = ('title',)
    list_filter = ('update','timestamp','price')





admin.site.register(Post, PostModelAdmin)
