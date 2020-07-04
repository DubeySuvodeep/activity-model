from  django.conf.urls import url 
from  django.urls import path

from activity_model.views import UserDetail

urlpatterns = [
    url(r'^get-user-detail/$', UserDetail.as_view(), name='get-user-detail'),
]