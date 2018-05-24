# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from coordinates_approach.models import Document
from coordinates_approach.forms import DocumentForm

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')

    else:
        form = DocumentForm() # A empty, unbound form
    # Render list page with the documents and the form
    return render(request, 'coordinates_approach/media_upload.html',{
    'form' : form
    })
'''
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
'''

