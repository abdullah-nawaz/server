class GRPCError(Exception):
    """ Exception raised when an error related to GRPC is raised"""

    def __init__(self, error):
        self.msg = error
        super(GRPCError, self).__init__(self.msg)
