from django.urls import path

from notas.views import HomePageView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
]