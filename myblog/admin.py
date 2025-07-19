from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Post, Comment
from taggit.models import Tag

class MyAdminSite(AdminSite):
    site_header = "My Blog Admin"
    site_title = "My Blog Admin Portal"
    index_title = "Welcome to My Blog Admin"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_admin_css'] = True
        return context

admin_site = MyAdminSite(name='myadmin')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'body')

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']

# Register models
admin_site.register(Post, PostAdmin)
admin_site.register(Comment, CommentAdmin)
admin_site.register(Tag,TagAdmin)