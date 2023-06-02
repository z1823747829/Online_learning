import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from web.modelforms.user import SigninModelForm, SignupModelForm, UpdateModelForm
from web.models.forum import Forum
from web.models.user import User
from web.serializer import UserSerializer, ForumSerializer


class SigninView(APIView):
    @csrf_exempt
    def post(self, request):
        form = SigninModelForm(data=request.POST)
        if form.is_valid():
            user = User.objects.filter(**form.cleaned_data).first()
            if not user:
                form.add_error("password", "用户名或密码错误")
                return Response({"status": False, "errors": form.errors})
            return set_cookies(request, user)
        return Response({"status": False, "errors": form.errors})


class SignupView(APIView):
    @csrf_exempt
    def post(self, request):
        form = SignupModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return Response({"status": True})
        return Response({"status": False, "errors": form.errors})


class SignOutView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        request.session.flush()
        response = Response({"status": True})
        response.delete_cookie("user_info", samesite="Lax")
        return response


class UserView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        uid = int(request.session['user_info'].get('id'))
        user = User.objects.filter(id=uid).first()
        user_data = UserSerializer(user).data
        return Response({"status": True, "user": user_data})

    @csrf_exempt
    def post(self, request):
        user_info = request.session.get('user_info')
        user = User.objects.filter(id=user_info['id']).first()
        form = UpdateModelForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            user = User.objects.filter(id=user_info['id']).first()
            return set_cookies(request, user)
        return Response({"status": False, "errors": form.errors})


class UserForumView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        uid = int(request.session['user_info'].get('id'))
        forums = Forum.objects.filter(user_id=uid)
        forums_data = ForumSerializer(forums, many=True).data
        return Response({"status": True, "forums": forums_data})


def set_cookies(request, user):
    serializer = UserSerializer(user)
    request.session["user_info"] = serializer.data
    request.session.set_expiry(60 * 60 * 24 * 7)
    response = Response({"status": True})
    response.set_cookie("user_info", json.dumps(serializer.data), max_age=60 * 60 * 24 * 7, samesite="Lax")
    return response
