from django.urls import path
from.import views
#from .views import download


urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # App pages
    path('', views.index, name='index'),
    path('s1/', views.s1, name='s1'),
    path('s2/', views.s2, name='s2'),
    path('s3/', views.s3, name='s3'),
    path('s4/', views.s4, name='s4'),
    path('s5/', views.s5, name='s5'),
    path('s6/', views.s6, name='s6'),
    path('base/', views.base, name='base'),
    #path('pdfs/',views.pdfs, name='pdfs'),
]
