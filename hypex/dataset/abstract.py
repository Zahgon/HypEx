from __future__ import annotations

import copy
import json  # type: ignore
from abc import ABC
from typing import Any, Iterable

import pandas as pd  # type: ignore

from ..utils import BackendsEnum, RoleColumnError
from .backends import PandasDataset
from .roles import ABCRole, DefaultRole, default_roles


def parse_roles(roles: dict) -> dict[str | int] | ABCRole:
    pass


class DatasetBase(ABC):
    @staticmethod
    def _select_backend_from_data(data):
        pass

    @staticmethod
    def _select_backend_from_str(data, backend):
        pass

    def _set_all_roles(self, roles):
        pass

    def _set_empty_types(self, roles):
        pass

    def __init__(
        self,
        roles: dict[ABCRole, list[str] | str] | dict[str, ABCRole],
        data: pd.DataFrame | str | None = None,
        backend: BackendsEnum | None = None,
        default_role: ABCRole | None = None,
    ):
        self._backend = (
            self._select_backend_from_str(data, backend)
            if backend
            else self._select_backend_from_data(data)
        )
        self.default_role = default_role
        roles = (
            parse_roles(roles)
            if any(isinstance(role, ABCRole) for role in roles.keys())
            else roles
        )
        if any(not isinstance(role, ABCRole) for role in roles.values()):
            raise TypeError("Roles must be instances of ABCRole type")
        if data is not None and any(
            i not in self._backend.columns for i in list(roles.keys())
        ):
            raise RoleColumnError(list(roles.keys()), self._backend.columns)
        if data is not None:
            roles = self._set_all_roles(roles)
            self._set_empty_types(roles)
        self._roles: dict[str, ABCRole] = roles
        self._tmp_roles: (
            dict[ABCRole, list[str] | str] | dict[list[str] | str] | ABCRole
        ) = {}

    def __repr__(self):
        return self.data.__repr__()

    def _repr_html_(self):
        pass

    def __len__(self):
        return self._backend.__len__()

    def search_columns(
        self,
        roles: ABCRole | Iterable[ABCRole],
        tmp_role=False,
        search_types: list | None = None,
    ) -> list[str]:
        pass

    def search_columns_by_type(
        self,
        search_types: list | type,
    ) -> list[str]:
        pass

    def replace_roles(
        self,
        new_roles_map: dict[ABCRole | str] | ABCRole,
        tmp_role: bool = False,
        auto_roles_types: bool = False,
    ):
        pass

    @property
    def index(self):
        pass

    @property
    def data(self):
        pass

    @property
    def roles(self):
        pass

    @roles.setter
    def roles(self, value):
        pass

    @data.setter
    def data(self, value):
        pass

    @property
    def columns(self):
        pass

    @property
    def shape(self):
        pass

    @property
    def tmp_roles(self):
        pass

    @tmp_roles.setter
    def tmp_roles(self, value):
        pass

    def to_dict(self):
        pass

    def to_numpy(self):
        pass

    def to_records(self):
        pass

    def to_json(self, filename: str | None = None):
        pass

    @property
    def backend(self):
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

    def _set_roles(
        self,
        new_roles_map: dict[ABCRole, list[str] | str] | dict[list[str] | str] | ABCRole,
        temp_role: bool = False,
    ):
        pass
