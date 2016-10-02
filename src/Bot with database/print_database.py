from kyotocabinet import *
db = DB()
db.open("users.kch", DB.OREADER)

cur = db.cursor()
cur.jump()
while True:
    rec = cur.get(True)
    if not rec: break
    print(rec[0].decode(encoding="utf-8", errors="strict"))
cur.disable()
db.close()
