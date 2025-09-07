from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler403 = "pages.views.handler403"
handler404 = "pages.views.handler404"
handler500 = "pages.views.handler500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("personal_account/", include("personal_account.urls")),
    # path("auth/", include("django.contrib.auth.urls")),
    # path(
    #     "auth/registration/",
    #     CreateView.as_view(
    #         template_name="registration/registration_form.html",
    #         form_class=UserCreationForm,
    #         success_url=reverse_lazy("personal_account:index"),
    #     ),
    #     name="registration",
    # ),
]

# Добавляем для работы медиа
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
