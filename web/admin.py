from django.contrib import admin

from web.models import user, academy, teacher, course, course_resource, keyword, comment, forum

# Register your models here.
admin.site.site_header = 'CAUC线上学习平台后台管理系统'
admin.site.site_title = 'CAUC线上学习平台后台管理系统'


def get_fields(model):
    fields = ()
    for field in model._meta.fields:
        fields += (field.name,)
    print(fields)
    return fields


@admin.register(user.User)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'uname', 'password', 'gender', 'head', 'birthday', 'phone', 'email')
    '''分类'''
    list_filter = ('gender',)
    list_per_page = 10
    '''设置可编辑字段'''
    list_editable = ()
    '''设置详细页面中的只读字段'''
    readonly_fields = ()
    ordering = ('id',)
    search_fields = ('uname',)


@admin.register(academy.Academy)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'academy', 'code', 'img', 'profile_80')
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('academy',)


@admin.register(teacher.Teacher)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'academy', 'code', 'professional_title')
    exclude = ['is_superuser', 'is_active', 'is_staff', 'last_login']
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('teacher',)


@admin.register(course.Course)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'img', 'profile_80', 'teacher')
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('course',)
    filter_horizontal = ('keyword',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='教师').first():
            return qs.filter(teacher__code=request.user.username)
        else:
            return qs


@admin.register(keyword.Keyword)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword')
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('keyword',)


@admin.register(course_resource.CourseResource)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'resource', 'resource_file', 'course', 'order')
    list_filter = ('course',)
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('file',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='教师').first():
            return qs.filter(course__teacher__code=request.user.username)
        else:
            return qs


@admin.register(forum.Forum)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'profile', 'content_type', 'annex', 'time', 'status')
    list_per_page = 10
    list_editable = ('status',)
    ordering = ('id',)
    search_fields = ('user',)
    filter_horizontal = ('keyword',)


@admin.register(comment.Comment)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'forum', 'content', 'time')
    list_filter = ('user',)
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('user',)
