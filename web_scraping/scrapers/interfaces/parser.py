from typing import Protocol


class Parser(Protocol):
    def parse_data(self): ...
