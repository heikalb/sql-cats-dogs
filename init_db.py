import pandas as pd
import sqlite3


def main():
    # Create database
    connection = sqlite3.connect('shelter_animals.db')
    cursor = connection.cursor()

    # Read data
    df = pd.read_csv('aac_shelter_outcomes.csv')

    # Get column names for table
    column_names = [f'{c} TEXT' for c in df]

    # Create table
    cursor.execute(f"CREATE TABLE animals ({', '.join(column_names)})")

    # Done
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
    exit(0)
