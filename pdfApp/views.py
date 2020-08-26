from django.shortcuts import render
from django.views.generic import TemplateView, View, CreateView
from .models import pdf_files
from .pdfscript import get_pdf_info, split, rotate, watermarker, rotate_all_page
from .forms import pdf_file_form
# Create your views here.



# class pdf_files_CreateView(CreateView):
#     model = pdf_files
#     queyset=pdf_files.objects.all()
#     fields=['pdf_file']
#     template_name = "split.html"

#     def save(self, *args, **kwargs):
#         super(pdf_files, self).save(*args, **kwargs)
#         filename=self.pdf_file.url
#         # print("this is the file name:", filename)
#         return filename

#     def rotate(self, request):
#         print(rotate_all_page(save()))
#         return render(request, 'split.html')





















# class index(TemplateView):
#     template_name = "pdfApp/index.html"



# def split_view(request):
#     if request.method == 'POST':
#         form = pdf_file_form(request.POST, request.FILES)
#         doc = request.FILES #returns a dict-like object
#         doc_name = doc['filename']
#         if form.is_valid():
#             split()
#             # file is saved
#             form.save()
#             fd = open(settings.MEDIA_URL+'documents/'+str(filename),'wb')
#             for chunk in doc_to_save.chunks():
#                 fd.write(chunk)
#             fd.close()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = pdf_file_form()
#     return render(request, 'split.html', {'form': form})



def rotate_view(request):
    if request.method == 'POST':
        
        
        form = pdf_file_form(request.POST, request.FILES)
        doc = request.FILES#returns a dict-like object
        print(doc , 'this is the stuff')
        if form.is_valid():
            # rotate(doc_name)
            # file is saved
            form.save()
            obj=pdf_files.objects.all().last()
            filename= obj.pdf_file.url
            rotate_all_page(r"C:\Users\DELL\Desktop\MyDjangoEnv\pdf_App\pdfpdf" +filename)
            # fd = open(settings.MEDIA_URL+'media/'+str(filename),'wb')
            # return HttpResponseRedirect('/success/url/')
            obj.delete()
    else:
        form = pdf_file_form()
    return render(request, 'split.html', {'form': form})


# def watermarker_view(request):
#     if request.method == 'POST':
#         form = pdf_file_form(request.POST, request.FILES)
#         doc = request.FILES #returns a dict-like object
#         doc_name = doc['filename']
#         if form.is_valid():
#             watermarker()
#             # file is saved
#             form.save()
#             fd = open(settings.MEDIA_URL+'documents/'+str(filename),'wb')
#             for chunk in doc_to_save.chunks():
#                 fd.write(chunk)
#             fd.close()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = pdf_file_form()
#     return render(request, 'watermarker.html', {'form': form})