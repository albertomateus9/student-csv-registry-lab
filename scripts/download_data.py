from __future__ import annotations

import argparse
from pathlib import Path

PROJECT = {
  "code": "P08",
  "title": "Student CSV Registry Lab",
  "source": "Local synthetic sample",
  "dataset": "Synthetic class registry sample"
}
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Document public data acquisition for this lab.")
    parser.add_argument("--write-source-card", action="store_true", help="Write a local source card in data/raw/SOURCE.md.")
    args = parser.parse_args()

    message = (
        f"{PROJECT['code']} - {PROJECT['title']}\n"
        f"Dataset reference: {PROJECT['dataset']}\n"
        f"Primary source: {PROJECT['source']}\n\n"
        "This helper does not download large files automatically. Review the source terms, download manually when needed, "
        "and keep large raw data outside Git."
    )
    print(message)

    if args.write_source_card:
        raw_dir = ROOT / "data" / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        (raw_dir / "SOURCE.md").write_text(message + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
