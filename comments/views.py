from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

# Create your views here.
def comments(request):
	comments = Comment.objects.all()
	context = {
               'form': CommentForm,
               'comments': comments,
              }

	return render(request, 'comments/newComments.html', context=context)


def post_comment(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				form.fields['text'] = request.user.username
				form.save()

	return redirect('/message_board/')
