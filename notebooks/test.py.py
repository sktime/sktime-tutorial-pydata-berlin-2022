from sktime.datatypes import check_is_mtype, convert
from sktime.forecasting.arima import ARIMA
from sktime.utils._testing.hierarchical import _make_hierarchical
from sktime.utils._testing.panel import _make_panel_X
n_instances = 10
PANEL_MTYPES = ["pd-multiindex", "nested_univ", "numpy3D"]
HIER_MTYPES = ["pd_multiindex_hier"]

y = _make_panel_X(n_instances=n_instances, random_state=42)
y = convert(y, from_type="nested_univ", to_type=HIER_MTYPES[0])

y_pred = ARIMA().fit(y).predict([1, 2, 3])
valid, _, metadata = check_is_mtype(y_pred, PANEL_MTYPES[0], return_metadata=True)