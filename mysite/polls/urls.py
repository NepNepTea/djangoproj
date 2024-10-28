from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.main, name='main'),
    path('quest/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('account/login', views.BBLoginView.as_view(), name='login'),
    path('account/profile/', views.profile, name='profile'),
]