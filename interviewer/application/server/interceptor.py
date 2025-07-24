import logging
from typing import Callable, Awaitable

import grpc


class SignatureInterceptor(grpc.aio.ServerInterceptor):
    """目前还无法做到签名，拿不到请求信息，reference：https://github.com/grpc/grpc/tree/master/examples

    """

    def __init__(self, identity) -> None:
        self.identity = identity

    async def intercept_service(
            self,
            continuation: Callable[[grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]],
            handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler:
        """可以作统计分析，以及重入问题
        """
        logging.info(
            f'Request metadata={handler_call_details.invocation_metadata}, method={handler_call_details.method}')
        return await continuation(handler_call_details)
