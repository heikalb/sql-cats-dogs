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
    print('Number of dogs in shelter: ', len(c.fetchall()), '\n')


    # Show cat outcomes
    c.execute("SELECT outcome_type FROM animals WHERE animal_type='Cat'")
    num_cats = len(c.fetchall())

    c.execute("SELECT outcome_type FROM animals WHERE animal_type='Cat' AND outcome_type='Adoption'")
    cats_adopted = len(c.fetchall())
    print('Cats adopted: ', cats_adopted, f'{round(100*cats_adopted/num_cats, 2)}%')

    c.execute("SELECT outcome_type FROM animals WHERE animal_type='Cat' AND outcome_type<>'Adoption'")
    cats_not_adopted = len(c.fetchall())
    print('Cats not adopted: ', cats_not_adopted, f'{round(100*cats_not_adopted/num_cats, 2)}%')

    # Show dog outcomes
    c.execute("SELECT outcome_type FROM animals WHERE animal_type='Dog'")
    num_dogs = len(c.fetchall())

    c.execute("SELECT outcome_type FROM animals WHERE animal_type='Dog' AND outcome_type='Adoption'")
    dogs_adopted = len(c.fetchall())
    print('Dogs adopted: ', dogs_adopted, f'{round(100 * dogs_adopted / num_dogs, 2)}%')

    c.execute("SELECT outcome_type FROM animals WHERE animal_type='Dog' AND outcome_type<>'Adoption'")
    dogs_not_adopted = len(c.fetchall())
    print('Dogs not adopted: ', dogs_not_adopted, f'{round(100 * dogs_not_adopted / num_dogs, 2)}%', '\n')


    # Show unusual pets
    c.execute("""
    SELECT DISTINCT animal_type, breed FROM animals 
    WHERE animal_type<>'Cat' AND animal_type<>'Dog'
    ORDER BY breed ASC
    """)

    unusual_animals = c.fetchall()

    print('Unusual pets (not cat or dog):')

    for animal in unusual_animals:
        print(animal[1])

    # Done
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    exit(0)
