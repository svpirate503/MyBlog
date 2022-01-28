from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import Post,Product
from .forms import CommentForm
from django.contrib.auth.decorators import login_required



def index(request):
	post = Post.objects.all()

	return render(request,'index.html',{'post':post})

def post_detail(request,post_id):
	text_comment = 0
	post = Post.objects.get(id=post_id)

	comments = post.comments.filter(active=True)

	for comentario in comments:
		text_comment+=1
		



	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.post = post 
			new_form.save()
			return HttpResponseRedirect("")
	else:
		form = CommentForm




	return render(request,'post_detail.html',{'post':post,'comments':comments,'form':form,'text_comment':text_comment})
@login_required
def profile(request):
	user = request.user
	return render(request,'account/profile.html',{'user':user})

def productos(request):
	productos = Product.objects.all()

	return render(request,'productos.html',{'productos':productos})
def paypal_proccess(request):
	return render(request,'paypal_proccess.html')