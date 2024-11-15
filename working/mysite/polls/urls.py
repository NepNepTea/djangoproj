from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import SignUpView, testing
from .views import add_post_view


app_name = 'polls'
urlpatterns = [
    path('quest/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('newpost/', add_post_view, name="newpost"),
    path('test/', testing, name="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

