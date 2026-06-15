from django.urls import path
from . import views
urlpatterns=[
    path('',views.student_list),
    path('add/',views.add_student),
    path('edit/<int:id>/',views.edit_student),
    path('delete/<int:id>/',views.delete_student),
    path('detail/<int:id>/',views.student_detail),
    path('search/',views.student_search), 
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('logout/', views.logout_user),

]