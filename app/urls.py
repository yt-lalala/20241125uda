from django.urls import path
from app import views

from django.urls import path
from app import views

from django.contrib import admin
from django.urls import path, include
# from shimadaproject import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from AI import predict
from django.conf import settings
from django.conf.urls.static import static
from .views import Aicall

urlpatterns = [
    path("", views.Top.as_view(), name="top"),
    path("top", views.Top.as_view(), name="top"),
    path('single', views.single, name='single'),
    path('preview', views.preview, name='preview'),
    path('single_ura', views.single_ura, name='single_ura'),
    path('preview_ura', views.preview_ura, name='preview_ura'),
    path('shimadaen_aicall/', Aicall.as_view(), name='shimadaen_aicall'),
    path('analysis', views.analysis, name='analysis'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)