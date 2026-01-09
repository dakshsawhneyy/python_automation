import sqlite3

# 1. Connect (creates file if not exists)
conn = sqlite3.connect('metrics.db')
cursor = conn.cursor()

# 2. Execute SQL
cursor.execute("CREATE TABLE IF NOT EXISTS uptime (server_ip TEXT, percent INTEGER)")
cursor.execute("INSERT INTO uptime VALUES ('10.0.0.1', 99)")

# Inserting items into DB
cursor.execute("CREATE TABLE IF NOT EXISTS disc_usage (date TEXT, percent INTEGER)")
cursor.execute(f"INSERT INTO disc_usage VALUES (?, ?)", (datetime.datetime.now().isoformat(), disc_usage))

# Fetching all data
cursor.execute("SELECT * FROM disc_usage")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 3. Save & Close
conn.commit()
conn.close()
