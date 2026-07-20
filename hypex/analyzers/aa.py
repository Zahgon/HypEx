from __future__ import annotations

from typing import Any, ClassVar

import numpy as np

from ..comparators import Chi2Test, KSTest, TTest
from ..dataset import Dataset, ExperimentData, StatisticRole
from ..executor import Executor
from ..experiments.base_complex import IfParamsExperiment, ParamsExperiment
from ..reporters.aa import OneAADictReporter
from ..splitters import AASplitter, AASplitterWithStratification
from ..utils import ID_SPLIT_SYMBOL, BackendsEnum, ExperimentDataEnum


class OneAAStatAnalyzer(Executor):
    def _set_value(self, data: ExperimentData, value, key=None) -> ExperimentData:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class AAScoreAnalyzer(Executor):
    AA_SPLITER_CLASS_MAPPING: ClassVar[dict] = {
        class_.__name__: class_ for class_ in [AASplitter, AASplitterWithStratification]
    }

    def __init__(self, alpha: float = 0.05, key: str = ""):
        super().__init__(key=key)
        self.alpha = alpha
        self.__feature_weights = {}
        self.threshold = 1 - (self.alpha * 1.2)

    def _set_value(
        self, data: ExperimentData, value: Any, key: Any = None
    ) -> ExperimentData:
        pass

    def _analyze_aa_score(
        self, data: ExperimentData, score_table: Dataset
    ) -> ExperimentData:
        pass

    def build_splitter_from_id(self, splitter_id: str):
        pass

    def _get_best_split(
        self,
        data: ExperimentData,
        score_table: Dataset,
        if_param_scores: Dataset | None = None,
    ) -> dict[str, Any]:
        pass

    def _set_best_split(
        self,
        data: ExperimentData,
        best_splitter_id: str,
    ) -> ExperimentData:
        pass

    def _analyze_best_split(
        self,
        data: ExperimentData,
        score_table: Dataset,
        if_param_scores: Dataset | None = None,
    ) -> ExperimentData:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
