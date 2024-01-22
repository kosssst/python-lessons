import json
import sqlite3

#-----task 1-----

with open("../raw_data.json") as f:
    text=json.load(f)

print(type(text))

result = []
for i in text["Ship_equipment"]:
    for keys, values in i.items():
        result.append(values)


with open('new_raw_data.json', 'w') as f:
    json.dump(result, f, indent=4)

#-----task 2-----
    
with open("new_raw_data.json") as f:
    text1=json.load(f)

con = sqlite3.connect("json_table.db")
c = con.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS json_table (
        name text,
        typeid text,
        line text )
""")

for i in text1:

    query = """INSERT INTO json_table VALUES (?, ?, ?)"""
    c.execute(query, (i['name'], i['typeid'], i['line']))

# c.execute("SELECT * FROM json_table ") 
# print(c.fetchall())

con.commit()
con.close()
