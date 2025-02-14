
import argparse
from datetime import date

import pandas


def append_line(name: str, purpose: str, created_by: str, created_date: date):
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
    )

    pandas.to_csv("temp_data/workloads_created.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="add_created_worload.py",
        description="Appends a line to the workloads_created file.",
    )
    parser.add_argument("name")
    parser.add_argument("purpose")
    parser.add_argument("created_by")

    append_line(
        name=parser.name,
        purpose=parser.purpose,
        created_by=parser.created_by,
        created_date=date.today(),
    )
    