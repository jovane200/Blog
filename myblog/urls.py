from django.urls import path


from . import views

app_name = 'myblog'

app_name = 'myblog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('posts/<int:id>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('tags/', views.tag_list, name='tag_list'),
    path('search/', views.post_search, name='post_search'),
]
