# with DatabaseSqlite('person.sqlite') as db:
#     sql = "SELECT * FROM courses WHERE noun = ?"
#     data = db.query(sql, (value,))
#     if len(data) > 0:
#         return Course(*db.query(sql, (value,))[0][1:])
# INTEGER PRIMARY KEY AUTOINCREMENT