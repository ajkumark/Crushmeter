from django.conf.urls import patterns, include, url


urlpatterns = patterns('crushapp.views',
	url(r'^$', 'index', name='index'),
	# url(r'^login/$', 'login', name='ulogin'),
	# url(r'^user/login/', name='login'),
	# url(r'^logout/$', 'user_logout', name='user_logout'),
)