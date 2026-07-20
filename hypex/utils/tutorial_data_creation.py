from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path("").absolute().parents[0]
sys.path.append(str(ROOT))


class DataGenerator:

    def __init__(
        self,
        n_samples=2000,
        distributions=None,
        time_correlations=None,
        effect_size=5.0,
        seed=None,
    ):
        self.n_samples = n_samples
        self.distributions = distributions or {
            "X1": {"type": "normal", "mean": 1, "std": 2},
            "X2": {"type": "bernoulli", "p": 0.4},
            "y0": {"type": "normal", "mean": 10, "std": 3},
        }
        self.time_correlations = time_correlations or {"X1": 0.7, "X2": 0.6, "y0": 0.8}
        self.effect_size = effect_size
        self.seed = seed
        np.random.seed(seed)

    def _generate_bernoulli_pair(self, p, rho):
        pass

    def _generate_correlated_pair(self, dist_type, params, rho, U_vector=0):
        pass

    def _generate_correlated_chain(self, params, rho, n_points, U=0):
        pass

    def generate(self):
        pass


def set_nans(
    data: pd.DataFrame,
    na_step: Sequence[int] | int | None = None,
    nan_cols: Sequence[str] | str | None = None,
) -> pd.DataFrame:
    pass


def create_test_data(
    num_users: int = 10000,
    na_step: Sequence[int] | int | None = None,
    nan_cols: Sequence[str] | str | None = None,
    file_name: str | None = None,
    exact_ATT: int = 100,
    rs=None,
):
    pass


def sigmoid(x: np.ndarray) -> np.ndarray:
    pass


def sigmoid_division(x, dependent_division=True) -> np.ndarray:
    pass


def gen_special_medicine_df(
    data_size=100, *, dependent_division=True, random_state=None
) -> pd.DataFrame:
    pass


def gen_oracle_df(
    data_size=8, *, dependent_division=True, factual_only=False, random_state=None
) -> pd.DataFrame:
    pass


def gen_control_variates_df(
    data_size=1000, *, dependent_division=True, random_state=None
) -> pd.DataFrame:
    pass
