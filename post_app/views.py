from django.shortcuts import render
from .models import Post, Like, Comment, Reply
import time 
import uuid
from django.core.files.base import ContentFile
from grpc import StatusCode
from proto import post_service_pb2
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


def all_posts(request, context):
    try:
        posts = Post.objects.filter(is_delete=False)
        user_id = request.user_id
        
        post_list = [post_service_pb2.Post( post_id = post.id,
                                            user_id = post.user_id,
                                            title = post.title,
                                            content = post.content,
                                            link = post.link,
                                            date = str(post.created_at),
                                            postimage = post.post_image.url,
                                            like = Like.objects.filter(post=post, user=user_id).exists(),
                                            like_count = Like.objects.filter(post=post).count(),
                                            comment_count = Comment.objects.filter(post=post).count(),
                                            ) for post in posts]
        
        return post_list
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
            
        all_comments = []
        
        for comment in comments:
            
            replies = Reply.objects.filter(comment=comment).order_by('created_at')
            
            all_replies = [post_service_pb2.Reply(
                replay_id = reply.id,
                user_id = reply.user,
                mention_user_id = reply.mention_user,
                mention_user = reply.mention_user_full_name,
                content = reply.content,
                date = str(reply.created_at)
            ) for reply in replies]
            
            all_comments.append(post_service_pb2.Comment(
                comment_id = comment.id, 
                user_id = comment.user,
                content = comment.content,
                date = str(comment.created_at),
                replies=all_replies
            ))  
        
        return {
            "post":post,
            "comments":all_comments
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
        
        
        
        
# Replay comment


def reply_comment(request, context):
    
    user_id = request.user_id
    mention_user_id = request.mention_user_id
    comment_id = request.comment_id
    mention_user_fullname = request.mention_user_fullname
    content = request.content
    

    
    
    if (user_id is None or
       mention_user_id is None or
       comment_id is None or
       mention_user_fullname is None or
       content is None):
        
       context.abort(StatusCode.NOT_FOUND, "Missing parameter")
       
    try:
        comment =  Comment.objects.get(id=comment_id)
        reply = Reply(user=user_id, 
                        mention_user=mention_user_id, 
                        mention_user_full_name=mention_user_fullname, 
                        comment=comment, 
                        content=content)
        reply.save()
        return{
            'message': 'reply on post'
        }
    except Comment.DoesNotExist:
        content.abort(StatusCode.NOT_FOUND, "Comment is not found")
           
       

        





    
    
    
        
        
        
    
    
    
        
    

