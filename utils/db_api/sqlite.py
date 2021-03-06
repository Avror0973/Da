import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
                CREATE TABLE "Users" (
                    "id" INTEGER NOT NULL UNIQUE,
                    "user_id" INTEGER NOT NULL UNIQUE,
                    "name" TEXT,
                    "contact" TEXT UNIQUE,
                    "address" INTEGER,
                    PRIMARY KEY("id" AUTOINCREMENT)
);
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    # Using
    def add_user(self, user_id: int, name: str, contact: str = None, address: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, name, contact, address) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, name, contact, address), commit=True)

    # Using
    def select_last_ten_users(self):
        sql = """
        SELECT * FROM Users ORDER BY id DESC LIMIT 10
        """

        return self.execute(sql, fetchall=True)

    # Using
    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    # Using
    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    # Using
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_address(self, address, user_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET address=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(address, user_id), commit=True)

    # Using
    def update_user_number(self, contact, user_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET contact=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(contact, user_id), commit=True)

    # Using
    def update_user_name(self, name, user_id):
        sql = f"""
                UPDATE Users SET name=? WHERE user_id=?
                """
        return self.execute(sql, parameters=(name, user_id), commit=True)

    # Using
    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    # Новый заказ
    def new_order(self, user_id: int, customer_name: str, order_data: str, order_address: str,
                  order_contact: str, order_check: int, order_status: str = None):
        sql = """
        INSERT INTO Orders(user_id, customer_name, order_data, order_address, order_contact, order_check, order_status) 
        VALUES(?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, customer_name, order_data, order_address, order_contact, order_check, order_status), commit=True)


    def show_orders(self, user):
        sql = """
        SELECT * FROM Orders
        """

        return self.execute(sql, parameters=user, fetchall=True)


# WHERE user_id=? ORDER BY order_id DESC LIMIT 5


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
