import mysql.connector,socket

def get_db():
    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="alumno",
        password="alumno",
        db="prueba"
    )
    return db


def insertar(db,data:tuple):
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO alumno values({data[0]}, '{data[1]}');")
    db.commit()
    cursor.close()

def delete(db,data:int):
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM alumno WHERE dni = '{data}';")
    db.commit()
    cursor.close()


def update(db,data:tuple):
    cursor = db.cursor()
    cursor.execute(f"""UPDATE alumno SET nombre = '{data[0]}'
                   WHERE dni = '{data[1]}';""")
    db.commit()
    cursor.close()

if  __name__  == '__main__':
    db = get_db()

    insertar(db,(2,"luis"))