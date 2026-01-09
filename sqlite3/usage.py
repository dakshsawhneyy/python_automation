import sqlite3

# 1. Connect (creates file if not exists)
conn = sqlite3.connect('metrics.db')
cursor = conn.cursor()

# 2. Execute SQL
cursor.execute("CREATE TABLE IF NOT EXISTS uptime (server_ip TEXT, percent INTEGER)")
cursor.execute("INSERT INTO uptime VALUES ('10.0.0.1', 99)")

# 3. Save & Close
conn.commit()
conn.close()
