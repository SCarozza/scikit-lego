import pytest

from sklego.dummy import RandomRegressor
from sklego.mixture import GMMClassifier
from tests.conftest import id_func


@pytest.mark.parametrize("estimator", [
    RandomRegressor(),
], ids=id_func)
def test_shape_regression(estimator, random_xy_dataset_regr):
    X, y = random_xy_dataset_regr
    assert estimator.fit(X, y).predict(X).shape[0] == y.shape[0]


@pytest.mark.parametrize("estimator", [
    GMMClassifier(),
], ids=id_func)
def test_shape_classification(estimator, random_xy_dataset_clf):
    X, y = random_xy_dataset_clf
    assert estimator.fit(X, y).predict(X).shape[0] == y.shape[0]
