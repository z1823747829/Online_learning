import json

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        except_list = ["admin", 'media', "home", 'header', "sign_in", "sign_up", "get_user_info", 'ckeditor','mdeditor',]
        path_info = request.path_info
        if path_info == "/":
            return
        for url in except_list:
            if url in path_info:
                return
        if request.COOKIES.get('user_info') and request.session.get('user_info'):
            cookies = json.loads(request.COOKIES.get('user_info'))
            session = request.session.get('user_info')
            if cookies == session:
                return
        return HttpResponse(json.dumps({"status": False, 'msg': '请先登录'}))
