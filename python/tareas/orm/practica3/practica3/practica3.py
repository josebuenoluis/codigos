import conexion

db = conexion.conexion()

from orm_tablas import *

def actualizarDatosCliente() -> None:
    """ 1. Actualización de Datos de Clientes: Implementa una función que permita actualizar el número
 de teléfono de un cliente específico utilizando el método .save() en Peewee."""
    dniCliente = input("\nIngrese el DNI del cliente a actualizar: ") 
    try:
        if validarDni(dniCliente) == True:
            cliente = Cliente.select().where(Cliente.dni_cliente == dniCliente).get()
            print(f"\nNombre cliente: {cliente.nombre_cliente}\nDni del cliente: {cliente.dni_cliente}\nTelefono: {cliente.telefono}")
            telefono = input("\nIngrese el nuevo telefono: ")
            if telefono.isdigit() and len(telefono) == 9:
                #Consultamos si el nuevo telefono existe
                if len(Cliente.select(Cliente.telefono).where(Cliente.telefono==int(telefono))) == 0:
                    cliente.telefono = telefono
                    cliente.save()
                    print("\nCliente actualizado correctamente.")
                else:
                    print("\nEl telefono ingresado ya existe, pruebe con otro.")
            else:
                print("\nEl numero de telefono debe tener 9 digitos numericos.")
        else:
            print("\nEl NIF ingresado no es valido.")
    except DoesNotExist:
        print("\nEl DNI ingresado no existe en los registros.")
    except Exception as error:
        print(f"\nError: {error}")

def aumentarPresupuesto() -> None:
    """2. Aumentar en un 10% el presupuesto de todos los proyectos activos."""
    consulta = Proyectos.update(presupuesto=Proyectos.presupuesto + Proyectos.presupuesto * 0.10).where(
        Proyectos.fecha_fin > datetime.now().date()
    )
    filasAfectadas = consulta.execute()
    if filasAfectadas > 0:
        print(f"\n{filasAfectadas} Presupuestos aumentados correctamente.")
    else:
        print("\nNo hay proyectos activos para actualizar.")

def reasignarJefeProyecto() -> None:
    """3. Reasignar jefe de proyecto por id_proyecto."""
    dniJefe = input("\nIngrese el DNI del nuevo Jefe de proyecto: ")
    idProyecto = input("\nIngrese el ID del proyecto a reasignar: ")
    if validarDni(dniJefe) == True:
        try:
            #Devuelve un proyecto por su Id
            consulta = Proyectos.select().where(
                Proyectos.id_proyecto==idProyecto
            ).get()
            #Consultamos si el proyecto que vamos reasignar esta activo, ya que no podemos reasignar un jefe 
            # a un proyecto que este terminado
            if consulta.fecha_fin < datetime.now().date():
                raise ValueError("El proyecto a reasignar esta finalizado, vuelva a intentar.")
            #Validamos que el empleado pueda ser jefe de proyecto.
            if comprobarPuesto(dniJefe) == True:
                #Consultamos todos los proyectos en los que trabaja ese empleado
                proyectosTrabajados = Proyectos.select().where(Proyectos.dni_jefe_proyecto_fk==dniJefe)
                #Ahora hacemos una consulta de esos proyectos para saber si esta trabajando en algun proyecto activo
                if len(proyectosTrabajados.where(
                    Proyectos.fecha_fin > datetime.now().date()
                    )) == 0:
                        consulta.dni_jefe_proyecto_fk = dniJefe
                        consulta.save(force_insert=False)
                        print("\nJefe de proyecto reasignado correctamente.")
                else:
                    print("\nEl Jefe ingresado ya esta trabajando en otro proyecto.")
            elif comprobarPuesto(dniJefe) == None:
                print("\nEl DNI del jefe ingresado no corresponde con nigun registro.")
            else:
                print("\nEl empleado ingresado no puede ser jefe de proyecto.")
        except DoesNotExist:
            print("\nEl ID del proyecto ingresado no existe en los registros.")
        except IntegrityError:
            print("\nEl DNI del jefe ingresado no corresponde con nigun registro.")
        except Exception as error:
            print(f"\nError:{error}")
    else:
        print("\nEl NIF ingresado no es valido.")

def eliminarRegistrosClientes() -> None:
    """4. Eliminar registros de clientes que no tengan proyectos asociados."""
    try:
        with db.atomic():
            consulta = Cliente.delete().where(
                Cliente.dni_cliente.not_in(Proyectos.select(Proyectos.dni_cliente_fk))
            )
            filasAfectadas = consulta.execute()
            if filasAfectadas > 0:
                print(f"\n{filasAfectadas} clientes eliminados correctamente.")
            else:
                print("\nNo hay clientes que no tengan registros asociados.")
    except Exception as error:
        print(f"Error: {error}")

def borrarProyectosPresupuesto() -> None:
    """5. Eliminar proyectos cuyo presupuesto sea menor a 10.000$ y 
    cuya fecha de finalizacion haya pasado."""
    try:
        with db.atomic():
            consulta = Proyectos.delete().where(
                (Proyectos.presupuesto < 10000) &
                (Proyectos.fecha_fin < datetime.now().date())
            )
            filasAfectadas = consulta.execute()
            if filasAfectadas > 0:
                print(f"\n{filasAfectadas} proyectos eliminados correctamente.")
            else:
                print("\nNo se encuentran proyectos con las condiciones establecidas.")
    except Exception as error:
        print(f"Error: {error}")
        

def eliminarProyectosFinalizados() -> None:
    """6. Eliminar proyectos finalizados con mas de 5 años de antiguedad y
    reasignar sus empleados a otros proyectos activos."""
    try:
        consulta = Proyectos.select().where(
            (datetime.now().year - Proyectos.fecha_fin.year > 5)
        )
        if not len(consulta) > 0:
            raise ValueError("No se encuentran proyectos con mas de 5 años de antiguedad.")
        proyectosActivos = Proyectos.select().where(
                                Proyectos.fecha_fin > datetime.now().date()
                            )
        if not len(proyectosActivos) > 0:
            raise ValueError("No se encuentran proyectos activos para reasignar los empleados.")
        
        print("\nPROYECTOS ACTIVOS:\n")
        print("     ".join([f"{proyecto.id_proyecto}. {proyecto.titulo_proyecto}" 
                            for proyecto in proyectosActivos]))

        nuevoProyecto = input("\nSeleccione un Id_proyecto para reasignar los empleados: ")
        if len(proyectosActivos.select().where(Proyectos.id_proyecto==nuevoProyecto)) == 0:
            raise ValueError("Debe seleccionar un proyecto activo valido.")
        #El metodo replace sirve para hacer insert en caso de que no exista el registro o
        # update si ya existe, hago esto ya que quiero que se reasignen los empleados nuevos en
        # el proyecto y tambien los que ya trabajaban en el nuevo proyecto a reasignar
        #INICIO TRANSACCION
        with db.atomic():
            for proyecto in consulta:
                # El jefe de proyecto pasa a ser empleado del proyecto a reasignar si no esta
                # como jefe en un proyecto activo.
                if len(Proyectos.select().where(
                    (Proyectos.dni_jefe_proyecto_fk==proyecto.dni_jefe_proyecto_fk) &
                    (Proyectos.fecha_fin > datetime.now().date())
                    )) == 0:
                    EmpleadosProyectos.replace(id_proyecto_fk=nuevoProyecto,dni_empleado_fk=proyecto.dni_jefe_proyecto_fk).execute()
                for empleadoProyecto in EmpleadosProyectos.select().where(proyecto.id_proyecto==EmpleadosProyectos.id_proyecto_fk):
                    EmpleadosProyectos.replace(id_proyecto_fk=nuevoProyecto,dni_empleado_fk=empleadoProyecto.dni_empleado_fk).execute()
            #Iteramos en los proyectos finalizados que hemos consultado y
            #eliminamos sus campos asociados por fk, en este caso no es necesario utilizar el
            # argumento recursive=True por la FK.
            for proyecto in consulta:
                proyecto.delete_instance()
            print("\nRegistros eliminados correctamente y empleados reasignados.")
    except Exception as error:
        print(f"\nError: {error}")

def eliminarCliente() -> None:
    """7. Eliminar un cliente y todos sus datos asociados incluido proyectos."""
    try:
        dni_cliente = input("\nIngrese el DNI del cliente: ")
        if validarDni(dni_cliente):
            with db.atomic():
                Cliente.select().where(
                    (Cliente.dni_cliente==dni_cliente)
                ).get().delete_instance(recursive=True)
                print("\nDatos de cliente eliminados correctamente.")
        else:
            print("\nEl DNI ingresado no es valido.")
    except DoesNotExist:
        print("\nEl cliente ingresado no existe.")
    except Exception as error:
        print(f"Error: {error}")

def crearTablas() -> None:
    """Funcion para crear las tablas si no existen."""
    tablas = [Cliente,Empleados,Proyectos,EmpleadosProyectos,ProyectosTrabajados]
    if not db.table_exists(tablas[0]):
        print("\nTablas creadas.")
        db.create_tables(tablas)

def comprobarPuesto(dniJefe:str) -> bool:
    """Funcion para comprobar que un empleado es Jefe."""
    valido = False
    try:
        consulta = Empleados.select(Empleados.puesto).where(
            (Empleados.dni_empleado==dniJefe)
        ).get()
        if consulta.puesto == True:
            valido = True
    except DoesNotExist:
        valido = None
    except:
        valido = False
    finally:
        return valido

def validarDni(nif:str) -> bool:
    """Funcion para validar que un NIF ingresado sea correcto"""
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    valido = False
    if len(nif) == 9:
        if nif[-1] in letras and nif[:-1].isdigit():
            if len(nif[:-1]) == 8:
                numeros = int(nif[:-1])
                letra_verificar = nif[-1]
                calculo = numeros % 23
                ultima_letra = letras[calculo]
                if ultima_letra == letra_verificar:
                    valido = True
        elif nif[0] in 'XYZ' and nif[1:-1].isdigit() and nif[-1] in letras:
            if len(nif[1:-1]) == 7:
                valores = ['X','Y','Z']
                primera_letra_nif = nif[0]
                ultima_letra_verificar = nif[-1]
                valor_primera_letra = str(valores.index(primera_letra_nif))
                numeros_nif = nif[1:-1]
                numeros = valor_primera_letra + numeros_nif
                calculo = int(numeros) % 23
                ultima_letra = letras[calculo]
                if ultima_letra_verificar == ultima_letra:
                    valido = True
    return valido

if __name__ == '__main__':
    
    menu = """
    1. Actualizar telefono de un cliente.
    2. Aumentar un 10% el presupuesto de los proyectos activos.
    3. Reasignar Jefe de proyecto.
    4. Eliminar registros de clientes que no tengan proyecto.
    5. Eliminar proyectos cuyo presupuesto sea menor que 10.000$ y esten finalizados.
    6. Eliminar proyectos finalizados con mas de 5 años de antiguedad y reasignacion de empleados.
    7. Eliminar un cliente y todos sus datos asociados.
    8. Salir."""
    try:
        db.connect()
        crearTablas()
        while True:
            print(menu)
            opcion = input("\nIngrese una opcion: ")
            match opcion:
                case "1":
                    actualizarDatosCliente()
                case "2":
                    aumentarPresupuesto()
                case "3":
                    reasignarJefeProyecto()
                case "4":
                    eliminarRegistrosClientes()
                case "5":
                    borrarProyectosPresupuesto()
                case "6":
                    eliminarProyectosFinalizados()
                case "7":
                    eliminarCliente()
                case "8":
                    print("\nSaliendo del programa.")
                    break
                case _:
                    print("\nOpcion invalida.\n")
    except Exception as error:
        print(f"\nError: {error}")