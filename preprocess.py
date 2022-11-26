import sqlite3
import csv
import pandas as pd
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to a SQLite database in Python"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("database connection created!")
    except Error as e:
        print(e)
    return conn


def create_table(c, create_table_sql):
    """create a table from the create_table_sql statement"""
    try:
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def add_data_to_db(cur, filename, db_name, num_cols):
    """add data from csv file to database"""
    file = open(filename, encoding="utf8")
    contents = csv.reader(file)
    questionmarks = ", ".join("?" * num_cols)
    insert_records = "INSERT INTO " + db_name + " VALUES " + "(" + questionmarks + ")"
    cur.executemany(insert_records, contents)


#if __name__ == "__main__":
def get_data():
    db_connection = create_connection(r"./sqlstore/database.db")
    cursor = db_connection.cursor()
    create_table(
        cursor,
        """CREATE TABLE IF NOT EXISTS attrition (
                                EmployeeID FLOAT,
                                Age FLOAT,
                                Attrition TEXT,
                                BusinessTravel TEXT,
                                DailyRate FLOAT,
                                Department TEXT,
                                DistanceFromHome FLOAT,
                                Education FLOAT,
                                EducationField TEXT,
                                EmployeeCount FLOAT,
                                EnvironmentSatisfaction FLOAT,
                                Gender TEXT,
                                HourlyRate FLOAT,
                                JobInvolvement FLOAT,
                                JobLevel FLOAT,
                                JobRole TEXT,
                                JobSatisfaction FLOAT,
                                MaritalStatus TEXT,
                                MonthlyIncome FLOAT,
                                MonthlyRate FLOAT,
                                NumCompaniesWorked FLOAT,
                                Over18 TEXT,
                                OverTime TEXT,
                                PercentSalaryHike FLOAT,
                                PerformanceRating FLOAT,
                                RelationshipSatisfaction FLOAT,
                                StandardHours FLOAT,
                                Shift FLOAT,
                                TotalWorkingYears FLOAT,
                                TrainingTimesLastYear FLOAT,
                                WorkLifeBalance FLOAT,
                                YearsAtCompany FLOAT,
                                YearsInCurrentRole FLOAT,
                                YearsSinceLastPromotion FLOAT,
                                YearsWithCurrManager FLOAT
                                );""",
    )
    
    cursor.execute(
        "DELETE FROM attrition;",
    )
    add_data_to_db(cursor, "train.csv", "attrition", 35)


    # store it in a pandas dataframe
    surveys_df = pd.read_sql_query("SELECT * from attrition", db_connection)
    #print(surveys_df)

    db_connection.commit()
    db_connection.close()
    return surveys_df