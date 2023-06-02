from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from web.modelforms.course_resource_time import CourseResourceTimeModelForm
from web.models.comment import Comment
from web.models.course import Course
from web.models.course_resource import CourseResource, CourseResourceTime
from web.models.user import User
from web.serializer import CourseResourceSerializer, CommentSerializer, CourseSerializer


class CourseResourceView(APIView):
    @staticmethod
    def get(request, crid):
        uid = int(request.session['user_info'].get('id'))

        if not CourseResourceTime.objects.filter(user_id=uid, course_resource_id=crid).exists():
            CourseResourceTime.objects.create(user_id=uid, course_resource_id=crid, time=0)
        crt = CourseResourceTime.objects.filter(user_id=uid, course_resource_id=crid).first()
        course_resource = CourseResource.objects.filter(id=crid).first()
        course_resource_data = CourseResourceSerializer(course_resource).data
        course = Course.objects.filter(id=course_resource.course.id).first()
        course_data = CourseSerializer(course).data
        course_resources = CourseResource.objects.filter(course=course)
        course_resources_data = CourseResourceSerializer(course_resources, many=True).data
        comments = Comment.objects.filter(course=course)
        comments_data = CommentSerializer(comments, many=True).data
        return Response({"status": True, "course": course_data, "course_resource": course_resource_data,
                         "course_resources": course_resources_data, "comments": comments_data, "time": crt.time})


class SetTimeView(APIView):
    @csrf_exempt
    def post(self, request, crid):
        print(request.POST)
        uid = int(request.session['user_info'].get('id'))
        user = User.objects.filter(id=uid).first()
        course_resource = CourseResource.objects.filter(id=crid).first()
        crt = CourseResourceTime.objects.filter(user=user, course_resource=course_resource).first()
        form = CourseResourceTimeModelForm(data=request.POST, instance=crt)
        if form.is_valid():
            form.save()
            return Response({"status": True})
        return Response({"status": False, "errors": form.errors})
