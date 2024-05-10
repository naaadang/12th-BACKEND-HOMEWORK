from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Post, User, Comment
from django.views.decorators.csrf import csrf_exempt

# 전체 Post 리스트 반환(GET)
@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = []

        for post in posts:
            data.append(
                {
                    'id': post.pk,
                    'title': post.title,
                    'content': post.content,
                    'user_id': post.user_id.name,
                }
            )

        return JsonResponse(data=data, safe=False, status=200)

# 새로운 Post 생성(POST)

    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        user_name = request.POST['user']

        try:
            user_id = User.objects.get(name=user_name)
            post.user_id = user_id
        except User.DoesNotExist:
            raise Http404('user does not exist')
        post.save()

        return JsonResponse({"success":"item has been saved"}, status=201)