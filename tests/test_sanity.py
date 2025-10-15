import os

def test_artifacts_exist():
    assert os.path.exists('artifacts/fig_pr_isolation_forest.png')
    assert os.path.exists('artifacts/fig_pr_lof.png')
    assert os.path.exists('artifacts/fig_heart_rate_anomalies.png')
