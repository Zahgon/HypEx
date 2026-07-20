from __future__ import annotations

from typing import Any, ClassVar

from ..analyzers.ab import ABAnalyzer
from ..comparators import Chi2Test, KSTest, TTest, UTest
from ..dataset import Dataset, ExperimentData, StatisticRole
from ..utils import ExperimentDataEnum
from .aa import OneAADictReporter


class ABDictReporter(OneAADictReporter):
    tests: ClassVar[list] = [TTest, KSTest, UTest, Chi2Test]

    def extract_analyzer_data(self, data: ExperimentData) -> dict[str, Any]:
        pass

    def extract_data_from_analysis_tables(self, data: ExperimentData) -> dict[str, Any]:
        pass

    def report(self, data: ExperimentData) -> dict[str, Any]:
        pass


class ABDatasetReporter(ABDictReporter):
    @staticmethod
    def _invert_aa_format(table: Dataset) -> Dataset:
        pass

    def report_variance_reductions(self, data: ExperimentData) -> Dataset | str:
        pass

    def report(self, data: ExperimentData):
        pass
