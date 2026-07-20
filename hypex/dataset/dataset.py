from __future__ import annotations

import warnings
from collections.abc import Iterable
from copy import deepcopy
from typing import Any, Callable, Hashable, Literal, Sequence

import numpy as np
import pandas as pd  # type: ignore
from numpy import ndarray

from ..utils import (
    ID_SPLIT_SYMBOL,
    BackendsEnum,
    BackendTypeError,
    ConcatBackendError,
    ConcatDataError,
    DataTypeError,
    ExperimentDataEnum,
    FromDictTypes,
    MultiFieldKeyTypes,
    NotFoundInExperimentDataError,
    ScalarType,
)
from ..utils.adapter import Adapter
from ..utils.errors import InvalidArgumentError
from .abstract import DatasetBase
from .roles import (
    ABCRole,
    AdditionalRole,
    DefaultRole,
    FilterRole,
    InfoRole,
    StatisticRole,
)


class Dataset(DatasetBase):
    class Locker:
        def __init__(self, backend, roles):
            self.backend = backend
            self.roles = roles

        def __getitem__(self, item) -> Dataset:
            t_data = self.backend.loc(item)
            return Dataset(
                data=t_data,
                roles={k: v for k, v in self.roles.items() if k in t_data.columns},
            )

        def __setitem__(self, item, value):
            column_name = item[1]
            column_data_type = self.roles[column_name].data_type
            if (
                column_data_type is None
                or (
                    isinstance(value, Iterable)
                    and all(isinstance(v, column_data_type) for v in value)
                )
                or isinstance(value, column_data_type)
            ):
                if column_name not in self.backend.data.columns:
                    raise KeyError("Column must be added by using add_column method.")
                else:
                    self.backend.data.loc[item] = value
            else:
                raise TypeError("Value type does not match the expected data type.")

    class ILocker:
        def __init__(self, backend, roles):
            self.backend = backend
            self.roles = roles

        def __getitem__(self, item) -> Dataset:
            t_data = self.backend.iloc(item)
            return Dataset(
                data=t_data,
                roles={k: v for k, v in self.roles.items() if k in t_data.columns},
            )

        def __setitem__(self, item, value):
            column_index = item[1]
            column_name = self.backend.data.columns[column_index]
            column_data_type = self.roles[column_name].data_type
            if (
                column_data_type is None
                or (
                    isinstance(value, Iterable)
                    and all(isinstance(v, column_data_type) for v in value)
                )  # check for backend specific list (?)
                or isinstance(value, column_data_type)
            ):
                if column_index >= len(self.backend.data.columns):
                    raise IndexError("Column must be added by using add_column method.")
                else:
                    self.backend.data.iloc[item] = value
            else:
                raise TypeError("Value type does not match the expected data type.")

    def __init__(
        self,
        roles: dict[ABCRole, list[str] | str] | dict[str, ABCRole],
        data: pd.DataFrame | str | None = None,
        backend: BackendsEnum | None = None,
        default_role: ABCRole | None = None,
    ):
        super().__init__(roles, data, backend, default_role)
        self.loc = self.Locker(self._backend, self.roles)
        self.iloc = self.ILocker(self._backend, self.roles)

    def __getitem__(self, item: Iterable | str | int) -> Dataset:
        if isinstance(item, Dataset):
            item = item.data
        items = (
            [item] if isinstance(item, str) or not isinstance(item, Iterable) else item
        )
        roles: dict = {
            column: (
                self.roles[column]
                if column in self.columns and self.roles.get(column, False)
                else InfoRole()
            )
            for column in items
        }
        result = Dataset(data=self._backend.__getitem__(item), roles=roles)
        result.tmp_roles = {
            key: value for key, value in self.tmp_roles.items() if key in items
        }
        return result

    def __setitem__(self, key: str, value: Any):
        if isinstance(value, Dataset):
            value = value.data.iloc[:, 0]
        if key not in self.columns and isinstance(key, str):
            self.add_column(value, {key: InfoRole()})
            warnings.warn(
                "Column must be added by using add_column method.",
                category=SyntaxWarning,
            )
            self.data[key] = value
        else:
            column_data_type = self.roles[key].data_type
            if (
                column_data_type is None
                or (
                    isinstance(value, Iterable)
                    and all(isinstance(v, column_data_type) for v in value)
                )  # check for backend specific list (?)
                or isinstance(value, column_data_type)
            ):
                self.data[key] = value
            else:
                raise TypeError("Value type does not match the expected data type.")

    def __binary_magic_operator(self, other, func_name: str) -> Any:
        pass

    def __eq__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__eq__")

    def __ne__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__ne__")

    def __le__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__le__")

    def __lt__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__lt__")

    def __ge__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__ge__")

    def __gt__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__gt__")

    def __pos__(self):
        return Dataset(roles=self.roles, data=(+self._backend))

    def __neg__(self):
        return Dataset(roles=self.roles, data=(-self._backend))

    def __abs__(self):
        return Dataset(roles=self.roles, data=abs(self._backend))

    def __invert__(self):
        return Dataset(roles=self.roles, data=(~self._backend))

    def __round__(self, ndigits: int = 0):
        return Dataset(roles=self.roles, data=round(self._backend, ndigits))

    def __bool__(self):
        return not self._backend.is_empty()

    def __add__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__add__")

    def __sub__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__sub__")

    def __mul__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__mul__")

    def __floordiv__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__floordiv__")

    def __div__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__div__")

    def __truediv__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__truediv__")

    def __mod__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__mod__")

    def __pow__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__pow__")

    def __and__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__and__")

    def __or__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__or__")

    def __radd__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__radd__")

    def __rsub__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__rsub__")

    def __rmul__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__rmul__")

    def __rfloordiv__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__rfloordiv__")

    def __rdiv__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__rdiv__")

    def __rtruediv__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__rtruediv__")

    def __rmod__(self, other):
        return self.__binary_magic_operator(other=other, func_name="__rmod__")

    def __rpow__(self, other) -> Any:
        return self.__binary_magic_operator(other=other, func_name="__rpow__")

    @property
    def index(self):
        pass

    @index.setter
    def index(self, value):
        pass

    @property
    def data(self):
        pass

    @data.setter
    def data(self, value):
        pass

    @property
    def columns(self):
        pass

    @staticmethod
    def create_empty(roles=None, index=None, backend=BackendsEnum.pandas) -> Dataset:
        pass

    def _convert_data_after_agg(self, result) -> Dataset | float:
        pass

    def get(
        self,
        key,
        default=None,
    ) -> Dataset:
        pass

    def take(
        self,
        indices: int | list[int],
        axis: Literal["index", "columns", "rows"] | int = 0,
    ) -> Dataset:
        pass

    def add_column(
        self,
        data,
        role: dict[str, ABCRole] | None = None,
        index: Iterable[Hashable] | None = None,
    ):
        pass

    def _check_other_dataset(self, other):
        if not isinstance(other, Dataset):
            raise ConcatDataError(type(other))
        if type(other._backend) is not type(self._backend):
            raise ConcatBackendError(type(other._backend), type(self._backend))

    def astype(
        self, dtype: dict[str, type], errors: Literal["raise", "ignore"] = "raise"
    ) -> Dataset:
        pass

    def append(self, other, reset_index=False, axis=0) -> Dataset:
        other = Adapter.to_list(other)

        new_roles = deepcopy(self.roles)
        for o in other:
            self._check_other_dataset(o)
            new_roles.update(o.roles)

        return Dataset(
            roles=new_roles, data=self.backend.append(other, reset_index, axis)
        )

    @staticmethod
    def from_dict(
        data: FromDictTypes,
        roles: dict[ABCRole, list[str] | str] | dict[str, ABCRole],
        backend: BackendsEnum = BackendsEnum.pandas,
        index=None,
    ) -> Dataset:
        pass

    def apply(
        self,
        func: Callable,
        role: dict[str, ABCRole],
        axis: int = 0,
        **kwargs,
    ) -> Dataset:
        pass

    def map(self, func, na_action=None, **kwargs) -> Dataset:
        pass

    def is_empty(self) -> bool:
        pass

    def unique(self) -> dict[str, list[Any]]:
        pass

    def nunique(self, dropna: bool = False) -> dict[str, int]:
        pass

    def isin(self, values: Iterable) -> Dataset:
        pass

    def groupby(
        self,
        by: Any,
        func: str | list | None = None,
        fields_list: str | list | None = None,
        reset_index: bool = True,
        **kwargs,
    ) -> list[tuple[str, Dataset]]:
        pass

    def sort(
        self,
        by: MultiFieldKeyTypes | None = None,
        ascending: bool = True,
        **kwargs,
    ):
        pass

    def fillna(
        self,
        values: ScalarType | dict[str, ScalarType] | None = None,
        method: Literal["bfill", "ffill"] | None = None,
        **kwargs,
    ):
        pass

    def mean(self):
        pass

    def max(self):
        pass

    def reindex(self, labels, fill_value: Any | None = None) -> Dataset:
        pass

    def idxmax(self):
        pass

    def min(self):
        pass

    def count(self):
        pass

    def sum(self):
        pass

    def log(self):
        pass

    def mode(self, numeric_only: bool = False, dropna: bool = True):
        pass

    def var(self, skipna: bool = True, ddof: int = 1, numeric_only: bool = False):
        pass

    def agg(self, func: str | list):
        pass

    def std(self, skipna: bool = True, ddof: int = 1):
        pass

    def quantile(self, q: float = 0.5):
        pass

    def coefficient_of_variation(self):
        pass

    def corr(self, method="pearson", numeric_only=False):
        pass

    def value_counts(
        self,
        normalize: bool = False,
        sort: bool = True,
        ascending: bool = False,
        dropna: bool = True,
    ):
        pass

    def na_counts(self):
        pass

    def dropna(
        self,
        how: Literal["any", "all"] = "any",
        subset: str | Iterable[str] | None = None,
        axis: Literal["index", "rows", "columns"] | int = 0,
    ):
        pass

    def isna(self):
        pass

    def select_dtypes(self, include: Any = None, exclude: Any = None):
        pass

    def merge(
        self,
        right,
        on: str | None = None,
        left_on: str | None = None,
        right_on: str | None = None,
        left_index: bool = False,
        right_index: bool = False,
        suffixes: tuple[str, str] = ("_x", "_y"),
        how: Literal["left", "right", "outer", "inner", "cross"] = "inner",
    ):
        pass

    def drop(
        self,
        labels: str | None = None,
        axis: int | None = None,
        columns: str | Iterable[str] | None = None,
    ):
        pass

    def filter(
        self,
        items: list | None = None,
        like: str | None = None,
        regex: str | None = None,
        axis: int | None = None,
    ) -> Dataset:
        pass

    def dot(self, other: Dataset | ndarray) -> Dataset:
        pass

    def transpose(
        self,
        roles: dict[str, ABCRole] | list[str] | None = None,
    ) -> Dataset:
        pass

    def sample(
        self,
        frac: float | None = None,
        n: int | None = None,
        random_state: int | None = None,
    ) -> Dataset:
        pass

    def cov(self):
        pass

    def rename(self, names: dict[str, str]):
        pass

    def replace(
        self,
        to_replace: Any = None,
        value: Any = None,
        regex: bool = False,
    ) -> Dataset:
        pass

    def list_to_columns(self, column: str) -> Dataset:
        pass


class ExperimentData:
    def __init__(self, data: Dataset):
        self._data = data
        self.additional_fields = Dataset.create_empty(index=data.index)
        self.variables: dict[str, dict[str, int | float]] = {}
        self.groups: dict[str, dict[str, Dataset]] = {}
        self.analysis_tables: dict[str, Dataset] = {}
        self.id_name_mapping: dict[str, str] = {}

    @property
    def ds(self):
        pass

    @staticmethod
    def create_empty(
        roles=None, backend=BackendsEnum.pandas, index=None
    ) -> ExperimentData:
        pass

    def check_hash(self, executor_id: int, space: ExperimentDataEnum) -> bool:
        pass

    def set_value(
        self,
        space: ExperimentDataEnum,
        executor_id: str | dict[str, str],
        value: Any,
        key: str | None = None,
        role=None,
    ) -> ExperimentData:
        pass

    def get_ids(
        self,
        classes: type | Iterable[type] | str | Iterable[str],
        searched_space: ExperimentDataEnum | Iterable[ExperimentDataEnum] | None = None,
        key: str | None = None,
    ) -> dict[str, dict[str, list[str]]]:
        pass

    def get_one_id(
        self,
        class_: type | str,
        space: ExperimentDataEnum,
        key: str | None = None,
    ) -> str:
        pass

    def copy(self, data: Dataset | None = None) -> ExperimentData:
        pass

    def field_search(
        self,
        roles: ABCRole | Iterable[ABCRole],
        tmp_role: bool = False,
        search_types=None,
    ) -> list[str]:
        pass

    def field_data_search(
        self,
        roles: ABCRole | Iterable[ABCRole],
        tmp_role: bool = False,
        search_types=None,
    ) -> Dataset:
        pass


class DatasetAdapter(Adapter):
    @staticmethod
    def to_dataset(
        data: dict | Dataset | pd.DataFrame | list | str | int | float | bool,
        roles: ABCRole | dict[str, ABCRole],
    ) -> Dataset:
        pass

    @staticmethod
    def value_to_dataset(
        data: ScalarType, roles: ABCRole | dict[str, ABCRole]
    ) -> Dataset:
        pass

    @staticmethod
    def dict_to_dataset(data: dict, roles: ABCRole | dict[str, ABCRole]) -> Dataset:
        pass

    @staticmethod
    def list_to_dataset(data: list, roles: dict[str, ABCRole]) -> Dataset:
        pass

    @staticmethod
    def frame_to_dataset(data: pd.DataFrame, roles: dict[str, ABCRole]) -> Dataset:
        pass

    @staticmethod
    def ndarray_to_dataset(data: np.ndarray, roles: dict[str, ABCRole]) -> Dataset:
        pass
