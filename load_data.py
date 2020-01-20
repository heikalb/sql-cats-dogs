import pandas as pd
import sqlite3


def main():
    # Connect to database
    conn = sqlite3.connect('shelter_animals.db')
    c = conn.cursor()

    # Read data from original CSV
    df = pd.read_csv('aac_shelter_outcomes.csv')

    # Insert data into database
    for index, row in df.iterrows():
        values = [str(v).replace("\'", "") for v in row]
        values = [f"\'{v}\'" for v in values]

        sql_values = ", ".join(values)
        c.execute(f"INSERT INTO animals VALUES ({sql_values})")

    # Done
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    exit(0)
