from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Iterable, Literal, Sequence, Sized

import numpy as np
import pandas as pd  # type: ignore

from ...utils import FromDictTypes, MergeOnError, ScalarType
from .abstract import DatasetBackendCalc, DatasetBackendNavigation


class PandasNavigation(DatasetBackendNavigation):
    @staticmethod
    def _read_file(filename: str | Path) -> pd.DataFrame:
        pass

    def __init__(self, data: pd.DataFrame | dict | str | pd.Series | None = None):
        if isinstance(data, pd.DataFrame):
            self.data = data
        elif isinstance(data, pd.Series):
            self.data = pd.DataFrame(data)
        elif isinstance(data, dict):
            if "index" in data.keys():
                self.data = pd.DataFrame(data=data["data"], index=data["index"])
            else:
                self.data = pd.DataFrame(data=data["data"])
        elif isinstance(data, str):
            self.data = self._read_file(data)
        else:
            self.data = pd.DataFrame()

    def __getitem__(self, item):
        if isinstance(item, (slice, int)):
            return self.data.iloc[item]
        if isinstance(item, (str, list)):
            return self.data[item]
        if isinstance(item, pd.DataFrame):
            if len(item.columns) == 1:
                return self.data[item.iloc[:, 0]]
            else:
                return self.data[item]
        raise KeyError("No such column or row")

    def __len__(self):
        return len(self.data)

    @staticmethod
    def __magic_determine_other(other) -> Any:
        pass

    def __eq__(self, other) -> Any:
        return self.data == self.__magic_determine_other(other)

    def __ne__(self, other) -> Any:
        return self.data != self.__magic_determine_other(other)

    def __le__(self, other) -> Any:
        return self.data <= self.__magic_determine_other(other)

    def __lt__(self, other) -> Any:
        return self.data < self.__magic_determine_other(other)

    def __ge__(self, other) -> Any:
        return self.data >= self.__magic_determine_other(other)

    def __gt__(self, other) -> Any:
        return self.data > self.__magic_determine_other(other)

    def __pos__(self) -> Any:
        return +self.data

    def __neg__(self) -> Any:
        return -self.data

    def __abs__(self) -> Any:
        return abs(self.data)

    def __invert__(self) -> Any:
        return ~self.data

    def __round__(self, ndigits: int = 0) -> Any:
        return round(self.data, ndigits)

    def __add__(self, other) -> Any:
        return self.data + self.__magic_determine_other(other)

    def __sub__(self, other) -> Any:
        return self.data - self.__magic_determine_other(other)

    def __mul__(self, other) -> Any:
        return self.data * self.__magic_determine_other(other)

    def __floordiv__(self, other) -> Any:
        return self.data // self.__magic_determine_other(other)

    def __div__(self, other) -> Any:
        return self.data / self.__magic_determine_other(other)

    def __truediv__(self, other) -> Any:
        return self.data / self.__magic_determine_other(other)

    def __mod__(self, other) -> Any:
        return self.data % self.__magic_determine_other(other)

    def __pow__(self, other) -> Any:
        return self.data ** self.__magic_determine_other(other)

    def __and__(self, other) -> Any:
        return self.data & self.__magic_determine_other(other)

    def __or__(self, other) -> Any:
        return self.data | self.__magic_determine_other(other)

    def __radd__(self, other) -> Any:
        return self.__magic_determine_other(other) + self.data

    def __rsub__(self, other) -> Any:
        return self.__magic_determine_other(other) - self.data

    def __rmul__(self, other) -> Any:
        return self.__magic_determine_other(other) * self.data

    def __rfloordiv__(self, other) -> Any:
        return self.__magic_determine_other(other) // self.data

    def __rdiv__(self, other) -> Any:
        return self.__magic_determine_other(other) / self.data

    def __rtruediv__(self, other) -> Any:
        return self.__magic_determine_other(other) / self.data

    def __rmod__(self, other) -> Any:
        return self.__magic_determine_other(other) % self.data

    def __rpow__(self, other) -> Any:
        return self.__magic_determine_other(other) ** self.data

    def __repr__(self):
        return self.data.__repr__()

    def _repr_html_(self):
        pass

    def create_empty(
        self,
        index: Iterable | None = None,
        columns: Iterable[str] | None = None,
    ):
        pass

    @property
    def index(self):
        pass

    @property
    def columns(self):
        pass

    @property
    def shape(self):
        pass

    def _get_column_index(
        self, column_name: Sequence[str] | str
    ) -> int | Sequence[int]:
        pass

    def get_column_type(self, column_name: str) -> type | None:
        pass

    def astype(
        self, dtype: dict[str, type], errors: Literal["raise", "ignore"] = "raise"
    ) -> pd.DataFrame:
        pass

    def update_column_type(self, column_name: str, type_name: type):
        pass

    def add_column(
        self,
        data: Sequence,
        name: str | list[str],
        index: Sequence | None = None,
    ):
        pass

    def append(self, other, reset_index: bool = False, axis: int = 0) -> pd.DataFrame:
        new_data = pd.concat([self.data] + [d.data for d in other], axis=axis)
        if reset_index:
            new_data = new_data.reset_index(drop=True)
        return new_data

    def from_dict(self, data: FromDictTypes, index: Iterable | Sized | None = None):
        pass

    def to_dict(self) -> dict[str, Any]:
        pass

    def to_records(self) -> list[dict]:
        pass

    def loc(self, items: Iterable) -> Iterable:
        pass

    def iloc(self, items: Iterable) -> Iterable:
        pass


class PandasDataset(PandasNavigation, DatasetBackendCalc):
    @staticmethod
    def _convert_agg_result(result):
        pass

    def __init__(self, data: pd.DataFrame | dict | str | pd.Series | None = None):
        super().__init__(data)

    def get(
        self,
        key,
        default=None,
    ) -> Any:
        pass

    def take(
        self,
        indices: int | list[int],
        axis: Literal["index", "columns", "rows"] | int = 0,
    ) -> Any:
        pass

    def get_values(
        self,
        row: str | None = None,
        column: str | None = None,
    ) -> Any:
        pass

    def iget_values(
        self,
        row: int | None = None,
        column: int | None = None,
    ) -> Any:
        pass

    def apply(self, func: Callable, **kwargs) -> pd.DataFrame:
        pass

    def map(self, func: Callable, **kwargs) -> pd.DataFrame:
        pass

    def is_empty(self) -> bool:
        pass

    def unique(self):
        pass

    def nunique(self, dropna: bool = True):
        pass

    def groupby(self, by: str | Iterable[str], **kwargs) -> list[tuple]:
        pass

    def agg(self, func: str | list, **kwargs) -> pd.DataFrame | float:
        pass

    def max(self) -> pd.DataFrame | float:
        pass

    def idxmax(self) -> pd.DataFrame | float:
        pass

    def min(self) -> pd.DataFrame | float:
        pass

    def count(self) -> pd.DataFrame | float:
        pass

    def sum(self) -> pd.DataFrame | float:
        pass

    def mean(self) -> pd.DataFrame | float:
        pass

    def mode(
        self, numeric_only: bool = False, dropna: bool = True
    ) -> pd.DataFrame | float:
        pass

    def var(
        self, skipna: bool = True, ddof: int = 1, numeric_only: bool = False
    ) -> pd.DataFrame | float:
        pass

    def log(self) -> pd.DataFrame:
        pass

    def std(self, skipna: bool = True, ddof: int = 1) -> pd.DataFrame | float:
        pass

    def cov(self):
        pass

    def quantile(self, q: float = 0.5) -> pd.DataFrame:
        pass

    def coefficient_of_variation(self) -> pd.DataFrame | float:
        pass

    def sort_index(self, ascending: bool = True, **kwargs) -> pd.DataFrame:
        pass

    def corr(
        self,
        method: Literal["pearson", "kendall", "spearman"] = "pearson",
        numeric_only: bool = False,
    ) -> pd.DataFrame | float:
        pass

    def isna(self) -> pd.DataFrame:
        pass

    def sort_values(
        self, by: str | list[str], ascending: bool = True, **kwargs
    ) -> pd.DataFrame:
        pass

    def value_counts(
        self,
        normalize: bool = False,
        sort: bool = True,
        ascending: bool = False,
        dropna: bool = True,
    ) -> pd.DataFrame:
        pass

    def fillna(
        self,
        values: ScalarType | dict[str, ScalarType] | None = None,
        method: Literal["bfill", "ffill"] | None = None,
        **kwargs,
    ) -> pd.DataFrame:
        pass

    def na_counts(self) -> pd.DataFrame | int:
        pass

    def dot(self, other: PandasDataset | np.ndarray) -> pd.DataFrame:
        pass

    def dropna(
        self,
        how: Literal["any", "all"] = "any",
        subset: str | Iterable[str] | None = None,
        axis: Literal["index", "rows", "columns"] | int = 0,
    ) -> pd.DataFrame:
        pass

    def transpose(self, names: Sequence[str] | None = None) -> pd.DataFrame:
        pass

    def sample(
        self,
        frac: float | None = None,
        n: int | None = None,
        random_state: int | None = None,
    ) -> pd.DataFrame:
        pass

    def select_dtypes(
        self,
        include: str | None = None,
        exclude: str | None = None,
    ) -> pd.DataFrame:
        pass

    def isin(self, values: Iterable) -> Iterable[bool]:
        pass

    def merge(
        self,
        right: PandasDataset,
        on: str | None = None,
        left_on: str | None = None,
        right_on: str | None = None,
        left_index: bool | None = None,
        right_index: bool | None = None,
        suffixes: tuple[str, str] = ("_x", "_y"),
        how: Literal["left", "right", "inner", "outer", "cross"] = "inner",
    ) -> pd.DataFrame:
        pass

    def drop(
        self,
        labels: str | None = None,
        axis: int | None = None,
        columns: str | Iterable[str] | None = None,
    ) -> pd.DataFrame:
        pass

    def filter(
        self,
        items: list | None = None,
        like: str | None = None,
        regex: str | None = None,
        axis: int = 0,
    ) -> pd.DataFrame:
        pass

    def rename(self, columns: dict[str, str]) -> pd.DataFrame:
        pass

    def replace(
        self, to_replace: Any = None, value: Any = None, regex: bool = False
    ) -> pd.DataFrame:
        pass

    def reindex(self, labels: str = "", fill_value: str | None = None) -> pd.DataFrame:
        pass

    def list_to_columns(self, column: str) -> pd.DataFrame:
        pass
