import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pda import check_balance

DATASET_PATH = ROOT / "dataset" / "html_samples.json"

with DATASET_PATH.open(encoding="utf-8") as file:
    samples = json.load(file)


@pytest.mark.parametrize("sample", samples)
def test_html_samples(sample):
    result = check_balance(sample["html"])

    assert result["balanced"] == sample["expected"], (
        f"Sample {sample['id']} failed: {result}"
    )