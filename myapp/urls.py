from django.urls import path
from. import views

#internal routing
urlpatterns = [
    path('register',views.register,name='register'),
    path('save',views.save,name='save'),
    path('login',views.login,name='login'),
    path('logincheck',views.logincheck,name='logincheck'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('students',views.students,name='students'),
    path('edit',views.edit,name='edit'),
    path('update',views.update,name='update'),
    path('contact',views.contact,name='contact'),
    path('send',views.send,name='send'),
    path('upload',views.upload,name='upload')
]