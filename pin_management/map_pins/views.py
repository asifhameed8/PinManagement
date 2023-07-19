from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView, View
from django.forms.models import model_to_dict

from map_pins.models import MapPin


class BaseView(LoginRequiredMixin):
    login_url = '/login/'


class PinListView(BaseView, ListView):
    model = MapPin
    template_name = 'map_pins/pin.html'
    context_object_name = 'pins'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_choices'] = MapPin.CATEGORY_CHOICES
        context['users'] = User.objects.all().values('id', 'first_name', 'last_name', 'username')
        context['GOOGLE_API_KEY'] = settings.GOOGLE_API_KEY
        return context


class PinCreateView(BaseView, View):
    def get(self, request):
        params = {
            'name': request.GET.get('name', None),
            'description': request.GET.get('description', None),
            'address': request.GET.get('address', None),
            'longitude': request.GET.get('longitude', None),
            'latitude': request.GET.get('latitude', None),
            'category': request.GET.get('category', None),
            'contact_person': request.GET.get('contact_person', None),
            'value': request.GET.get('value', None),
            'progress': request.GET.get('progress', None),
        }

        assigned_user_id = request.GET.get('assigned_user', None)
        user = User.objects.get(id=assigned_user_id)
        obj = MapPin.objects.create(**params, assigned_user=user)
        pin = model_to_dict(obj)
        pin['assigned_user'] = model_to_dict(user, fields=('id', 'username', 'first_name', 'last_name'))

        return JsonResponse({'pin': pin})


class PinUpdateView(BaseView, View):
    def get(self, request):
        params = {
            'name': request.GET.get('name', None),
            'description': request.GET.get('description', None),
            'address': request.GET.get('address', None),
            'longitude': request.GET.get('longitude', None),
            'latitude': request.GET.get('latitude', None),
            'category': request.GET.get('category', None),
            'contact_person': request.GET.get('contact_person', None),
            'value': request.GET.get('value', None),
            'progress': request.GET.get('progress', None),
        }

        assigned_user_id = request.GET.get('assigned_user', None)
        user = User.objects.get(id=assigned_user_id)

        pin_id = request.GET.get('id', None)
        objs = MapPin.objects.filter(id=pin_id)
        objs.update(**params, assigned_user=user)

        pin = model_to_dict(objs[0])
        pin['assigned_user'] = model_to_dict(user, fields=('id', 'username', 'first_name', 'last_name'))

        return JsonResponse({'pin': pin})


class PinDeleteView(BaseView, View):
    def get(self, request):
        id = request.GET.get('id', None)

        obj = MapPin.objects.get(id=id)
        data = {
            'id': obj.id,
            'name': obj.name,
            'longitude': obj.longitude,
            'latitude': obj.latitude,
            'deleted': True
        }

        obj.delete()

        return JsonResponse(data)


@login_required
def pins(_request):
    pins = MapPin.objects.exclude(
        Q(latitude__isnull=True) |
        Q(longitude__isnull=True)
    ).values(
        'id',
        'name',
        'latitude',
        'longitude',
        'address',
    )
    result_list = list(pins)

    return JsonResponse(result_list, safe=False)
