from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("", include(("common.urls", "common"), namespace="common")),
                path("docs/", include_docs_urls(title="API Documentation")),
            ]
        ),
    ),
    path("admin/", admin.site.urls),
]
