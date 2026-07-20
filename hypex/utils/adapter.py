from __future__ import annotations

from typing import Any, Sequence


class Adapter:
    @staticmethod
    def to_list(data: Any) -> list:
        if data is None:
            return []
        if isinstance(data, str):
            return [data]
        return list(data) if isinstance(data, Sequence) else [data]

    @staticmethod
    def list_to_single(data: list) -> Any:
        pass
