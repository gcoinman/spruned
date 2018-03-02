from spruned.exceptions import SprunedException


class HeadersInconsistencyException(SprunedException):
    pass


class NoQuorumOnResponsesException(SprunedException):
    pass


class ConsistencyCheckRetryException(SprunedException):
    pass
