from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('prices/', views.PricesView.as_view(), name='prices'),
    path('topic_info/<int:topic_id>/', views.TopicInfoView.as_view(), name='Topic_info'),
    path('post/<int:post_id>/<slug:post_slug>/', views.PostView.as_view(), name='post'),
]