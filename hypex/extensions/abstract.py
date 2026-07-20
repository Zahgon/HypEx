from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Literal

from ..dataset import ABCRole, Dataset
from ..dataset.backends import PandasDataset
from ..dataset.dataset import DatasetAdapter
from ..utils.errors import AbstractMethodError


class Extension(ABC):
    def __init__(self):
        self.BACKEND_MAPPING = {
            PandasDataset: self._calc_pandas,
        }

    @abstractmethod
    def _calc_pandas(self, data: Dataset, **kwargs):
        raise AbstractMethodError

    def calc(self, data: Dataset, **kwargs):
        pass

    @staticmethod
    def result_to_dataset(result: Any, roles: ABCRole | dict[str, ABCRole]) -> Dataset:
        pass


class CompareExtension(Extension, ABC):
    def calc(self, data: Dataset, other: Dataset | None = None, **kwargs):
        pass


class MLExtension(Extension):
    def _calc_pandas(
        self,
        data: Dataset,
        mode: Literal["auto", "fit", "predict"] | None = None,
        **kwargs,
    ):
        pass

    @abstractmethod
    def fit(self, X, Y=None, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def predict(self, X, **kwargs):
        raise NotImplementedError

    def calc(
        self,
        data: Dataset,
        **kwargs,
    ):
        pass
