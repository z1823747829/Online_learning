from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from web.modelforms.comment import CommentAddModelForm
from web.models.course import Course
from web.models.forum import Forum
from web.models.user import User


class CommentAddView(APIView):
    @csrf_exempt
    def post(self, request):
        uid = int(request.session['user_info'].get('id'))
        user = User.objects.filter(id=uid).first()
        form = CommentAddModelForm(data=request.POST)
        c_id = request.POST.get('c_id')
        if c_id:
            course = Course.objects.filter(id=c_id).first()
            forum = None
        else:
            f_id = request.POST.get('f_id')
            course = None
            forum = Forum.objects.filter(id=f_id).first()
        if form.is_valid():
            new_forum = form.save(commit=False)
            new_forum.user = user
            new_forum.course = course
            new_forum.forum = forum
            new_forum.save()
            return Response({"status": True})
        return Response({"status": False, "errors": form.errors})
