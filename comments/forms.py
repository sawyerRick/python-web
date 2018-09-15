# 用django提供的forms创建表单，表单为已有的models的fields
from django import forms
from .models import Comment

# 从已有模型创建表单 
# 继承form.ModelForm
# 子元类Meta里定义需要的model与fields

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'text']