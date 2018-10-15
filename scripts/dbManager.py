import sqlite3
import os


class DbManager:
    def __init__(self):
        if not os.path.exists("db/"):
            os.mkdir("db/")
        self.__db_path = "db/overtimes_db.sqlite"

        self.__connection = sqlite3.connect(self.__db_path)
        cursor = self.__connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Overtimes
                (`Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                `Date`	TEXT NOT NULL UNIQUE,
                `Hours`	INTEGER NOT NULL,
                `Note`	TEXT);""")
        self.__connection.commit()
        cursor.close()
        self.__connection.close()

    def insert_data(self, date, hours, note):
        try:
            self.__connection = sqlite3.connect(self.__db_path)
            cursor = self.__connection.cursor()
            cursor.execute("""
            SELECT Hours
            FROM Overtimes
            WHERE Date = ?;""", (date,))
            exists_data = cursor.fetchone()

            if exists_data is not None:
                new_data = exists_data[0] + hours
                print(new_data)
                if new_data >= 24:
                    cursor.execute("""
                    UPDATE Overtimes
                    SET Hours = 24
                    WHERE Date = ?;""", (date,))
                elif new_data < 24:
                    cursor.execute("""
                    UPDATE Overtimes
                    SET Hours = ?
                    WHERE Date = ?;""", (new_data, date))
            else:
                cursor.execute("""
                INSERT INTO Overtimes(Date, Hours, Note)
                VALUES(?, ?, ?);""", (date, hours, note))

        except sqlite3.Error as error:
            return ['error', str(error)]

        finally:
            self.__connection.commit()
            cursor.close()
            self.__connection.close()

        return ['done', 'inserted']

    def get_data_from_date(self, date):
        try:
            self.__connection = sqlite3.connect(self.__db_path)
            cursor = self.__connection.cursor()
            cursor.execute("""
                SELECT Date, Hours, Note
                FROM Overtimes
                WHERE Date=?;""", (date,))
            result = cursor.fetchall()

        except sqlite3.Error as error:
            # return ['error', str(error)]
            print(error)

        finally:
            self.__connection.commit()
            cursor.close()
            self.__connection.close()
            return result

    def get_from_all_time(self):
        try:
            self.__connection = sqlite3.connect(self.__db_path)
            cursor = self.__connection.cursor()

            cursor.execute("""
                SELECT Date, Hours, Note
                FROM Overtimes;""")
            result = cursor.fetchall()

        except sqlite3.Error as error:
            return ['error', str(error)]

        finally:
            self.__connection.commit()
            cursor.close()
            self.__connection.close()
            return result

    def get_data_from_date_range(self, date_start, date_end):
        try:
            self.__connection = sqlite3.connect(self.__db_path)
            cursor = self.__connection.cursor()
            cursor.execute("""
                SELECT Date, Hours, Note
                FROM Overtimes
                WHERE Date BETWEEN ? AND ?;""", (date_start, date_end))
            result = cursor.fetchall()

        except sqlite3.Error as error:
            return ['error', str(error)]

        finally:
            self.__connection.commit()
            cursor.close()
            self.__connection.close()
            return result




