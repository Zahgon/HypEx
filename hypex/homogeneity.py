from .analyzers.aa import OneAAStatAnalyzer
from .comparators import Chi2Test, GroupDifference, GroupSizes, KSTest, TTest
from .dataset import TargetRole, TreatmentRole
from .experiments.base import Experiment, OnRoleExperiment
from .ui.base import ExperimentShell
from .ui.homo import HomoOutput

HOMOGENEITY_TEST = Experiment(
    executors=[
        OnRoleExperiment(
            executors=[
                GroupSizes(grouping_role=TreatmentRole(), compare_by="groups"),
                GroupDifference(grouping_role=TreatmentRole(), compare_by="groups"),
                TTest(grouping_role=TreatmentRole(), compare_by="groups"),
                KSTest(grouping_role=TreatmentRole(), compare_by="groups"),
                Chi2Test(grouping_role=TreatmentRole(), compare_by="groups"),
            ],
            role=TargetRole(),
        ),
        OneAAStatAnalyzer(),
    ]
)


class HomogeneityTest(ExperimentShell):

    def __init__(self):
        """Initialize HomogeneityTest with default experiment and output configurations."""
        super().__init__(
            experiment=HOMOGENEITY_TEST,
            output=HomoOutput(),
        )
