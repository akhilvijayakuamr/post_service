from django.shortcuts import render
from .models import Post, Like, Comment, Reply, Report
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
        posts = Post.objects.filter(is_delete=False, is_block=False)
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
        post = Post.objects.get(id = post_id, is_block=False)
        try:
            comments = Comment.objects.filter(post=post, is_delete=False).order_by('created_at')
        except Comment.DoesNotExist:
            comments = []
        all_comments = []
        
        for comment in comments:
            
            replies = Reply.objects.filter(comment=comment, is_delete=False).order_by('created_at')
            replies_count = Reply.objects.filter(comment=comment).count()
            
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
                reply_count=replies_count,
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

        if created :
        
            return {
                'message': 'like post',
                'user_id':post.user_id
            }
        else:
            like.delete()
            return{
                'message': 'unlike post',
                'user_id':post.user_id 
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
            'message': 'comment on post',
            'user_id':post.user_id
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
        context.abort(StatusCode.NOT_FOUND, "Comment is not found")
        
        
        
        
# Unique user allposts



def user_all_posts(request, context):
    try:
        user_id = request.user_id
        posts = Post.objects.filter(user_id=user_id, is_delete=False, is_block=False)
        
        
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
        
        
        
        
# Post Update


def update_post(request, context):
    post_id = request.post_id
    user_id = request.user_id
    title = request.title
    post_image = request.post_image
    content = request.content
    link = request.link
    try:
        post = Post.objects.get(id = post_id)
    
        if (post.user_id==user_id):
            if title:
                post.title = title
            if content:
                post.content = content
            if link:
                post.link = link
            if post_image:
                post_image_name = f"post_{uuid.uuid4().hex}_{int(time.time())}.jpg"
                post.post_image.save(post_image_name, ContentFile(post_image))
            post.save()
        else:
            context.abort(StatusCode.NOT_FOUND, "Permission denied")
        
        return {
                'post_id':post.id,
                'message': 'Post Updation Successful'
            }
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Post is not found")
        
        
        
        
# Comment delete


def delete_comment(request, context):
    comment_id = request.comment_id
    try:
        comment =  Comment.objects.get(id = comment_id)
        comment.is_delete = True
        comment.save()
        return{
            'message': 'Comment is delete is successfully'
        }
    except Comment.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Comment is not found")
        
        
        
# Reply delete


def delete_reply(request, context):
    reply_id = request.reply_id
    try:
        comment =  Reply.objects.get(id = reply_id)
        comment.is_delete = True
        comment.save()
        return{
            'message': 'Reply is delete is successfully'
        }
    except Reply.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Reply is not found")
        
        
        
# Post delete


def delete_post(request, context):
    post_id = request.post_id
    try:
        post = Post.objects.get(id = post_id)
        post.is_delete = True
        post.save()
        return{
            'message': 'Post is delete is succssfully'
        }
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Post is not found")
        
        
        
# Post Report


def report_post(request, context):
    post_id = request.post_id
    report_user_id = request.report_user_id
    reson = request.reson
    try:
        post = Post.objects.get(id=post_id)
        report = Report(post=post, report_user_id=report_user_id, reson = reson)
        report.save()
        return{
            'message': 'Report succssfully'
        }
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Post is not found")
    
    
# Admin Get all posts


def admin_all_posts(request, context):
    try:
        posts = Post.objects.all()
        post_list = [post_service_pb2.AdminPost( post_id = post.id,
                                                 user_id = post.user_id,
                                                 title = post.title,
                                                 content = post.content,
                                                 link = post.link,
                                                 date = str(post.created_at),
                                                 postimage = post.post_image.url,
                                                 is_block = post.is_block,
                                                 like_count = Like.objects.filter(post=post).count(),
                                                 comment_count = Comment.objects.filter(post=post).count(),
                                                 is_delete = post.is_delete,
                                                 reports=[
                                                    post_service_pb2.Report(
                                                        report_id=report.id,
                                                        report_user_id = report.report_user_id,
                                                        reason=report.reson,
                                                        created_at=str(report.created_at),
                                                    ) for report in Report.objects.filter(post=post)],
                                                 is_report = Report.objects.filter(post=post).exists()
                                                 ) for post in posts]
        return post_list
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Posts not found")     
        
        
        
        
# Hide unHide post


def hide_post(request, context):
    post_id = request.post_id
    try:
        post = Post.objects.get(id = post_id)
        if (post.is_block):
            post.is_block = False
            post.save()
            return{
                'message': 'Post is unhide'
            }
        else:
            post.is_block = True
            post.save()
            return{
                'message': 'Post is hide'
            }
            
    except Post.DoesNotExist:
        context.abort(StatusCode.NOT_FOUND, "Post is not found") 
           
       

        





    
    
    
        
        
        
    
    
    
        
    

