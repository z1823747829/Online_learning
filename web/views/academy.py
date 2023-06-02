from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.academy import Academy
from web.models.course import Course
from web.serializer import AcademySerializer, CourseSerializer


class AcademyListView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        academies = Academy.objects.all()
        academies_data = AcademySerializer(academies, many=True).data
        return Response({"status": True, "academies": academies_data})


class AcademyView(APIView):
    @staticmethod
    def get(request, aid, *args, **kwargs):
        academy = Academy.objects.filter(id=aid).first()
        academy_data = AcademySerializer(academy).data
        courses = Course.objects.filter(teacher__academy_id=aid).all()
        courses_data = CourseSerializer(courses, many=True).data
        return Response({"status": True, "academy": academy_data, "courses": courses_data})
