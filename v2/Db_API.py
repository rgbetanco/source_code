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