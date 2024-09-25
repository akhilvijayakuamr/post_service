# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import post_service_pb2 as post__service__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in post_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PostServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/post_service.PostService/CreatePost',
                request_serializer=post__service__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=post__service__pb2.CreatePostResponse.FromString,
                _registered_method=True)
        self.GetAllPost = channel.unary_unary(
                '/post_service.PostService/GetAllPost',
                request_serializer=post__service__pb2.GetAllPostRequest.SerializeToString,
                response_deserializer=post__service__pb2.GetAllPostResponse.FromString,
                _registered_method=True)
        self.GetUniquePost = channel.unary_unary(
                '/post_service.PostService/GetUniquePost',
                request_serializer=post__service__pb2.GetUniquePostRequest.SerializeToString,
                response_deserializer=post__service__pb2.GetUniquePostResponse.FromString,
                _registered_method=True)
        self.LikePost = channel.unary_unary(
                '/post_service.PostService/LikePost',
                request_serializer=post__service__pb2.LikePostRequest.SerializeToString,
                response_deserializer=post__service__pb2.LikePostResponse.FromString,
                _registered_method=True)
        self.CommentPost = channel.unary_unary(
                '/post_service.PostService/CommentPost',
                request_serializer=post__service__pb2.CommentPostRequest.SerializeToString,
                response_deserializer=post__service__pb2.CommentPostResponse.FromString,
                _registered_method=True)
        self.CommentReply = channel.unary_unary(
                '/post_service.PostService/CommentReply',
                request_serializer=post__service__pb2.CommentReplyRequest.SerializeToString,
                response_deserializer=post__service__pb2.CommentReplyResponse.FromString,
                _registered_method=True)


class PostServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUniquePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LikePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommentPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommentReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=post__service__pb2.CreatePostRequest.FromString,
                    response_serializer=post__service__pb2.CreatePostResponse.SerializeToString,
            ),
            'GetAllPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllPost,
                    request_deserializer=post__service__pb2.GetAllPostRequest.FromString,
                    response_serializer=post__service__pb2.GetAllPostResponse.SerializeToString,
            ),
            'GetUniquePost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUniquePost,
                    request_deserializer=post__service__pb2.GetUniquePostRequest.FromString,
                    response_serializer=post__service__pb2.GetUniquePostResponse.SerializeToString,
            ),
            'LikePost': grpc.unary_unary_rpc_method_handler(
                    servicer.LikePost,
                    request_deserializer=post__service__pb2.LikePostRequest.FromString,
                    response_serializer=post__service__pb2.LikePostResponse.SerializeToString,
            ),
            'CommentPost': grpc.unary_unary_rpc_method_handler(
                    servicer.CommentPost,
                    request_deserializer=post__service__pb2.CommentPostRequest.FromString,
                    response_serializer=post__service__pb2.CommentPostResponse.SerializeToString,
            ),
            'CommentReply': grpc.unary_unary_rpc_method_handler(
                    servicer.CommentReply,
                    request_deserializer=post__service__pb2.CommentReplyRequest.FromString,
                    response_serializer=post__service__pb2.CommentReplyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'post_service.PostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('post_service.PostService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PostService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/post_service.PostService/CreatePost',
            post__service__pb2.CreatePostRequest.SerializeToString,
            post__service__pb2.CreatePostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/post_service.PostService/GetAllPost',
            post__service__pb2.GetAllPostRequest.SerializeToString,
            post__service__pb2.GetAllPostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUniquePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/post_service.PostService/GetUniquePost',
            post__service__pb2.GetUniquePostRequest.SerializeToString,
            post__service__pb2.GetUniquePostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LikePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/post_service.PostService/LikePost',
            post__service__pb2.LikePostRequest.SerializeToString,
            post__service__pb2.LikePostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CommentPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/post_service.PostService/CommentPost',
            post__service__pb2.CommentPostRequest.SerializeToString,
            post__service__pb2.CommentPostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CommentReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/post_service.PostService/CommentReply',
            post__service__pb2.CommentReplyRequest.SerializeToString,
            post__service__pb2.CommentReplyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
