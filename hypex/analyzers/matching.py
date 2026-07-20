from ..dataset.dataset import DatasetAdapter, ExperimentData
from ..dataset.roles import StatisticRole
from ..executor.executor import Executor
from ..operators.operators import MatchingMetrics
from ..utils.enums import ExperimentDataEnum


class MatchingAnalyzer(Executor):
    def _set_value(self, data: ExperimentData, value, key=None) -> ExperimentData:
        pass

    def execute(self, data: ExperimentData):
        pass
