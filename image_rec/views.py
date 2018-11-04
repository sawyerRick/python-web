from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm

def home(request):
    return render(request, 'image_rec/image_rec.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            #把表单的键值存入数据库对应的表
            form.save()
            file = request.FILES['file']
            filename = file.name
            path = "C:/Users/sawyer/Desktop/" + str(filename)
            handle_uploaded_file(request.FILES['file'], path)
            return HttpResponseRedirect('/image_rec/result/1?filename=' + str(filename))
        else :
            return HttpResponseRedirect('/image_rec/result/0')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(file, path):
    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def result(request, isSuccess):
    filename = request.GET.get('filename','None')
    return render(request, 'image_rec/result.html', {"pic":filename, "isSuccess":isSuccess})