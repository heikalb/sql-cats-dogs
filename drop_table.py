import sqlite3


def main():
    connection = sqlite3.connect('shelter_animals.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE animals")

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
    exit(0)