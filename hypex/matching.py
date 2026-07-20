from __future__ import annotations

from typing import Literal

from .analyzers.matching import MatchingAnalyzer
from .comparators import Chi2Test, KSTest, TTest
from .comparators.distances import MahalanobisDistance
from .dataset import AdditionalMatchingRole, FeatureRole, TargetRole, TreatmentRole
from .encoders.encoders import DummyEncoder
from .executor import Executor
from .experiments import GroupExperiment
from .experiments.base import Experiment, OnRoleExperiment
from .ml.faiss import FaissNearestNeighbors
from .operators.operators import Bias, MatchingMetrics
from .reporters.matching import MatchingDatasetReporter
from .transformers import TypeCaster
from .ui.base import ExperimentShell
from .ui.matching import MatchingOutput


class Matching(ExperimentShell):

    @staticmethod
    def _make_experiment(
        group_match: bool = False,
        distance: Literal["mahalanobis", "l2"] = "mahalanobis",
        metric: Literal["atc", "att", "ate"] = "ate",
        bias_estimation: bool = True,
        quality_tests: (
            Literal["smd", "psi", "ks-test", "repeats", "t-test", "chi2-test", "auto"]
            | list[
                Literal[
                    "smd", "psi", "ks-test", "repeats", "t-test", "chi2-test", "auto"
                ]
            ]
        ) = "auto",
        faiss_mode: Literal["base", "fast", "auto"] = "auto",
        n_neighbors: int = 1,
        weights: dict[str, float] | None = None,
        encode_categories: bool = True,
    ) -> Experiment:
        pass

    def __init__(
        self,
        group_match: bool = False,
        distance: Literal["mahalanobis", "l2"] = "mahalanobis",
        bias_estimation: bool = True,
        quality_tests: (
            Literal["smd", "psi", "ks-test", "repeats", "t-test", "chi2-test", "auto"]
            | list[
                Literal[
                    "smd", "psi", "ks-test", "repeats", "t-test", "chi2-test", "auto"
                ]
            ]
        ) = "auto",
        faiss_mode: Literal["base", "fast", "auto"] = "auto",
        n_neighbors: int = 1,
        weights: dict[str, float] | None = None,
        encode_categories: bool = True,
    ):
        metric = "ate"
        super().__init__(
            experiment=self._make_experiment(
                group_match,
                distance,
                metric,
                bias_estimation,
                quality_tests,
                faiss_mode,
                n_neighbors,
                weights,
                encode_categories,
            ),
            output=MatchingOutput(GroupExperiment if group_match else MatchingAnalyzer),
        )
