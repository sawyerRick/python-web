from django.forms import ModelForm
from .models import FilesModel

class FileForm(ModelForm):
    # form中的可选字段Meta, 直接从model中的fields中取
    class Meta:
        model = FilesModel
        fields = ['file']