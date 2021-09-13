# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from src.comms import hdcomm_pb2 as hdcomm__pb2


class HdCommStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Move = channel.unary_unary(
                '/hdcomm.HdComm/Move',
                request_serializer=hdcomm__pb2.MoveRequest.SerializeToString,
                response_deserializer=hdcomm__pb2.MoveResponse.FromString,
                )
        self.MoveCancel = channel.unary_unary(
                '/hdcomm.HdComm/MoveCancel',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Ping = channel.unary_unary(
                '/hdcomm.HdComm/Ping',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=hdcomm__pb2.PingResponse.FromString,
                )
        self.GetRadii = channel.unary_unary(
                '/hdcomm.HdComm/GetRadii',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=hdcomm__pb2.RadiiResponse.FromString,
                )
        self.GetHeading = channel.unary_unary(
                '/hdcomm.HdComm/GetHeading',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=hdcomm__pb2.HeadingResponse.FromString,
                )
        self.GetFrontDistance = channel.unary_unary(
                '/hdcomm.HdComm/GetFrontDistance',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=hdcomm__pb2.FrontDistanceResponse.FromString,
                )


class HdCommServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Move(self, request, context):
        """Commands the robot to move.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveCancel(self, request, context):
        """Commands the robot to abort an ongoing move.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Pings the robot.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRadii(self, request, context):
        """Obtain a list of available turn radii.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHeading(self, request, context):
        """Obtain the robot's heading.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFrontDistance(self, request, context):
        """Obtain the front distance sensor's reading.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HdCommServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Move': grpc.unary_unary_rpc_method_handler(
                    servicer.Move,
                    request_deserializer=hdcomm__pb2.MoveRequest.FromString,
                    response_serializer=hdcomm__pb2.MoveResponse.SerializeToString,
            ),
            'MoveCancel': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveCancel,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=hdcomm__pb2.PingResponse.SerializeToString,
            ),
            'GetRadii': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRadii,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=hdcomm__pb2.RadiiResponse.SerializeToString,
            ),
            'GetHeading': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHeading,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=hdcomm__pb2.HeadingResponse.SerializeToString,
            ),
            'GetFrontDistance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFrontDistance,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=hdcomm__pb2.FrontDistanceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hdcomm.HdComm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HdComm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Move(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hdcomm.HdComm/Move',
            hdcomm__pb2.MoveRequest.SerializeToString,
            hdcomm__pb2.MoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveCancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hdcomm.HdComm/MoveCancel',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hdcomm.HdComm/Ping',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            hdcomm__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRadii(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hdcomm.HdComm/GetRadii',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            hdcomm__pb2.RadiiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHeading(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hdcomm.HdComm/GetHeading',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            hdcomm__pb2.HeadingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFrontDistance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hdcomm.HdComm/GetFrontDistance',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            hdcomm__pb2.FrontDistanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
