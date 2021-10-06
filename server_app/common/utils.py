import os


def init_sec_client():
    """
    INIT method for sec Client
    """
    from swagger_client import Configuration, ApiClient, DefaultApi

    configuration = Configuration()
    configuration.host = os.environ.get("SEC_LINK", "http://gcpwebsec:8001")
    return DefaultApi(ApiClient(configuration))
