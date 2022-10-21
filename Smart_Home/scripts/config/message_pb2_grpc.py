# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import message_pb2 as message__pb2


class GrpcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ServerClient = channel.unary_stream(
                '/Grpc/ServerClient',
                request_serializer=message__pb2.Request.SerializeToString,
                response_deserializer=message__pb2.Response.FromString,
                )
        self.ClientServer = channel.stream_unary(
                '/Grpc/ClientServer',
                request_serializer=message__pb2.Request.SerializeToString,
                response_deserializer=message__pb2.Response.FromString,
                )
        self.InteractingStream = channel.stream_stream(
                '/Grpc/InteractingStream',
                request_serializer=message__pb2.Request.SerializeToString,
                response_deserializer=message__pb2.Response.FromString,
                )


class GrpcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ServerClient(self, request, context):
        """Server Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientServer(self, request_iterator, context):
        """Server Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InteractingStream(self, request_iterator, context):
        """Both Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ServerClient': grpc.unary_stream_rpc_method_handler(
                    servicer.ServerClient,
                    request_deserializer=message__pb2.Request.FromString,
                    response_serializer=message__pb2.Response.SerializeToString,
            ),
            'ClientServer': grpc.stream_unary_rpc_method_handler(
                    servicer.ClientServer,
                    request_deserializer=message__pb2.Request.FromString,
                    response_serializer=message__pb2.Response.SerializeToString,
            ),
            'InteractingStream': grpc.stream_stream_rpc_method_handler(
                    servicer.InteractingStream,
                    request_deserializer=message__pb2.Request.FromString,
                    response_serializer=message__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Grpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Grpc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ServerClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Grpc/ServerClient',
            message__pb2.Request.SerializeToString,
            message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientServer(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Grpc/ClientServer',
            message__pb2.Request.SerializeToString,
            message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InteractingStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Grpc/InteractingStream',
            message__pb2.Request.SerializeToString,
            message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)