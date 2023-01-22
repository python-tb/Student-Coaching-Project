from django.urls import path
from student_app import views

urlpatterns = [
    path('',views.index,name='home' ),

    # Student URL Section:-

    path('show_students',views.show_students,name='show_students'),
    path('add_student',views.add_student,name='add_student'),
    path('update_student/<int:id>',views.update_student,name='update_student'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),

    # Teacher URL Section:-

    path('show_teachers',views.show_teachers,name='show_teachers'),
    path('add_teacher',views.add_teacher,name='add_teacher'),
    path('update_teacher/<int:id>',views.update_teacher,name='update_teacher'),
    path('delete_teacher/<int:id>',views.delete_teacher,name='delete_teacher'),


#   Course URL Section:-

    path('show_courses',views.show_courses,name='show_courses'),
    path('add_course',views.add_course,name='add_course'),
    path('update_course/<int:id>',views.update_course,name='update_course'),
    path('delete_course/<int:id>',views.delete_course,name='delete_course'),

# Login,Logout and Signup  URL Section :-

    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
]




#  -------------------Developed By :- NARESH KUMAR AGRAWAL ----------------------