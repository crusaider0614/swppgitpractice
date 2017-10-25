from django.conf.urls import url
from .views import hero_list, hero_detail


urlpatterns = [
	url(r'^hero$', hero_list, name='hero_list'),
	url(r'^hero/(?P<hero_id>[0-9]+)$', hero_detail, name='hero_detail'),
]
