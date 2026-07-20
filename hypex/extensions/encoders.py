from __future__ import annotations

import copy

import pandas as pd  # type: ignore

from ..dataset import Dataset, DatasetAdapter
from .abstract import Extension


class DummyEncoderExtension(
    Extension
):  # TODO: role types are being rewritten, needs to be fixed
    @staticmethod
    def _calc_pandas(data: Dataset, target_cols: str | None = None, **kwargs):
        pass
