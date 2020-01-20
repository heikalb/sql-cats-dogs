"""
Create a database and a table within.
Heikal Badrulhisham, 2020 <heikal93@gmail.com>
"""

import pandas as pd
import sqlite3


def main():
    # Create database
    conn = sqlite3.connect('shelter_animals.db')
    c = conn.cursor()

    # Read data
    df = pd.read_csv('aac_shelter_outcomes.csv')

    # Get column names for table
    column_names = [f'{c} TEXT' for c in df]

    # Create table
    c.execute(f"CREATE TABLE animals ({', '.join(column_names)})")

    # Done
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    exit(0)
