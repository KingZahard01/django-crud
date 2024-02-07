from django.urls import path
from notas.views import HomePageView, CreateNotaView, UpdateNotaView, DeleteNotaView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/', CreateNotaView.as_view(), name='new'),
    path('edit/<int:pk>', UpdateNotaView.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteNotaView.as_view(), name='delete')
]