from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='blog'),
    path('blog/post/<int:id>/', views.post, name='post'),
    path('blog/category/<int:id>', views.category, name="category"),
    path('blog/search', views.search, name='search'),
    path('blog/create/', views.create, name='create'),
    path('login/', LoginView.as_view(), name='blog_login'),
    path('logout/', LogoutView.as_view(), name='blog_logout'),

    path('form/', views.form),
    path('form/show', views.show),
    path('access/', views.access),
    path('access/loggedIn', views.loggedIn),
    path('Django/', views.index),
    path('Python/', views.index),
    path('Other/', views.index),


]

