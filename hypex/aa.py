from __future__ import annotations

import warnings
from typing import Any, Iterable

from .analyzers.aa import AAScoreAnalyzer, OneAAStatAnalyzer
from .comparators import GroupDifference, GroupSizes
from .comparators.abstract import Comparator
from .comparators.hypothesis_testing import Chi2Test, KSTest, TTest
from .dataset import AdditionalTreatmentRole, TargetRole
from .experiments.base import Experiment, OnRoleExperiment
from .experiments.base_complex import IfParamsExperiment, ParamsExperiment
from .forks.aa import IfAAExecutor
from .reporters import DatasetReporter
from .reporters.aa import OneAADictReporter
from .splitters import AASplitter, AASplitterWithStratification
from .ui.aa import AAOutput
from .ui.base import ExperimentShell
from .utils import SpaceEnum

AA_METRICS = Experiment(
    executors=[
        GroupSizes(grouping_role=AdditionalTreatmentRole()),
        OnRoleExperiment(
            executors=[
                GroupDifference(
                    compare_by="groups", grouping_role=AdditionalTreatmentRole()
                ),
                TTest(compare_by="groups", grouping_role=AdditionalTreatmentRole()),
                KSTest(compare_by="groups", grouping_role=AdditionalTreatmentRole()),
                Chi2Test(compare_by="groups", grouping_role=AdditionalTreatmentRole()),
            ],
            role=TargetRole(),
        ),
        OneAAStatAnalyzer(),
    ]
)

ONE_AA_TEST = Experiment(executors=[AASplitter(), AA_METRICS])
ONE_AA_TEST_WITH_STRATIFICATION = Experiment(
    executors=[AASplitterWithStratification(), AA_METRICS]
)

AA_TEST = Experiment(
    [
        ParamsExperiment(
            executors=([ONE_AA_TEST]),
            params={
                AASplitter: {"random_state": range(2000), "control_size": [0.5]},
                Comparator: {
                    "grouping_role": [AdditionalTreatmentRole()],
                    "space": [SpaceEnum.additional],
                },
            },
            reporter=DatasetReporter(OneAADictReporter(front=False)),
        ),
        AAScoreAnalyzer(),
    ],
    key="AATest",
)
AA_TEST_WITH_STRATIFICATION = Experiment(
    [
        ParamsExperiment(
            executors=([ONE_AA_TEST_WITH_STRATIFICATION]),
            params={
                AASplitter: {"random_state": range(2000), "control_size": [0.5]},
                Comparator: {
                    "grouping_role": [AdditionalTreatmentRole()],
                    "space": [SpaceEnum.additional],
                },
            },
            reporter=DatasetReporter(OneAADictReporter(front=False)),
        ),
        AAScoreAnalyzer(),
    ],
    key="AATest",
)


class AATest(ExperimentShell):

    @staticmethod
    def _prepare_params(
        n_iterations: int,
        control_size: float,
        random_states: Iterable[int] | None = None,
        sample_size: float | None = None,
        additional_params: dict[str, Any] | None = None,
        groups_sizes: list[float] | None = None,
    ) -> dict[type, dict[str, Any]]:
        pass

    def __init__(
        self,
        precision_mode: bool = False,
        control_size: float = 0.5,
        stratification: bool = False,
        n_iterations: int | None = None,
        sample_size: float | None = None,
        additional_params: dict[str, Any] | None = None,
        random_states: Iterable[int] | None = None,
        equal_variance: bool | None = None,
        groups_sizes: list[float] | None = None,
        **kwargs,
    ):
        if "t_test_equal_var" in kwargs:
            warnings.warn(
                "t_test_equal_var is deprecated and will be removed in a future version. "
                "Use equal_variance instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            if equal_variance is None:
                equal_variance = kwargs.pop("t_test_equal_var")
        if n_iterations is None:
            if precision_mode:
                n_iterations = 2000
            else:
                n_iterations = 10
        experiment_params = [
            ParamsExperiment(
                executors=(
                    [ONE_AA_TEST_WITH_STRATIFICATION if stratification else ONE_AA_TEST]
                ),
                params=self._prepare_params(
                    n_iterations,
                    control_size,
                    random_states,
                    sample_size,
                    additional_params,
                    groups_sizes,
                ),
                reporter=DatasetReporter(OneAADictReporter(front=False)),
            )
        ]
        if sample_size:
            experiment_params.append(
                IfParamsExperiment(
                    executors=(
                        [
                            (
                                ONE_AA_TEST_WITH_STRATIFICATION
                                if stratification
                                else ONE_AA_TEST
                            )
                        ]
                    ),
                    params=self._prepare_params(
                        n_iterations,
                        control_size,
                        random_states,
                        additional_params,
                        groups_sizes,
                    ),
                    reporter=DatasetReporter(OneAADictReporter(front=False)),
                    stopping_criterion=IfAAExecutor(sample_size=sample_size),
                )
            )
        experiment_params.append(AAScoreAnalyzer())
        super().__init__(
            experiment=Experiment(
                experiment_params,
                key="AATest",
            ),
            output=AAOutput(),
        )
        if equal_variance is not None:
            self.experiment.set_params(
                {TTest: {"calc_kwargs": {"equal_var": equal_variance}}}
            )
        else:
            self.experiment.set_params(
                {TTest: {"calc_kwargs": {"equal_var": False}}}
            )
