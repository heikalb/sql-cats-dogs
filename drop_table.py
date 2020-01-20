import sqlite3


def main():
    # Connect to database
    conn = sqlite3.connect('shelter_animals.db')
    c = conn.cursor()

    # Drop table
    c.execute("DROP TABLE animals")

    # Done
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    exit(0)