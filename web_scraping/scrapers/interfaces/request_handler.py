from typing import Protocol


class RequestHandler(Protocol):
    def send_request(self): ...
