from django.urls import path

from . import views
from .views import SignUpView

app_name = 'polls'
urlpatterns = [
    path('quest/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path("signup/", SignUpView.as_view(), name="signup"),
]