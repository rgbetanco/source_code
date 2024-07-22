import Ads as ads
import sqlite3
import Db_API as db

DB_NAME = 'aguaCero.db'

def main():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            db.create_tarjetas(conn)
            db.create_transaccions(conn)
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

    ads.Ads()

if __name__ == '__main__':
    main()