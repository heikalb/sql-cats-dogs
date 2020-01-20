import sqlite3


def main():
    # Create database
    conn = sqlite3.connect('shelter_animals.db')
    c = conn.cursor()

    # Show number of animals in shelter
    c.execute("SELECT * FROM animals")
    print('Number of animals in shelter: ', len(c.fetchall()))

    c.execute("SELECT * FROM animals WHERE animal_type='Cat'")
    print('Number of cats in shelter: ', len(c.fetchall()))

    c.execute("SELECT * FROM animals WHERE animal_type='Dog'")
    print('Number of dogs in shelter: ', len(c.fetchall()))

    # Done
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    exit(0)
