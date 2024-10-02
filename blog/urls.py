from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    CreateDetailPost,
                    DeletePost,
                    UpdateDetailPost)
from . import views

urlpatterns = [
    # path('',  views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('new',CreateDetailPost.as_view(), name='create-post'),
    path('<int:pk>/update',UpdateDetailPost.as_view(), name='update-post'),
    path('<int:pk>/delete', DeletePost.as_view(), name="delete-post"),
]


# by default CBV looking for a template at the address
# <app>/<model>_<viewtype>.html