import sqlite3
from datetime import datetime

#tipo: 0 -> venta (dispensado), 1 -> compra (recarga)
#retirado: 0 -> No ( aun no ), 1 -> Si
def create_transaccions (conn):
    sql = '''CREATE TABLE IF NOT EXISTS transacciones (id INTEGER PRIMARY KEY AUTOINCREMENT, tarjeta_id INTEGER, monto INTEGER, tipo INTEGER, fecha TEXT, hora TEXT, retirado INTEGER, FOREIGN KEY (tarjeta_id) REFERENCES tarjetas (id))'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

# tipo: 0 -> admin, 1-> vendedor, 2 -> usuario
# habilitado: 0 -> no, 1 -> si
def create_tarjetas (conn):
    sql = '''CREATE TABLE IF NOT EXISTS tarjetas (id INTEGER PRIMARY KEY AUTOINCREMENT, tarjeta_numero TEXT, emitido TEXT, saldo INTEGER, habilitado INTEGER, tipo INTEGER)'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def add_tarjetas (conn, record):
    sql = '''INSERT INTO tarjetas_usuarios (tarjeta_numero, emitido, saldo, habilitado) VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, record)
    conn.commit()
    return cur.lastrowid

def add_transaccion (conn, record):
    sql = '''INSERT INTO transacciones (tarjeta_id, monto, tipo, fecha, hora, retirado) VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, record)
    conn.commit()
    return cur.lastrowid

def main():
    try:
        with sqlite3.connect("aguaCero.db") as conn:
            create_tarjetas(conn)
            create_transaccions(conn)
            
            #AGREGAR TARJETA
            numero_tarjeta = 'ABC'
            emitido = datetime.now().strftime("%Y-%m-%d %H:%M")
            saldo = 100
            habilitado = 1
            tarjeta = (numero_tarjeta, emitido, saldo, habilitado)
            nueva_tarjeta_id = add_tarjetas(conn, tarjeta)
            print(nueva_tarjeta_id)

            #AGREGAR TRANSACCION
            monto = 100
            tipo = 1
            fecha = datetime.now().strftime("%Y-%m-%d")
            hora = datetime.now().strftime("%H:%M")
            retirado = 0
            transaccion = (nueva_tarjeta_id, monto, tipo, fecha, hora, retirado)
            nueva_transaccion_id = add_transaccion(conn, transaccion)
            print(nueva_transaccion_id)


            fechahora = datetime.now().strftime("%Y-%m-%d %H:%M")
            print("Fecha / Hora de la transaccion: "+fechahora)
            
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    main()