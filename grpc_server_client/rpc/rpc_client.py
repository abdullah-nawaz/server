import grpc

from grpc_server_client.rpc.exceptions import GRPCError
from grpc_server_client.rpc.proto_files import rpc_responses_grpc_def_pb2, rpc_responses_grpc_def_pb2_grpc


class GRPCClient:

    def __init__(self, channel):
        self.stub = rpc_responses_grpc_def_pb2_grpc.ResponseCallsStub(channel)

    def get_users(self):
        message = rpc_responses_grpc_def_pb2.EmptyRequest()
        response = self.__execute(self.stub.get_users, message)
        return response.users

    def __execute(self, stub_method, message):
        try:
            response = stub_method(message)
        except grpc.RpcError as e:
            raise GRPCError(str(e))
        else:
            if response.status in {201, 200}:
                return response
