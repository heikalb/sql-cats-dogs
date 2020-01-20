# Cats, dogs and SQL
This project is to showcase me learning SQL, or more specifically,
SQLite via Python. The dataset involved here is about animals in the Austin
Animal Center Shelter, which can be accessed 
[here](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-outcomes-and/version/1).
The dataset is in `aac_shelter_outcomes.csv` in this repository.

The following scripts have the following function, and should be run in order:

- `init_db.py`: Creates database (`shelter_animals.db`) and set column names.
- `load_data.py`: Gets data from `aac_shelter_outcomes.csv` into a table (`animals`) in the database.
- `drop_table.py`: For deleting the table `animals` in the databse (for starting over).
- `explore_data.py`: Does some data exploration of the database, including looking at 'unusual' animals.

## Requirements
- pandas