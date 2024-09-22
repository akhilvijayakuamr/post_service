from django.shortcuts import render
from .models import Post, Like, Comment
import time 
import uuid
from django.core.files.base import ContentFile
from grpc import StatusCode
# Create your views here.



# Create Post view 

def create_post(request, context):
    user_id = request.user_id
    title = request.title
    post_image = request.post_image
    content = request.content
    link = request.link
    
    post = Post(user_id = user_id,
                title = title,
                content = content,
                link = link
                )
    
  
    
    post_image_name = f"profile_{uuid.uuid4().hex}_{int(time.time())}.jpg"
    post_image_storage = post.post_image.storage
    unique_post_image_name = post_image_storage.get_available_name(post_image_name)
    post.post_image.save(unique_post_image_name, ContentFile(post_image))

    post.save()
     
    return {
            'post_id':post.id,
            'message': 'Post Creation Successful'
        }
    
    
    
# Get all posts


def all_posts(context):
    try:
        posts = Post.objects.filter(is_delete=False)
        return posts
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Posts not found")
    


# Get unique post



def unique_post(request, context):
    post_id = request.post_id
  
   
    try:
        post = Post.objects.get(id = post_id)
        try:
            comments = Comment.objects.filter(post=post).order_by('created_at')
        except Comment.DoesNotExist:
            context.abort(StatusCode.NOT_FOUND, "Comment not found") 
        return {
            "post":post,
            "comments":comments
        }
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Post not found")
        
        
        
# Like post

def like_post(request, context):
    post_id = request.post_id
    user_id = request.user_id
    
    if post_id is None:
        context.abort(StatusCode.NOT_FOUND, "Missing parameter")
        
    if user_id is None:
        context.abort(StatusCode.NOT_FOUND, "Missing parameter")
        
    try:
        post = Post.objects.get(id = post_id)
        like, created = Like.objects.get_or_create(user = user_id, post = post)

        if created:
             return {
            'message': 'like post'
            }
        else:
            like.delete()
            return{
                'message': 'unlike post' 
            }
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Post not found")
        
        
        
        
# Comment post

def comment_post(request, context):
    post_id = request.post_id
    user_id = request.user_id
    content = request.content
    
    if post_id is None:
        context.abort(StatusCode.NOT_FOUND, "Missing parameter")
         
         
    if user_id is None:
        context.abort(StatusCode.NOT_FOUND, "Missing parameter")
         
    if content is None:
        context.abort(StatusCode.NOT_FOUND, "Missing parameter")
    
    try:
        post = Post.objects.get(id = post_id)
        comment = Comment(user=user_id, post=post, content=content)
        comment.save()
    
        return {
            'message': 'comment on post'
        }
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Post not found")
        
        
        
    
    
    
        
    

