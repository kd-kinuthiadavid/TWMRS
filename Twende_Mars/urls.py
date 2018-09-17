from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from Twende_Mars import views

urlpatterns=[
    url(r'^$', views.photos, name='welcome'),
    url(r'^september/', views.september_first, name='september'),
    url(r'^navcam/', views.navcam, name='navcam'),
    url(r'^fhaz/', views.fhaz, name='fhaz'),
    url(r'^mast/', views.mast, name='mast'),
    url(r'^chemcam/', views.chemcam, name='chemcam'),
    url(r'^mahli/', views.mahli, name='mahli'),
    url(r'^mardi/', views.mardi, name='mardi'),
    url(r'^rhaz/', views.rhaz, name='rhaz'),

]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)