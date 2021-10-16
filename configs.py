import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class ClientConfigs:
    GRPC_MAX_MESSAGE_SIZE = 10 * 1000000
    CERTS_PATH = os.environ.get("CERTS_PATH", "{}/deployment/certs".format(BASEDIR))


class GrpcClientConfigs(ClientConfigs):
    GRPC_HOST = os.environ.get("ENV_GRPC_HOST", "mangos_gcp-rpc")
    GRPC_PORT = int(os.environ.get("ENV_GRPC_PORT", "50051"))
    GRPC_URL = "{}:{}".format(GRPC_HOST, GRPC_PORT)
