from proto import post_service_pb2
from proto import post_service_pb2_grpc
from post_app.views import *
from post_app.models import Like

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
        user_id = request.user_id
        posts = all_posts(context)
        print(posts)
        post_list = [post_service_pb2.Post( post_id = post.id,
                                            user_id = post.user_id,
                                            title = post.title,
                                            content = post.content,
                                            link = post.link,
                                            date = str(post.created_at),
                                            postimage = post.post_image.url,
                                            like = Like.objects.filter(post=post, user=user_id).exists()
                                            ) for post in posts]
        return post_service_pb2.GetAllPostResponse(posts = post_list)
    
    
    
    # Get unique post
    
    
    def GetUniquePost(self, request, context):
        user_id = request.user_id
        response = unique_post(request, context)
        post = response['post']
        comments = response['comments']
        
        
        all_comments = [post_service_pb2.Comment(
            comment_id = comment.id,
            user_id = comment.user,
            content = comment.content,
            date = str(comment.created_at)
        )
        for comment in comments ]
        
        
        return post_service_pb2.GetUniquePostResponse(
            post_id = post.id,
            user_id = post.user_id,
            title = post.title,
            content = post.content,
            link = post.link,
            date = str(post.created_at),
            postimage = post.post_image.url,
            like = Like.objects.filter(post=post, user=user_id).exists(),
            comments = all_comments
        )
        
        
        
    
    # Like post
    
    
    def LikePost(self, request, context):
        response = like_post(request, context)
        return post_service_pb2.LikePostResponse(message=response['message'])
    
    
    # Comment post
    
    def CommentPost(self, request, context):
        response = comment_post(request, context)
        return post_service_pb2.CommentPostResponse(message=response['message'])