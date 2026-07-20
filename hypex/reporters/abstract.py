from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ..dataset import Dataset, ExperimentData
from ..dataset.roles import InfoRole, ReportRole, TreatmentRole
from ..utils import ID_SPLIT_SYMBOL, ExperimentDataEnum
from ..utils.errors import AbstractMethodError


class Reporter(ABC):
    @abstractmethod
    def report(self, data: ExperimentData):
        raise AbstractMethodError


class DictReporter(Reporter, ABC):
    def __init__(self, front=True):
        self.front = front

    @staticmethod
    def extract_from_one_row_dataset(data: Dataset) -> dict[str, Any]:
        pass

    def _extract_from_comparator(self, data: ExperimentData, comparator_id: str):
        pass

    def _extract_from_comparators(
        self, data: ExperimentData, comparator_ids: list[str]
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def report(self, data: ExperimentData) -> dict:
        raise AbstractMethodError


class OnDictReporter(Reporter, ABC):
    def __init__(self, dict_reporter: DictReporter) -> None:
        self.dict_reporter = dict_reporter


class DatasetReporter(OnDictReporter):
    def report(self, data: ExperimentData) -> dict[str, Dataset] | Dataset:
        pass

    @staticmethod
    def convert_to_dataset(data: dict) -> dict[str, Dataset] | Dataset:
        pass


class TestDictReporter(DictReporter):
    @staticmethod
    def _get_struct_dict(data: dict):
        pass

    @staticmethod
    def _convert_struct_dict_to_dataset(data: dict) -> Dataset:
        pass

    def extract_tests(self, data: ExperimentData) -> dict[str, Any]:
        pass
