from __future__ import annotations

from typing import Any

from ..analyzers.matching import MatchingAnalyzer
from ..dataset import (
    AdditionalMatchingRole,
    Dataset,
    ExperimentData,
    GroupingRole,
    StatisticRole,
    TargetRole,
)
from ..reporters.matching import MatchingDictReporter, MatchingQualityDatasetReporter
from ..utils import ID_SPLIT_SYMBOL, MATCHING_INDEXES_SPLITTER_SYMBOL
from .base import Output


class MatchingOutput(Output):
    resume: Dataset
    full_data: Dataset
    quality_results: Dataset

    def __init__(self, searching_class: type = MatchingAnalyzer):
        super().__init__(
            resume_reporter=MatchingDictReporter(searching_class),
            additional_reporters=MatchingQualityDatasetReporter(),
        )

    def _extract_full_data(self, experiment_data: ExperimentData, indexes: Dataset):
        pass

    @staticmethod
    def _reformat_resume(resume: dict[str, Any]):
        pass

    @staticmethod
    def _collect_grouped_indexes(experiment_data, group) -> Dataset:
        pass

    def extract(self, experiment_data: ExperimentData):
        pass
