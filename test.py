from mysql.connector import connect,Error

print("of")
val_tuple=("available",1)
print("ok")
val_tuple=("available",1)
try:
    with connect(
        host="192.168.1.121",
        user="toruser",
        password="64011340",
        database="project",
    ) as connection:
        print("test")
        update_query = "UPDATE yord SET state=%s WHERE refer=%s "
        with connection.cursor() as cursor:
            cursor.execute(update_query,val_tuple)
            connection.commit()  
        print("done")
except Error as e:
    print(e)