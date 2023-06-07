import dataclasses
from typing import List

from Field import Field


class QueryResult:
    def __init__(self, outputs: List[Field]):
        self.outputs: List[Field] = outputs
