# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yeying.api.asset import recycle_pb2 as yeying_dot_api_dot_asset_dot_recycle__pb2


class RecycleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/yeying.api.asset.Recycle/Search',
                request_serializer=yeying_dot_api_dot_asset_dot_recycle__pb2.SearchDeletedAssetRequest.SerializeToString,
                response_deserializer=yeying_dot_api_dot_asset_dot_recycle__pb2.SearchDeletedAssetResponse.FromString,
                )
        self.Recover = channel.unary_unary(
                '/yeying.api.asset.Recycle/Recover',
                request_serializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RecoverDeletedAssetRequest.SerializeToString,
                response_deserializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RecoverDeletedAssetResponse.FromString,
                )
        self.Remove = channel.unary_unary(
                '/yeying.api.asset.Recycle/Remove',
                request_serializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RemoveDeletedAssetRequest.SerializeToString,
                response_deserializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RemoveDeletedAssetResponse.FromString,
                )


class RecycleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Search(self, request, context):
        """*
        从回收站里搜索资产
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recover(self, request, context):
        """*
        从回收站里恢复资产
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """*
        从回收站里删除资产
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecycleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=yeying_dot_api_dot_asset_dot_recycle__pb2.SearchDeletedAssetRequest.FromString,
                    response_serializer=yeying_dot_api_dot_asset_dot_recycle__pb2.SearchDeletedAssetResponse.SerializeToString,
            ),
            'Recover': grpc.unary_unary_rpc_method_handler(
                    servicer.Recover,
                    request_deserializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RecoverDeletedAssetRequest.FromString,
                    response_serializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RecoverDeletedAssetResponse.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RemoveDeletedAssetRequest.FromString,
                    response_serializer=yeying_dot_api_dot_asset_dot_recycle__pb2.RemoveDeletedAssetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yeying.api.asset.Recycle', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recycle(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yeying.api.asset.Recycle/Search',
            yeying_dot_api_dot_asset_dot_recycle__pb2.SearchDeletedAssetRequest.SerializeToString,
            yeying_dot_api_dot_asset_dot_recycle__pb2.SearchDeletedAssetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Recover(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yeying.api.asset.Recycle/Recover',
            yeying_dot_api_dot_asset_dot_recycle__pb2.RecoverDeletedAssetRequest.SerializeToString,
            yeying_dot_api_dot_asset_dot_recycle__pb2.RecoverDeletedAssetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yeying.api.asset.Recycle/Remove',
            yeying_dot_api_dot_asset_dot_recycle__pb2.RemoveDeletedAssetRequest.SerializeToString,
            yeying_dot_api_dot_asset_dot_recycle__pb2.RemoveDeletedAssetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
