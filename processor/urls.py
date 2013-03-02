from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(
        r'^$',
        view='processor.views.upload_history',
        name='processor',
    ),
)
