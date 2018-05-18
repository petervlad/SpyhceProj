from django.conf.urls import url
from django.contrib import admin

from students.views import student_detail
from courses.views import course_add, course_detail, course_list


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #course URLSs
    url(r'^course_detail/(?P<course_id>\d)/$', course_detail, name='course_detail'),
    url(r'^course_add/$', course_add, name='course_add'),
    url(r'^$', course_list),

    #student URLs
    url(r'^student_detail/(?P<student_id>\d)/$', student_detail, name='student_detail')
]
