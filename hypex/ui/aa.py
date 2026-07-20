from ..analyzers.aa import AAScoreAnalyzer
from ..dataset import Dataset, ExperimentData
from ..reporters.aa import AABestSplitReporter, AAPassedReporter
from ..utils import ExperimentDataEnum
from ..utils.enums import RenameEnum
from .base import Output


class AAOutput(Output):
    best_split: Dataset
    experiments: Dataset
    aa_score: Dataset
    best_split_statistic: Dataset

    def __init__(self):
        super().__init__(
            resume_reporter=AAPassedReporter(),
            additional_reporters={"best_split": AABestSplitReporter()},
        )

    def _extract_experiments(self, experiment_data: ExperimentData):
        pass

    def _extract_aa_score(self, experiment_data: ExperimentData):
        pass

    def extract(self, experiment_data: ExperimentData):
        pass
