

import sqlite3



conn = sqlite3.connect('demo_data.sqlite3')
curr = conn.cursor()

curr.execute('DROP TABLE IF EXISTS demo')

curr.execute('CREATE TABLE demo(s TEXT, x INTEGER, y INTEGER)')
curr.execute('INSERT INTO demo(s, x, y) VALUES ("g", 3, 9)')
curr.execute('INSERT INTO demo(s, x, y) VALUES ("v", 5, 7)')
curr.execute('INSERT INTO demo(s, x, y) VALUES ("f", 8, 7)')
conn.commit()





conn = sqlite3.connect('demo_data.sqlite3')
curr = conn.cursor()
    
curr.execute('SELECT COUNT(x) FROM demo')

print('Rows: ', curr.fetchall())

curr.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND Y >= 5')
 
print('Rows where x and y are > 5: ', curr.fetchall()[0][0])

curr.execute('SELECT COUNT(DISTINCT y) FROM demo')

print('Distinct values of y: ', curr.fetchall()[0][0])
