import main.views
from . import views
from django.urls import path

# import activity.views







#Functions
urlpatterns = [
    path('other-settings', views.other_settings, name='other-settings'),

    path('dashboard/create-lecture' , views.create_lecture , name="create-lecture"),
    path('dashboard/add-video' , views.add_video, name="add-video"),
    path('dashboard/add-part' , views.add_part, name="add-part"),

    path('dashboard/lecture-settings' , views.lecture_settings, name="lecture-settings"),
    path('dashboard/part-settings' , views.part_settings, name="part-settings"),
    path('dashboard/delete-lecture' , views.lecture_delete, name="lecture-delete"),
    path('dashboard/delete-part' , views.part_delete, name="part-delete"),

    path('dashboard/remove-student-from-lecture' , views.remove_student, name="remove-student-from-lecture"),
    path('dashboard/add-student-to-lecture' , views.add_student, name="add-student-to-lecture"),
    path('dashboard/add-part-to-lecture' , views.add_part_to_lecture, name="add-part-to-lecture"),


    path('dashboard/create-lecture-code' , views.create_lecture_Code, name="create-lecture-code"),
    path('dashboard/delete-lecture-code' , views.delete_lecture_Code, name="delete-lecture-code"),

    path('dashboard/create-lecture-discount' , views.create_lecture_Discount, name="create-lecture-discount"),
    path('dashboard/delete-lecture-discount' , views.delete_lecture_Discount, name="delete-lecture-discount"),


    path('dashboard/chapter-functions' , views.chapter_functions , name="chapter-settings"),
    path('dashboard/group-functions' , views.group_functions , name="group-settings"),




    path('dashboard/delete-chapter' , views.delete_chapter , name="delete-chapter"),

    path('delete-lesson', views.delete_lesson, name='dashboard-delete-lesson'),
    path('delete-code', views.delete_code, name='dashboard-delete-code'),
    path('delete-assignment', views.delete_assignment, name='dashboard-delete-assignment'),
    path('dashboard-delete-assignment', views.dashboard_delete_assignment, name='dashboard-delete-assignment'),

    path('upload', views.upload, name='upload'),
    path('code-generator', views.code_generator, name='code-generator'),
    path('dashboard-edit-student', views.dashboard_profiles, name='dashboard-edit-student'),

    path('wallet/code-charge', views.code_charge_function, name='wallet-code-recharge-function'),


    path('chapter-code-charge', views.chapter_code_join_function, name='chapter-code-recharge'),
    path('lesson-code-charge', views.lesson_code_charge, name='code-recharge'),
    path('code-charge-function', views.code_charge_function, name='code-recharge-function'),


    path('dashboard/create-theme' , views.create_theme, name="create-theme"),
    path('dashboard/activate-theme' , views.activate_theme, name="activate-theme"),
    path('dashboard/delete-theme' , views.delete_theme, name="delete-theme"),
]

