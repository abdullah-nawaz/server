from grpc_server_client.rpc.rpc_client import GRPCClient

client_types = {
    'GrpcClientConfigs': GRPCClient
}


def create_rpc_client(config):
    import grpc
    from grpc._cython.cygrpc import CompressionAlgorithm
    from grpc._cython.cygrpc import CompressionLevel

    # credentials = grpc.ssl_channel_credentials(
    #     root_certificates=load_cert_file("{}/server.crt".format(config.CERTS_PATH)),
    #     private_key=load_cert_file("{}/client.key".format(config.CERTS_PATH)),
    #     certificate_chain=load_cert_file("{}/client.crt".format(config.CERTS_PATH))
    # )
    channel = grpc.insecure_channel(
        config.GRPC_URL,
        # credentials,
        options=[
            ("grpc.max_send_message_length", config.GRPC_MAX_MESSAGE_SIZE),
            ("grpc.max_receive_message_length", config.GRPC_MAX_MESSAGE_SIZE),
            ("grpc.default_compression_algorithm", CompressionAlgorithm.gzip),
            ("grpc.default_compression_level", CompressionLevel.high),
        ],
    )
    grpc_client = client_types[config.__name__](channel)
    return grpc_client


__all__ = [
    "create_rpc_client"
]
