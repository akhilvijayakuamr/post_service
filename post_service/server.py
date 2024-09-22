import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'post_service.settings')

import django
django.setup()

import grpc
from concurrent import futures
from proto import post_service_pb2
from proto import post_service_pb2_grpc
import time
from .service import PostServiceServicer


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
post_service_pb2_grpc.add_PostServiceServicer_to_server(PostServiceServicer(), server)
print("Starting grpc server on port 50052......") 
server.add_insecure_port('[::]:50052')
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)