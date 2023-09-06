from . import views
from django.urls import path
from .views import (
    PostCreateView,
    profile_view
    )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post_profile/', profile_view, name='post_profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('newsletter/', views.NewsLetter, name='NewsLetter'),
    path('validate/', views.validate_email, name='validate_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
