from proto import post_service_pb2
from proto import post_service_pb2_grpc
from post_app.views import *
from post_app.models import Like, Comment

class PostServiceServicer(post_service_pb2_grpc.PostServiceServicer):
    
    # Post Creation
    
    def CreatePost(self, request, context):
        response =  create_post(request, context)
        return post_service_pb2.CreatePostResponse(
            post_id = response['post_id'],
            message=response['message']
            )
    
    
    # Get All posts
    
    
    def GetAllPost(self, request, context):
        posts = all_posts(request, context)
        return post_service_pb2.GetAllPostResponse(posts = posts)
    
    
    
    # Get unique post
    
    
    def GetUniquePost(self, request, context):
        user_id = request.user_id
        response = unique_post(request, context)
        post = response['post']
        comments = response['comments']
        print("post",post)
        print("comment",comments)
        
        return post_service_pb2.GetUniquePostResponse(
            post_id = post.id,
            user_id = post.user_id,
            title = post.title,
            content = post.content,
            link = post.link,
            date = str(post.created_at),
            postimage = post.post_image.url,
            like = Like.objects.filter(post=post, user=user_id).exists(),
            like_count = Like.objects.filter(post=post).count(),
            comment_count = Comment.objects.filter(post=post).count(),
            comments = comments
        )
        
        
        
    
    # Like post
    
    
    def LikePost(self, request, context):
        response = like_post(request, context)
        return post_service_pb2.LikePostResponse(message=response['message'],
                                                 user_id=response['user_id'])
    
    
    # Comment post
    
    def CommentPost(self, request, context):
        response = comment_post(request, context)
        return post_service_pb2.CommentPostResponse(message=response['message'],
                                                    user_id=response['user_id'])
    
    
    # Replay comment
    
    
    def CommentReply(self, request, context):
        response = reply_comment(request, context)
        return post_service_pb2.CommentReplyResponse(message=response['message'])
    
    
    # Unique user posts
    
    def UniqueUserPosts(self, request, context):
        posts = user_all_posts(request, context)
        return post_service_pb2.UniqueUserPostsResponse(posts = posts)
    
    
    # Post Update
    
    
    def PostUpdate(self, request, context):
        response =  update_post(request, context)
        return post_service_pb2.PostUpdateResponse(
            post_id = response['post_id'],
            message=response['message']
            )
        
        
    # Delete Comment
    
    def CommentDelete(self, request, context):
        response = delete_comment(request, context)
        return post_service_pb2.CommentDeleteResponse(message = response['message'])
    
    
    
    # Delete Replay
    
    def ReplyDelete(self, request, context):
        response = delete_reply(request, context)
        return post_service_pb2.ReplyDeleteResponse(message = response['message'])
    
    
    
    # Delete Post
    
    
    def PostDelete(self, request, context):
        response = delete_post(request, context)
        return post_service_pb2.PostDeleteResponse(message =  response['message'])
    
    
    # Report Post
    
    
    def PostReport(self, request, context):
        response = report_post(request, context)
        return post_service_pb2.PostReportResponse(message =  response['message'])
    
    
   
    # Get admin all posts
    
    
    def GetAllAdminPost(self, request, context):
        posts = admin_all_posts(request, context)
        print("posts",posts)
        return post_service_pb2.GetAllAdminPostResponse(posts = posts)
    
    
    
    # Hide Unhide post
    
    def PostHide(self, request, context):
        response = hide_post(request, context)
        return post_service_pb2.PostHideResponse(message =  response['message'])
    
    
    
    
    
    

        
    
    
  