
import psycopg2

try:
    print('PostgreSQL: Connecting to the database...')
    conn = psycopg2.connect(host="localhost", port=5432, database="mydb", user="myuser", password="mypassword")

    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print('PostgreSQL database version:', db_version)    
    cur.close

    cur = conn.cursor()
    cur.execute("SELECT task_id, user_id, title, done FROM task")
    print('Task count: ', cur.rowcount)
    row = cur.fetchone()
    while row is not None:
        print('Task: ', row)
        row = cur.fetchone()
    cur.close

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
