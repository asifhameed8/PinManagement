from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from users.forms import LoginForm
from users.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('map_pins.urls')),
    path('register/', include('users.urls')),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
