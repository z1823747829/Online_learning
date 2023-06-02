from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.course import Course
from web.models.forum import Forum
from web.models.keyword import Keyword
from web.serializer import KeywordSerializer, CourseSerializer, ForumSerializer


class HeaderView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        return Response({"status": True, "logo": '/media/CAUC.jpg'})


class HomeView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        if request.COOKIES.get('user_info') and request.session.get('user_info'):
            uid = int(request.session['user_info'].get('id'))
            user_keywords = Keyword.objects.all().annotate(
                clicks=Count('course', filter=Q(course__courseclick__user__id=uid))).filter(clicks__gt=0).order_by('-clicks')[0:3]
            user_courses = Course.objects.filter(keyword__in=user_keywords).annotate(
                clicks=Count('courseclick')).order_by('-clicks')[0:5]
            if len(user_courses) < 5:
                courses = Course.objects.annotate(clicks=Count('courseclick')).order_by('-clicks')[0:5]
                user_courses = user_courses | courses
            home = CourseSerializer(user_courses, many=True).data
        else:
            user_courses = Course.objects.annotate(clicks=Count('courseclick')).order_by('-clicks')[0:5]
            home = CourseSerializer(user_courses, many=True).data
        courses = Course.objects.annotate(clicks=Count('courseclick')).order_by('-clicks')[0:10]
        popular_courses = CourseSerializer(courses, many=True).data
        keywords = Keyword.objects.annotate(clicks=Count('course__courseclick')).order_by('-clicks')[0:10]
        popular_keywords = KeywordSerializer(keywords, many=True).data
        forums = Forum.objects.annotate(clicks=Count('forumclick')).order_by('-clicks')[0:10]
        popular_forums = ForumSerializer(forums, many=True).data
        return Response(
            {"status": True, "home": home, "popular_courses": popular_courses, "popular_keywords": popular_keywords,
             "popular_forums": popular_forums})
