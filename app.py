from flask import Flask, render_template, request, redirect, url_for
from database import get_all_transactions, inserting_values, get_saldo, delete_transaction, update_transaction, get_transaction_by_id

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    all_transactions = get_all_transactions()
    saldo = get_saldo()

    if request.method == 'POST':
        tanggal = request.form['tanggal']
        pilihan = request.form['pilihan']
        kategori = request.form['kategori']
        deskripsi = request.form['deskripsi']
        try:
            jumlah = int(request.form['jumlah'])
        except ValueError:
            error_message = "Jumlah harus berupa angka."
            return render_template('index.html', transactions=all_transactions, saldo=saldo, error_message=error_message)
        
        if jumlah <= 0:
            error_message = "Jumlah harus lebih besar dari 0."
            return render_template('index.html', transactions=all_transactions, saldo=saldo, error_message=error_message)
        
        

        if not tanggal or not pilihan or not kategori or not deskripsi:
            error_message = "Semua field harus diisi."
            return render_template('index.html', transactions=all_transactions, saldo=saldo, error_message=error_message)

        inserting_values(tanggal=tanggal, uang=jumlah, pilihan=pilihan, kategori=kategori, deskripsi=deskripsi)
        return redirect(url_for('hello'))
        
    return render_template('index.html', transactions=all_transactions, saldo=saldo)

@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete(transaction_id):
    delete_transaction(transaction_id)
    return redirect(url_for('hello'))

@app.route('/update/<int:transaction_id>', methods=['GET', 'POST'])
def edit(transaction_id):
    transaction = get_transaction_by_id(transaction_id)

    if transaction is None:
        return redirect(url_for('hello'))

    if request.method == 'POST':
        tanggal = request.form['tanggal']
        pilihan = request.form['pilihan']
        kategori = request.form['kategori']
        deskripsi = request.form['deskripsi']
        try:
            jumlah = int(request.form['jumlah'])
        except ValueError:
            error_message = "Jumlah harus berupa angka."
            return render_template('edit.html', transactions=transaction, error_message=error_message)
                
        if jumlah <= 0:
            error_message = "Jumlah harus lebih besar dari 0."
            return render_template('edit.html', transactions=transaction, error_message=error_message)

        if not tanggal or not pilihan or not kategori or not deskripsi:
            error_message = "Semua field harus diisi."
            return render_template('edit.html', transactions=transaction, error_message=error_message)
        
        update_transaction(transaction_id, tanggal=tanggal, uang=jumlah, pilihan=pilihan, kategori=kategori, deskripsi=deskripsi)
        return redirect(url_for('hello'))

    return render_template('edit.html', transaction=transaction)

if __name__ == '__main__':
    app.run(debug=True)
    
