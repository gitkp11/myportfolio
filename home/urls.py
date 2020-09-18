from django.urls import path

from .views import HomePageView, SingleBlogView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blogsingle/', SingleBlogView.as_view(), name='blogsingle'),
    
]
