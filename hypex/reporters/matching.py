from __future__ import annotations

from typing import Any, ClassVar

from ..analyzers.matching import MatchingAnalyzer
from ..comparators import Chi2Test, KSTest, TTest
from ..dataset import Dataset, ExperimentData
from ..ml import FaissNearestNeighbors
from ..reporters.abstract import DatasetReporter, DictReporter, TestDictReporter
from ..utils import (
    ID_SPLIT_SYMBOL,
    MATCHING_INDEXES_SPLITTER_SYMBOL,
    ExperimentDataEnum,
)


class MatchingDictReporter(DictReporter):
    def __init__(self, searching_class: type = MatchingAnalyzer):
        self.searching_class = searching_class
        super().__init__()

    @staticmethod
    def _convert_dataset_to_dict(data: Dataset) -> dict[str, Any]:
        pass

    def _extract_from_analyser(self, data: ExperimentData):
        pass

    @staticmethod
    def _extract_from_additional_fields(data: ExperimentData):
        pass

    def report(self, experiment_data: ExperimentData):
        pass


class MatchingQualityDictReporter(TestDictReporter):
    tests: ClassVar[list] = [TTest, KSTest, Chi2Test]

    def report(self, data: ExperimentData) -> dict[str, Any]:
        pass


class MatchingQualityDatasetReporter(MatchingQualityDictReporter):
    @classmethod
    def convert_flat_dataset(cls, data: dict) -> Dataset:
        pass

    def report(self, data: ExperimentData):
        pass


class MatchingDatasetReporter(DatasetReporter):
    def __init__(self, searching_class: type = MatchingAnalyzer) -> None:
        self.dict_reporter = MatchingDictReporter(searching_class)
        super().__init__(self.dict_reporter)
