from django.urls import path
from . import views



urlpatterns = [ 
    path('login/', views.loginPage,name="login"),
    path('register/',views.registerUser,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('hr/',views.hrpage,name="hr"),
    path('employee/<str:pk_test>/',views.employee,name="employee"),
    path('createjob/',views.createjob,name="createjobpost"),
    path('updatejob/<str:pk>/',views.updatejob,name="updatejobpost"),
    path('deletejob/<str:pk>/',views.deletejob,name="deletejobpost"),
   
 
]