from flask import Flask, render_template, request, redirect, url_for
import mariadb

app = Flask(__name__)

DB_CONFIG = {
    "host": "10.200.14.28",
    "user": "anohej",
    "password": "alphadaddyjehona",
    "database": "Quetes"
}

def get_db_connection():
    return mariadb.connect(**DB_CONFIG)


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, quote, created_at FROM quotes ORDER BY created_at DESC")
    rows = cur.fetchall()  
    cur.close()
    conn.close()
    return render_template('quotes.html', quotes=rows)


@app.route('/add', methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        quote = request.form.get('quote', '').strip()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO quotes (name, quote) VALUES (%s, %s)",
            (name, quote)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add_quote.html')


@app.route('/delete/<int:qid>', methods=['POST'])
def delete_quote(qid):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM quotes WHERE id = %s", (qid,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/quote/<int:qid>', methods=['GET', 'POST'])
def view_quote(qid):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        new_quote = request.form.get('quote', '').strip()
        if new_quote:
            cur.execute("UPDATE quotes SET quote=%s WHERE id=%s", (new_quote, qid))
            conn.commit()

    cur.execute("SELECT id, name, quote, created_at FROM quotes WHERE id = %s", (qid,))
    quote = cur.fetchone()
    cur.close()
    conn.close()

    if not quote:
        return "Quote not found", 404

    return render_template('quote.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
