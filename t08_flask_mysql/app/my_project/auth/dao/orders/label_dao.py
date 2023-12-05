"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text, func

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Label
from sqlalchemy.exc import IntegrityError
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain import Label
import random

class LabelDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Label

    def create_label(self, name: str, country: str) -> Label:
        """
        Creates a new label in the database.
        :param name: Label name
        :param country: Label country
        :return: Created Label object
        """
        new_label = Label(name=name, country=country)

        try:
            db.session.add(new_label)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Label with the same name already exists.")

        return new_label

    def create_database_and_tables(self):
        try:
            # Fetch names from the 'label' table
            result = db.session.execute(text("SELECT name FROM label"))
            label_names = [row[0] for row in result]

            for name in label_names:
                # Create a new database with the name from the 'label' table
                create_database_query = text(f"CREATE DATABASE IF NOT EXISTS `{name}`")
                db.session.execute(create_database_query)

                # Create random number of tables (1 to 9) in the created database
                num_tables = random.randint(1, 9)  # Generate random number in Python
                for i in range(1, num_tables + 1):
                    table_name = f"{name}{i}"
                    create_table_query = text(f"CREATE TABLE IF NOT EXISTS `{name}`.`{table_name}` (id INT)")
                    db.session.execute(create_table_query)

        except Exception as e:
            # Handle exceptions as needed
            print(f"An error occurred: {str(e)}")