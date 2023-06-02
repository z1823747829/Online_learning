from django.urls import path

from web.views import page, user, academy, course, course_resource, comment, forum

urlpatterns = [
    # page
    path('header', page.HeaderView.as_view()),
    path('home', page.HomeView.as_view()),

    # user
    path('sign_in', user.SigninView.as_view()),
    path('sign_up', user.SignupView.as_view()),
    path('sign_out', user.SignOutView.as_view()),
    path('user', user.UserView.as_view()),
    path('user/forum', user.UserForumView.as_view()),

    # academy
    path('academy/list', academy.AcademyListView.as_view()),
    path('academy/<int:aid>', academy.AcademyView.as_view()),

    # course
    path('course/list', course.CourseListView.as_view()),
    path('course/<int:cid>', course.CourseView.as_view()),

    # course_resource
    path('course/resource/<int:crid>', course_resource.CourseResourceView.as_view()),
    path('course/resource/<int:crid>/set_time', course_resource.SetTimeView.as_view()),

    # comment
    path('comment/add', comment.CommentAddView.as_view()),

    # forum
    path('forum/list', forum.ForumListView.as_view()),
    path('forum/<int:fid>', forum.ForumView.as_view()),
    path('forum/add', forum.ForumAddView.as_view()),
    path('forum/img/add', forum.ForumImgAddView.as_view()),
]
