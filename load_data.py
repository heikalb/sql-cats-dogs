import pandas as pd
import sqlite3


def main():
    # Create database
    conn = sqlite3.connect('shelter_animals.db')
    c = conn.cursor()

    # Read data from original CSV
    df = pd.read_csv('aac_shelter_outcomes.csv')

    # Insert data into database
    column_names = [c for c in df]
    num_columns = len([c for c in df])

    for index, row in df.iterrows():
        values = [str(v).replace("\'", "") for v in row]
        values = [f"\'{v}\'" for v in values]

        sql_values = ", ".join(values)
        c.execute(f"INSERT INTO animals VALUES ({sql_values})")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    exit(0)
