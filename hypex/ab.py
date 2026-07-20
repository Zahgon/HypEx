from __future__ import annotations

import warnings
from typing import Literal

from .analyzers.ab import ABAnalyzer
from .comparators import Chi2Test, GroupDifference, GroupSizes, KSTest, TTest, UTest
from .dataset import AdditionalTargetRole, TargetRole, TreatmentRole
from .executor.executor import Executor
from .experiments.base import Experiment, OnRoleExperiment
from .transformers import CUPEDTransformer
from .ui.ab import ABOutput
from .ui.base import ExperimentShell
from .utils import ABNTestMethodsEnum, ABTestTypesEnum


class ABTest(ExperimentShell):

    @staticmethod
    def _make_experiment(
        additional_tests: str | ABTestTypesEnum | list[str | ABTestTypesEnum] | None,
        multitest_method: ABNTestMethodsEnum | str | None,
        cuped_features: dict[str, str] | None,
        cupac_models: str | list[str] | None,
        enable_cupac: bool,
    ) -> Experiment:
        pass

    def __init__(
        self,
        additional_tests: (
            str | ABTestTypesEnum | list[str | ABTestTypesEnum] | None
        ) = None,
        multitest_method: (
            Literal[
                "bonferroni",
                "sidak",
                "holm-sidak",
                "holm",
                "simes-hochberg",
                "hommel",
                "fdr_bh",
                "fdr_by",
                "fdr_tsbh",
                "fdr_tsbhy",
                "quantile",
            ]
            | None
        ) = "holm",
        equal_variance: bool | None = None,
        cuped_features: dict[str, str] | None = None,
        cupac_models: str | list[str] | None = None,
        enable_cupac: bool = False,
        **kwargs,
    ):
        """
        Args:
            additional_tests: Statistical test(s) to run in addition to the default group difference calculation. Valid options are 't-test', 'u-test', 'chi2-test' or ABTestTypesEnum.t_test, ABTestTypesEnum.u_test, and ABTestTypesEnum.chi2_test. Can be a single test name/enum or list of test names/enums. Defaults to [ABTestTypesEnum.t_test].
            multitest_method: Method to use for multiple testing correction. Valid options are ABNTestMethodsEnum.bonferroni, ABNTestMethodsEnum.sidak, etc. Defaults to ABNTestMethodsEnum.holm.
            equal_variance: Whether to use equal variance in t-test (optional).
            cuped_features: dict[str, str] — Dictionary {target_feature: pre_target_feature} for CUPED. Only dict is allowed.
            cupac_models: str | list[str] — model name (e.g. 'linear', 'ridge', 'lasso', 'catboost') or list of model names to try. If None, all available models will be tried and the best will be selected by variance reduction.
            enable_cupac: bool — Enable CUPAC variance reduction. CUPAC configuration is extracted from dataset.features_mapping.
        """
        if "t_test_equal_var" in kwargs:
            warnings.warn(
                "t_test_equal_var is deprecated and will be removed in a future version. "
                "Use equal_variance instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            if equal_variance is None:
                equal_variance = kwargs.pop("t_test_equal_var")
        super().__init__(
            experiment=self._make_experiment(
                additional_tests,
                multitest_method,
                cuped_features,
                cupac_models,
                enable_cupac,
            ),
            output=ABOutput(),
        )
        if equal_variance is not None:
            self.experiment.set_params(
                {TTest: {"calc_kwargs": {"equal_var": equal_variance}}}
            )
        else:
            self.experiment.set_params(
                {TTest: {"calc_kwargs": {"equal_var": False}}}
            )
