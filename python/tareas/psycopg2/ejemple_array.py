#SINTAXIS PARA INSERTAR EN POSTGRE EN TABLAS CON CAMPOS TIPADOS Y CON ARRAYS

'''insert into libros (isbn, libro) values ('isbn555',('UT4 Acceso a datos','2024', 'Edt. Santillana', array[('Autor1', 'apel1'),
 								('Autor2', 'Apel2')]::tipo_autor[]))
                                
    insert into libros (isbn, libro) values ('isbn555',ROW('UT4 Acceso a datos','2024', 'Edt. Santillana', array[ROW('Autor1', 'apel1'),
 							ROW('Autor2', 'Apel2')]::tipo_autor[]))
                            
    Se puede observar que el uso de la palabra ROW es opcional siempre que se facilite el nº de datos correcto'''


from psycopg2 import *
from psycopg2.extras import *
from conexion import *
from tablas import *
#from config import Config


def insertar():
    autores =[]
    i=0
    isbn= input ("Isbn: ");
    titulo= input ("Título: ");
    anio= int (input ("Año: "));
    edt= input ("Editorial: ");
    num_autores = int(input ("Cuántos autores: "));
    for i in range(num_autores):
        nombre = input(f"Nombre {i}: ")
        apellido = input(f"Apellido {i}: ")
        autores.append((nombre, apellido))
    auts = [tuple(a) for a in autores]
    
    #libro_data = (titulo, int(anio), edt, autores)
    libro_data = (titulo, int(anio), edt, auts)

    print (libro_data)

    
    try:  
        cursor = conectar.cursor()
        consulta = 'insert into libros (isbn, libro) values (%s,%s)'
        
        print (consulta)
        cursor.execute(consulta, (isbn, libro_data))
        print ("Datos insertados correctamente")
        
        cursor.close()
        conectar.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conectar is not None:
            conectar.close()
            

        
if __name__ == '__main__':
    #conectar_bd()
    insertar() 
    #mostrar_tabla()