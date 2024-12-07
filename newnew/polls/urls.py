from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('register', views.register_page, name = 'register'),
    path('createquestion', views.create_question_view, name = 'createquestion'),
    path('addavatar', views.add_avatar, name = 'addavatar'),
    path('profile', views.profile_view, name = 'profile'),
    path('<int:pk>/addvariants', views.add_variant, name='addvariants'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)