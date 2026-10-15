import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pda import check_balance


def test_html_samples():
    dataset_path = ROOT / "dataset" / "html_samples.json"

    with dataset_path.open(encoding="utf-8") as file:
        samples = json.load(file)

    for sample in samples:
        result = check_balance(sample["html"])

        assert result["balanced"] == sample["expected"], (
            f"Sample {sample['id']} failed: {result}"
        )