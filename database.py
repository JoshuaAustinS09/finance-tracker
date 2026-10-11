import sqlite3

def create_table_on_database():

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transaksi(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT NOT NULL,
            uang INTEGER NOT NULL,
            pilihan TEXT NOT NULL,
            kategori TEXT NOT NULL,
            deskripsi TEXT NOT NULL
            )
        ''')

    conn.commit()
    conn.close()

def inserting_values(tanggal, uang, pilihan, kategori, deskripsi):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO transaksi (tanggal, uang, pilihan, kategori, deskripsi) 
    VALUES (?, ?, ?, ?, ?)
    ''', (tanggal, uang, pilihan, kategori, deskripsi))
        
    conn.commit()
    conn.close()

def get_all_transactions():

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM transaksi')
    transactions = cursor.fetchall()

    conn.close()
    return transactions

def get_summary(pilihan):

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT SUM(uang) FROM transaksi WHERE pilihan = ?', (pilihan,))
    total = cursor.fetchone()[0]

    conn.close()

    if total is None:
        return 0
    else:
        return total

def get_saldo():
    pemasukan = get_summary('Pemasukan')
    pengeluaran = get_summary('Pengeluaran')

    dictionary = {'pemasukan': pemasukan, 'pengeluaran': pengeluaran, 'saldo': pemasukan - pengeluaran}
    return dictionary

def delete_transaction(transaction_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM transaksi WHERE id = ?', (transaction_id,))
    conn.commit()
    conn.close()

def update_transaction(transaction_id, tanggal, uang, pilihan, kategori, deskripsi):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE transaksi SET tanggal = ?, uang = ?, pilihan = ?, kategori = ?, deskripsi = ?
    WHERE id = ?''', (tanggal, uang, pilihan, kategori, deskripsi, transaction_id))

    conn.commit()
    conn.close()

def get_transaction_by_id(transaction_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM transaksi WHERE id = ?', (transaction_id,))
    transaction = cursor.fetchone()

    conn.close()

    return transaction

if __name__ == '__main__':
    create_table_on_database()
    print(get_transaction_by_id(1))
    print(get_transaction_by_id(9))
