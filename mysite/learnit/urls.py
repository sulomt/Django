from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from learnit.models import Subs
from . import views

python=Subs.objects.filter(tech='Python')


urlpatterns = [ 
		url(r'^$',views.subjects,name='subjetcs'),
                url(r'^python/', ListView.as_view(
                                    queryset=python.order_by("-date")[:25],
                                    template_name="learnit/learn.html")),

	       url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Subs,
                                    template_name="learnit/detail.html"))
	       
            ]
