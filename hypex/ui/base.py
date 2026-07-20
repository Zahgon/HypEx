from __future__ import annotations

from typing import Any

from ..dataset import Dataset, ExperimentData
from ..experiments.base import Experiment
from ..reporters import Reporter
from ..utils import ID_SPLIT_SYMBOL
from ..utils.enums import RenameEnum


class Output:

    resume: Dataset
    _experiment_data: ExperimentData

    def __init__(
        self,
        resume_reporter: Reporter,
        additional_reporters: dict[str, Reporter] | None = None,
    ):
        self.resume_reporter = resume_reporter
        self.additional_reporters = additional_reporters or {}

    def _extract_by_reporters(self, experiment_data: ExperimentData):
        pass

    @staticmethod
    def _replace_splitters(
        data: Dataset, mode: RenameEnum = RenameEnum.columns
    ) -> Dataset:
        pass

    def extract(self, experiment_data: ExperimentData):
        pass


class ExperimentShell:

    def __init__(
        self,
        experiment: Experiment,
        output: Output,
        experiment_params: dict[str, Any] | None = None,
    ):
        if experiment_params:
            experiment.set_params(experiment_params)
        self._out = output
        self._experiment = experiment

    @property
    def experiment(self):
        pass

    def execute(self, data: Dataset | ExperimentData) -> Output:
        pass
