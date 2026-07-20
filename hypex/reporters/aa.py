from __future__ import annotations

import contextlib
from typing import Any, ClassVar

from ..comparators import Chi2Test, GroupDifference, GroupSizes, KSTest, TTest
from ..dataset import Dataset, ExperimentData, InfoRole, StatisticRole
from ..splitters import AASplitter, AASplitterWithStratification
from ..utils import ID_SPLIT_SYMBOL, ExperimentDataEnum, NotFoundInExperimentDataError
from .abstract import Reporter, TestDictReporter


class OneAADictReporter(TestDictReporter):
    tests: ClassVar[list] = [TTest, KSTest, Chi2Test]

    @staticmethod
    def convert_flat_dataset(data: dict) -> Dataset:
        pass

    @staticmethod
    def get_splitter_id(data: ExperimentData):
        pass

    def extract_group_difference(self, data: ExperimentData) -> dict[str, Any]:
        pass

    def extract_group_sizes(self, data: ExperimentData) -> dict[str, Any]:
        pass

    def extract_analyzer_data(self, data: ExperimentData) -> dict[str, Any]:
        pass

    def extract_data_from_analysis_tables(self, data: ExperimentData) -> dict[str, Any]:
        pass

    def report(self, data: ExperimentData) -> dict[str, Any]:
        pass


class AADatasetReporter(OneAADictReporter):
    def report(self, data: ExperimentData):
        pass


class AAPassedReporter(Reporter):
    @staticmethod
    def _reformat_aa_score_table(table: Dataset) -> Dataset:
        pass

    @staticmethod
    def _reformat_best_split_table(table: Dataset) -> Dataset:
        pass

    def _detect_pass(self, analyzer_tables: dict[str, Dataset]):
        pass

    def report(self, data: ExperimentData) -> Dataset:
        pass


class AABestSplitReporter(Reporter):
    def report(self, data: ExperimentData):
        pass
