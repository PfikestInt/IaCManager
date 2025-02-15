
import argparse
from datetime import date

import pandas


def prepend_line(name: str, purpose: str, created_by: str, created_date: date):
    df = pandas.read_csv("temp_data/workloads_created.csv")

    pandas.concat(
        [
            pandas.DataFrame(
                [
                    {
                        "Name": name,
                        "Purpose": purpose,
                        "Created By": created_by,
                        "Date": created_date
                    }
                ]
            ), 
            df
        ], 
        ignore_index=True
    ).to_csv("temp_data/workloads_created.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="add_created_worload.py",
        description="Prepends a line to the workloads_created file.",
    )
    parser.add_argument("name")
    parser.add_argument("purpose")
    parser.add_argument("created_by")
    args = parser.parse_args()
    
    prepend_line(
        name=args.name,
        purpose=args.purpose,
        created_by=args.created_by,
        created_date=date.today(),
    )
    