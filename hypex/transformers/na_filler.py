from __future__ import annotations

from typing import Any, Literal, Sequence

from ..dataset.dataset import Dataset, ExperimentData
from ..dataset.roles import FeatureRole
from ..utils import ScalarType
from ..utils.adapter import Adapter
from .abstract import Transformer


class NaFiller(Transformer):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        values: ScalarType | dict[str, ScalarType] | None = None,
        method: Literal["bfill", "ffill"] | None = None,
        key: Any = "",
    ):
        """
        Initializes a NaFiller object.

        Args:
            target_roles (Optional[Union[str, Sequence[str]]], optional): The roles of the target columns. Defaults to None.
            key (Any, optional): The key for the NaFiller object. Defaults to "".
            values (Union[ScalarType, Dict[str, ScalarType]], optional): The values to fill missing values with. Defaults to None.
            method (Literal["bfill", "ffill"], optional): The method to fill missing values. Defaults to None.

        Returns:
            None
        """

        super().__init__(key=key)
        self.target_roles = target_roles or FeatureRole()
        self.values = values
        self.method = method

    @staticmethod
    def _inner_function(
        data: Dataset,
        target_cols: str | None = None,
        values: ScalarType | dict[str, ScalarType] | None = None,
        method: Literal["bfill", "ffill"] | None = None,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
