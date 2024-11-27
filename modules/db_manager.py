import sqlite3

class DBManager:
    def __init__(self):
        self.connection = sqlite3.connect('data/data.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS EstateTable (
                                id INTEGER PRIMARY KEY,
                                estate_type TEXT,
                                city TEXT,
                                street TEXT,
                                number INTEGER,
                                square REAL,
                                price INTEGER,
                                rooms INTEGER,
                                floor INTEGER,
                                comment TEXT
                                )""")
        self.connection.commit()

    def create_call_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Call_EstateTable (
                                id INTEGER PRIMARY KEY,
                                estate_type TEXT,
                                city TEXT,
                                street TEXT,
                                number INTEGER,
                                square REAL,
                                price INTEGER,
                                rooms INTEGER,
                                floor INTEGER,
                                comment TEXT
                                )""")
        self.connection.commit()

    def get_all_estates(self):
        self.cursor.execute("SELECT * FROM EstateTable")
        return self.cursor.fetchall()


    def find_estate(self, estate_type, city, street, number, square, price, rooms, floor):
        query = "SELECT * FROM EstateTable WHERE 1=1"
        params = []

        if not estate_type == "":
            query += " AND estate_type=?"
            params.append(estate_type)
        if not city == "":
            query += " AND city=?"
            params.append(city)
        if not street == "":
            query += " AND street=?"
            params.append(street)
        if not number == "":
            query += " AND number=?"
            params.append(number)
        if not square == "":
            squares = square.split(" ")
            query += " AND square BETWEEN ? AND ?"
            params.append(squares[0])
            params.append(squares[1])
        if not price == "":
            prices = price.split(" ")
            query += " AND price BETWEEN ? AND ?"
            params.append(prices[0])
            params.append(prices[1])
        if not rooms == "":
            rooms = rooms.split(" ")
            query += " AND rooms BETWEEN ? AND ?"
            params.append(rooms[0])
            params.append(rooms[1])
        if not floor == "":
            query += " AND floor=?"
            params.append(floor)

        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def add_data(self, estate_type, city, street, number, square, price, rooms, floor, comment):
        self.cursor.execute("INSERT INTO EstateTable (estate_type, city, street, number, square, price, rooms, floor, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (estate_type, city, street, number, square, price, rooms, floor, comment))
        self.connection.commit()

    def add_call(self, estate_type, city, street, number, square, price, rooms, floor, phone):
        self.cursor.execute(
            "INSERT INTO Call_EstateTable (estate_type, city, street, number, square, price, rooms, floor, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (estate_type, city, street, number, square, price, rooms, floor, phone))
        self.connection.commit()