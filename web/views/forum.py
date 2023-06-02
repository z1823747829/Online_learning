from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.comment import Comment
from web.models.forum import Forum
from web.models.forum_click import ForumClick
from web.models.keyword import Keyword
from web.modelforms.forum import ForumAddModelForm, ForumImgAddModelForm
from web.models.sensitive_word import SensitiveWord
from web.models.user import User
from web.serializer import KeywordSerializer, ForumSerializer, CommentSerializer, ForumImgSerializer, \
    SensitiveWordSerializer


class ForumListView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        forums = Forum.objects.filter(status=1)
        forums_data = ForumSerializer(forums, many=True).data
        return Response({"status": True, "forums": forums_data})


class ForumView(APIView):
    @staticmethod
    def get(request, fid, *args, **kwargs):
        uid = int(request.session['user_info'].get('id'))
        user = User.objects.filter(id=uid).first()
        forum = Forum.objects.filter(id=fid).first()
        ForumClick.objects.create(user=user, forum=forum)
        forum_data = ForumSerializer(forum).data
        comments = Comment.objects.filter(forum=forum)
        comments_data = CommentSerializer(comments, many=True).data
        return Response({"status": True, "forum": forum_data, 'comments': comments_data})


class ForumAddView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        keywords = Keyword.objects.annotate(clicks=Count('course__courseclick')).order_by('-clicks')
        keywords_data = KeywordSerializer(keywords, many=True).data
        return Response({"status": True, "keywords": keywords_data})

    @csrf_exempt
    def post(self, request):
        uid = int(request.session['user_info'].get('id'))
        user = User.objects.filter(id=uid).first()
        keyword = request.POST.getlist('keyword')
        form = ForumAddModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_forum = form.save(commit=False)
            sensitive_words = SensitiveWord.objects.all()
            sw = SensitiveWordSerializer(sensitive_words, many=True).data
            if new_forum.content_type:
                new_forum.rtf_content = None
                new_forum.status = set_status(sw, new_forum.md_content)
            else:
                new_forum.md_content = None
                new_forum.status = set_status(sw, new_forum.rtf_content)
            new_forum.user = user
            new_forum.save()
            for i in keyword:
                k = Keyword.objects.filter(id=i).first()
                new_forum.keyword.add(k)
            return Response({"status": True})
        return Response({"status": False, "errors": form.errors})


class ForumImgAddView(APIView):
    @csrf_exempt
    def post(self, request):
        form = ForumImgAddModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            instance = form.save()
            forum_img = ForumImgSerializer(instance).data
            return Response({"status": True, "url": forum_img.get('img')})
        return Response({"status": False, "errors": form.errors})


def set_status(sensitive_words, content):
    for item in sensitive_words:
        if item.get('word') in content:
            return 2
    return 0
