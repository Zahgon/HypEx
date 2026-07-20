from __future__ import annotations

from ..analyzers.ab import ABAnalyzer
from ..comparators import GroupDifference, GroupSizes
from ..dataset import Dataset, ExperimentData, InfoRole, StatisticRole, TreatmentRole
from ..reporters.ab import ABDatasetReporter
from ..utils import ID_SPLIT_SYMBOL, ExperimentDataEnum
from .base import Output


class CupacOutput:

    def __init__(self):
        self.variance_reductions: Dataset | None = None
        self.feature_importances: Dataset | None = None

    def __repr__(self) -> str:
        has_vr = self.variance_reductions is not None
        has_fi = self.feature_importances is not None

        if not has_vr and not has_fi:
            return "CupacOutput(no CUPAC data available)"

        parts = []
        if has_vr:
            n_targets = len(self.variance_reductions.data)
            parts.append(f"variance_reductions: {n_targets} target(s)")
        if has_fi:
            n_features = len(self.feature_importances.data)
            parts.append(f"feature_importances: {n_features} feature(s)")

        return f"CupacOutput({', '.join(parts)})"


class ABOutput(Output):
    multitest: Dataset | str
    sizes: Dataset
    cupac: CupacOutput

    def __init__(self):
        self._groups = []
        self.cupac = CupacOutput()
        super().__init__(resume_reporter=ABDatasetReporter())

    def _extract_multitest_result(self, experiment_data: ExperimentData):
        pass

    def _extract_differences(self, experiment_data: ExperimentData):
        pass

    def _extract_sizes(self, experiment_data: ExperimentData):
        pass

    def _extract_variance_reductions(self, experiment_data: ExperimentData):
        pass

    def _extract_feature_importances(self, experiment_data: ExperimentData):
        pass

    @property
    def variance_reduction_report(self) -> Dataset | str:
        pass

    def extract(self, experiment_data: ExperimentData):
        pass
