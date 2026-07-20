from __future__ import annotations

from typing import Literal

import numpy as np

from ..dataset import ABCRole, Dataset
from ..utils.constants import NUMBER_TYPES_LIST
from .abstract import Comparator

NUM_OF_BUCKETS = 10


class GroupDifference(Comparator):
    def __init__(
        self,
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ] = "groups",
        grouping_role: ABCRole | None = None,
        target_roles: ABCRole | list[ABCRole] | None = None,
    ):
        super().__init__(
            compare_by=compare_by,
            grouping_role=grouping_role,
            target_roles=target_roles,
        )

    @property
    def search_types(self) -> list[type] | None:
        pass

    @classmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        **kwargs,
    ) -> dict:
        pass


class GroupSizes(Comparator):
    def __init__(
        self,
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ] = "groups",
        grouping_role: ABCRole | None = None,
    ):
        super().__init__(
            compare_by=compare_by,
            grouping_role=grouping_role,
            target_roles=grouping_role,
        )

    @classmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> dict:
        pass


class PSI(Comparator):
    @classmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> dict[str, float]:
        pass
