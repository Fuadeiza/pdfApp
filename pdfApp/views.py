from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import pdf_files
from .pdfscript import get_pdf_info, split, rotate, watermarker
from .forms import pdf_file_form
# Create your views here.


class index(TemplateView):
    template_name = "pdfApp/index.html"



def split_view(request):
    if request.method == 'POST':
        form = pdf_file_form(request.POST, request.FILES)
        doc = request.FILES #returns a dict-like object
        doc_name = doc['filename']
        if form.is_valid():
            split()
            # file is saved
            form.save()
            fd = open(settings.MEDIA_URL+'documents/'+str(filename),'wb')
            for chunk in doc_to_save.chunks():
                fd.write(chunk)
            fd.close()
            return HttpResponseRedirect('/success/url/')
    else:
        form = pdf_file_form()
    return render(request, 'split.html', {'form': form})



def rotate_view(request):
    if request.method == 'POST':
        form = pdf_file_form(request.POST, request.FILES)
        doc = request.FILES #returns a dict-like object
        doc_name = doc['filename']
        if form.is_valid():
            rotate()
            # file is saved
            form.save()
            fd = open(settings.MEDIA_URL+'documents/'+str(filename),'wb')
            for chunk in doc_to_save.chunks():
                fd.write(chunk)
            fd.close()
            return HttpResponseRedirect('/success/url/')
    else:
        form = pdf_file_form()
    return render(request, 'rotate.html', {'form': form})


def watermarker_view(request):
    if request.method == 'POST':
        form = pdf_file_form(request.POST, request.FILES)
        doc = request.FILES #returns a dict-like object
        doc_name = doc['filename']
        if form.is_valid():
            watermarker()
            # file is saved
            form.save()
            fd = open(settings.MEDIA_URL+'documents/'+str(filename),'wb')
            for chunk in doc_to_save.chunks():
                fd.write(chunk)
            fd.close()
            return HttpResponseRedirect('/success/url/')
    else:
        form = pdf_file_form()
    return render(request, 'watermarker.html', {'form': form})