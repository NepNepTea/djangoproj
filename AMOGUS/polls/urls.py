from django.urls import path
from . import views
from .views import ChangeUserInfoView
from .views import BBPasswordChangeView
from .views import RegisterDoneView, RegisterUserView

app_name = 'polls'
urlpatterns = [
    path('', views.main, name='main'),
    path('quest/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('accounts/login/', views.BBLoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/logout/', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', views.BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
]