from map_pins import views
from django.urls import path


urlpatterns = [
   path('',  views.PinListView.as_view(), name='pin_ajax'),
   path('ajax/pin/create/',  views.PinCreateView.as_view(), name='pin_ajax_create'),
   path('ajax/pin/update/',  views.PinUpdateView.as_view(), name='pin_ajax_update'),
   path('ajax/pin/delete/',  views.PinDeleteView.as_view(), name='pin_ajax_delete'),

   path('pins', views.pins, name="pins"),
]
