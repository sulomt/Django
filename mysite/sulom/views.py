# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.#views for sulom

def index_s(request):
	return render(request,'sulom/home.html')

def contact(request):
    return render(request, 'sulom/basic.html',{'content':['If you would like to contact me, please email me.','sulomtulshibagwale@gmail.com','Find me on Facebook','Sulom Tulshibagwale']})
