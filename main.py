import sqlite3
from wsgiref.util import request_uri

DB_NAME = "estudiantes.db"

class Docente:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.roe_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS docentes (
            id_docente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            carrera TEXT NOT NULL 
            );
            
        """)
        conn.commit()
        return conn

    @staticmethod
    def guardar_docente(self):
        with self._conn() as conn:
            conn.execute("INSERT INTO docentes(nombre, curso) VALUES (?, ?)",
                         (self.nombre,self.carrera))
            print(f"Docente {self.nombre} guardado exitosamente.")

    @staticmethod
    def listar_docentes(self):
        with Docente._conn() as conn:
            doc = conn.execute("SELECT * FROM docentes")
            filas = doc.fetchall()
            if not filas:
                print("No hay docente en la base de datos")
                return

            print("LISTA DE DOCENTES")
            for f in filas:
                print(f"ID: {f['id_docente']} | Nombre: {f['nombre']} | Carrera: {f['carrera']}")

    @staticmethod
    def modificar_docente(self):
        ide = input("ingrese el ID del docente que desea modificar")
        with Docente._conn() as conn:
            doc = conn.execute("SELECT * FROM docentes WHERE id_docente = ?", (ide,))
            fila = doc.fetchall()
            if not fila:
                print("No hay docente en la base de datos")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            carrera = input(f"Nueva carrera [{fila['carrera']}]: ") or fila['carrera']
            conn.execute("UPDATE docentes SET nombre=?, carrera=? WHERE id_docente=?",
                         (nombre, carrera, ide))
            print("docente actualizado con éxito.")

    @staticmethod
    def eliminar_docente(self):
        ide = input("Ingrese ID del docente a eliminar: ")
        with Docente._conn() as conn:
            doc = conn.execute("DELETE FROM docentes WHERE id_docente = ?", (ide,))
            if doc.rowcount == 0:
                print("No se encontró el docente.")
            else:
                print("Docente eliminado con éxito.")


class Curso:
    def __init__(self, nombre, carrera, creditos):
        self.nombre = nombre
        self.carrera = carrera
        self.creditos = creditos

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.roe_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            carrera TEXT NOT NULL,
            creditos INTEGER NOT NULL
            );

        """)
        conn.commit()
        return conn

    @staticmethod
    def guardar_curso(self):
        with self._conn() as conn:
            conn.execute("INSERT INTO carrera(nombre, carrera, creditos) VALUES (?, ?, ?)",
                         (self.nombre, self.carrera, self.creditos))
            print(f"Curso {self.nombre} guardado exitosamente.")

    @staticmethod
    def listar_cursos():
        with Curso._conn() as conn:
            cur = conn.execute("SELECT * FROM docentes")
            filas = cur.fetchall()
            if not filas:
                print("No hay cursos en la base de datos")
                return

            print("LISTA DE Cursos")
            for f in filas:
                print(f"ID: {f['id_Curso']} | Nombre: {f['nombre']} | Carrera: {f['carrera']} | Creditos: {f['creditos']}")

    @staticmethod
    def modificar_curso():
        ide = input("ingrese el ID del curso que desea modificar")
        with Curso._conn() as conn:
            doc = conn.execute("SELECT * FROM cursos WHERE id_curso = ?", (ide,))
            fila = doc.fetchall()
            if not fila:
                print("No hay cursos en la base de datos")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            carrera = input(f"Nueva carrera [{fila['carrera']}]: ") or fila['carrera']
            creditos = input(f"Nuevos creditos [{fila['creditos']}]: ]") or fila['creditos']
            conn.execute("UPDATE cursos SET nombre=?, carrera=? , creditos=? WHERE id_curso=?",
                         (nombre, carrera, creditos, ide))
            print("Curso actualizado con éxito.")

    @staticmethod
    def eliminar_curso():
        ide = input("Ingrese ID del curso a eliminar: ")
        with Curso._conn() as conn:
            cur = conn.execute("DELETE FROM Curso WHERE id_curso = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el curso.")
            else:
                print("Curso eliminado con éxito.")


class Estudiante:
    def __init__(self, nombre, carrera, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                carrera TEXT NOT NULL,
                promedio REAL
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO estudiantes (nombre, carrera, promedio) VALUES (?, ?, ?)",
                (self.nombre, self.carrera, self.promedio)
            )
        print(f"Estudiante '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes")
            filas = cur.fetchall()
            if not filas:
                print("No hay estudiantes registrados.")
                return
            print("\n--- LISTADO DE ESTUDIANTES ---")
            for f in filas:
                print(f"ID: {f['id_estudiante']} | Nombre: {f['nombre']} | Carrera: {f['carrera']} | Promedio: {f['promedio']}")

    @staticmethod
    def modificar():
        ide = input("Ingrese ID del estudiante a modificar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes WHERE id_estudiante = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el estudiante.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            carrera = input(f"Nueva carrera [{fila['carrera']}]: ") or fila['carrera']
            promedio = input(f"Nuevo promedio [{fila['promedio']}]: ") or fila['promedio']
            conn.execute("UPDATE estudiantes SET nombre=?, carrera=?, promedio=? WHERE id_estudiante=?",
                         (nombre, carrera, promedio, ide))
        print("Estudiante actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del estudiante a eliminar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("DELETE FROM estudiantes WHERE id_estudiante = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el estudiante.")
            else:
                print("Estudiante eliminado con éxito.")

    @staticmethod
    def promedio_general():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT AVG(promedio) AS prom FROM estudiantes")
            prom = cur.fetchone()["prom"]
            if prom:
                print(f"\nPromedio general: {prom:.2f}")
            else:
                print("No hay datos para calcular el promedio.")


# --- MENÚ PRINCIPAL ---

def menu():
    while True:
        print("====== MENÚ PRINCIPAL =======")
        print("1. Opciones Estudiantes")
        print("2. Opciones Docentes")
        print("0. Salir ")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                menu_estudiante()
            case "2":
                menu_docente()
            case "3":
                menu_docente()
            case "0":
                print("Saliendo del programa...")
                break



def menu_estudiante():
    while True:
        print("\n===== MENÚ DE ESTUDIANTES =====")
        print("1. Ingresar estudiante")
        print("2. Listar estudiantes")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
        print("5. Promedio general")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                carrera = input("Carrera: ")
                promedio = float(input("Promedio: "))
                e = Estudiante(nombre, carrera, promedio)
                e.guardar()

            case "2":
                Estudiante.listar()
            case "3":
                Estudiante.modificar()
            case "4":
                Estudiante.eliminar()
            case "5":
                Estudiante.promedio_general()
            case "0":
                print("Saliendo al menu principal...")
                break


def menu_docente():
    while True:
        print("\n===== MENÚ DE DOCENTE =====")
        print("1. Ingresar Docente")
        print("2. Listar Docentes")
        print("3. Modificar Docente")
        print("4. Eliminar Docente")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
         case "1":
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
            d = Docente(nombre, carrera)
            d.guardar_docente()
         case "2":
            Docente.listar_docentes()
         case "3":
            Docente.modificar_docente()
         case "4":
            Docente.eliminar_docente()
         case "0":
            print("Saliendo al Menu principal...")
            break

def menu_curso():
    while True:
        print("\n===== MENÚ DE CURSO =====")
        print("1. Ingresar Cursos")
        print("2. Listar Cursos")
        print("3. Modificar Curso")
        print("4. Eliminar Curso")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
         case "1":
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
            creditos = float(input("Creditos: "))
            c = Curso(nombre, carrera, creditos)
            c.guardar_curso()
         case "2":
            Curso.listar_cursos()
         case "3":
            Curso.modificar_curso()
         case "4":
            Curso.eliminar_curso()
         case "0":
            print("Saliendo al Menu principal...")
            break

if __name__ == "__main__":
    menu()