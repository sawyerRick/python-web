from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Userphoto
# 图片识别
from PIL import Image
import pytesseract, os
from newsite.settings import BASE_DIR

def home(request):
    return render(request, 'image_rec/home.html')


def uploadImg(request):
    pic = Userphoto(photo=request.FILES.get('photo'))
    pic.save()
    text = pytesseract.image_to_string(Image.open(pic.photo), lang='chi_sim')
    return render(request, 'image_rec/home.html', {'pic': pic, 'text': text})
