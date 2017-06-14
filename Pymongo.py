from  pymongo import collation

if "__name__"=="__main__":
    Conn = collation()
    db = Conn.test_database
    people = db.people