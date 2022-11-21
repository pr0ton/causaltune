import warnings
from auto_causality import AutoCausality
from auto_causality.datasets import iv_dgp_econml


warnings.filterwarnings("ignore")


class TestEndToEnd(object):
    def test_endtoend_iv(self):
        data = iv_dgp_econml()
        data.preprocess_dataset()
        # treatment = data.treatment
        # targets = data.outcomes
        # instruments = data.instruments
        # data_df, features_X, features_W = preprocess_dataset(
        #     data.data, treatment, targets, instruments
        # )
        # outcome = targets[0]
        auto_causality = AutoCausality(
            time_budget=1000,
            components_time_budget=10,
            propensity_model="auto",
            resources_per_trial={"cpu": 0.5},
            use_ray=False,
            verbose=3,
            components_verbose=2,
        )

        auto_causality.fit(data)

        for est_name, scores in auto_causality.scores.items():
            assert est_name in auto_causality.estimator_list
