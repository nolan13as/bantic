from django.urls import re_path, path

urlpatterns = [
    re_path(r'^$', cabinet.as_view(), name='index'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
