import requests
import sqlite3

def fetch_cat_facts():
    """API'den kedi fact'lerini çeker."""
    response = requests.get("https://cat-fact.herokuapp.com/facts")
    cat_facts = response.json()
    return cat_facts  # 'all' kullanmadan doğrudan döndür

def create_database(db_name):
    """SQLite veritabanı ve tablo oluşturur."""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cat_facts
                 (id INTEGER PRIMARY KEY, fact TEXT)''')
    conn.commit()
    conn.close()

def save_facts_to_database(db_name, cat_facts):
    """Kedi fact'lerini veritabanına kaydeder."""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    for fact in cat_facts:
        c.execute("INSERT INTO cat_facts (fact) VALUES (?)", (fact['text'],))
    conn.commit()
    conn.close()

def display_facts(db_name):
    """Veritabanındaki kedi fact'lerini görüntüler."""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    for row in c.execute('SELECT * FROM cat_facts'):
        print(row)
    conn.close()

def main():
    db_name = "cat_facts.db"
    create_database(db_name)
    cat_facts = fetch_cat_facts()
    save_facts_to_database(db_name, cat_facts)
    print("Veritabanına kaydedilen kedi fact'leri:")
    display_facts(db_name)

if __name__ == "__main__":
    main()