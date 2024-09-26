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
        return post_service_pb2.LikePostResponse(message=response['message'])
    
    
    # Comment post
    
    def CommentPost(self, request, context):
        response = comment_post(request, context)
        return post_service_pb2.CommentPostResponse(message=response['message'])
    
    
    # Replay comment
    
    
    def CommentReply(self, request, context):
        response = reply_comment(request, context)
        return post_service_pb2.CommentReplyResponse(message=response['message'])
    
    
    # Unique user posts
    
    def UniqueUserPosts(self, request, context):
        posts = user_all_posts(request, context)
        return post_service_pb2.UniqueUserPostsResponse(posts = posts)

        
    
    
  