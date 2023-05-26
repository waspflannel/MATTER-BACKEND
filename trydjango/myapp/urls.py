
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.views.generic import TemplateView;
from .views import GetUsersView , GetImageInfoView , GetUserProfile , getImageInfo , loginView , registerView , image_upload_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns =[
    #path('register/', views.register, name='register'),
    #path('login/', views.loginPage, name='login'),
    path('upload/', image_upload_view.as_view(),name = 'upload'),
   # path('profile/<str:pk>/', views.profile, name='profile'),
    
    path('', views.homePage, name='base'),
    path('profile/', views.homePage, name='base'),



    path('signup/', loginView.as_view(), name='login'),
    path('register/', registerView.as_view(), name='register'),

    path('api/profileData',GetUsersView.as_view()),
    path('api/imageData', GetImageInfoView.as_view()),

    path('api/user', GetUserProfile.as_view()),
    path('api/images', getImageInfo.as_view()),


    #path('api/csrf', GetCSRFToken.as_view()),
    #path('profile/<str:pk>/', views.profileTest, name='profileTest')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)