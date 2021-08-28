"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# Documentations
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts", include("cartdrop.accounts.urls", namespace="accounts")),
    path("core/", include("cartdrop.core.urls", namespace="core")),
    path("products/", include("cartdrop.products.urls", namespace="products")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Documentations
    path(
        "openapi",
        get_schema_view(
            title="Cartdrop",
            description="Documentation for cartdrop api using swagger ui",
            version="1.10.0",
        ),
        name="openapi-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="documantation/documantation.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="api_documentation",
    ),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
