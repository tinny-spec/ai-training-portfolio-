"""
dataset_quality_checker.py

A small utility for sanity-checking a labeled dataset before it goes into
model training or annotation review. Reports row counts, duplicate rows,
missing values, and the distribution of unique labels.

Usage:
    python dataset_quality_checker.py sample_dataset.csv
"""

import sys
import pandas as pd


def check_dataset(path: str) -> None:
    df = pd.read_csv(path)

    print("Total Rows:", len(df))

    print("\nDuplicate Rows:")
    print(df[df.duplicated()])

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nUnique Labels:")
    print(df["label"].value_counts())


if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "sample_dataset.csv"
    check_dataset(file_path)
