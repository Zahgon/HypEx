import numpy as np
import pandas as pd  # type: ignore

from ..dataset import Dataset
from ..dataset.roles import FeatureRole
from .abstract import Extension


class CholeskyExtension(Extension):
    def _calc_pandas(self, data: Dataset, epsilon: float = 1e-3, **kwargs):
        pass


class InverseExtension(Extension):
    def _calc_pandas(self, data: Dataset, **kwargs):
        pass
