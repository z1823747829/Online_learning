from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.academy import Academy
from web.models.course import Course
from web.models.courseclick import CourseClick
from web.models.course_resource import CourseResource
from web.models.user import User
from web.serializer import AcademySerializer, CourseSerializer, CourseResourceSerializer


class CourseListView(APIView):
    @staticmethod
    def get(request):
        code = request.GET.get("code", '')
        page = int(request.GET.get("page", 1))
        size = int(request.GET.get("size", 12))
        search = (request.GET.get("search", ""))
        select = (request.GET.get("select", 1))
        academies = Academy.objects.all()
        academies_data = AcademySerializer(academies, many=True).data
        search_list = {}
        if code:
            search_list['teacher__academy__code'] = code
        if search:
            match select:
                case '1':
                    search_list['course__contains'] = search
                case '2':
                    search_list['keyword__keyword__contains'] = search
        if search and select == '3':
            courses = Course.objects.filter(Q(course__contains=search) | Q(keyword__keyword__contains=search),
                                            **search_list).distinct().order_by('id')
        else:
            courses = Course.objects.filter(**search_list).order_by('id')
        courses_page = Paginator(courses, size)
        courses_data = CourseSerializer(courses_page.get_page(page), many=True).data
        count = courses.count()
        return Response(
            {"status": True, "academies": academies_data, "courses": courses_data, "count": count, 'msg': '123'})


class CourseView(APIView):
    @staticmethod
    def get(request, cid, *args, **kwargs):
        course = Course.objects.filter(id=cid).first()
        uid = int(request.session['user_info'].get('id'))
        user = User.objects.filter(id=uid).first()
        CourseClick.objects.create(user=user, course=course)
        course_serializer = CourseSerializer(course)
        course_resources = CourseResource.objects.filter(course=cid).all().order_by('order')
        course_resources_data = CourseResourceSerializer(course_resources, many=True).data
        return Response({"status": True, "course": course_serializer.data, "course_resources": course_resources_data})
