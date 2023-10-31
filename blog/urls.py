from django.urls import path, include
from . views import Index, DetailArticleView, CreateBlog, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('new_blog/', CreateBlog.as_view(), name='new'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>', DetailArticleView.as_view(), name='detail_article'),
    path('post/edit/<int:pk>', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
]