
import csv
from pathlib import Path
from typing import Optional
from models import *

COMPONENTES_DB = "componentes.csv"
ELIMINADOS_COMP = "eliminados_componentes.csv"
ELIMINADOS_DISTRI = "eliminados_distribuidores.csv"
DISTRIBUIDORES = "distribuidores.csv"
CAMPOS = ["id", "nombre", "tipo", "marca", "modelo"]
CAMPOSDISTRI = ["id", "nombre", "direccion"]

def leer_todos_componentes():
    with open(COMPONENTES_DB) as archivo:
        reader = csv.DictReader(archivo)
        return [ComponenteConId(**row) for row in reader]
def leer_todos_componentes_eliminados():
    with open(ELIMINADOS_COMP) as archivo:
        reader = csv.DictReader(archivo)
        return [ComponenteConId(**row) for row in reader]

def leer_componente(id):
    with open(COMPONENTES_DB) as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            if int(fila["id"]) == id:
                return ComponenteConId(**fila)

def busqueda_atributo_componente(tipo, modelo):
    with open(COMPONENTES_DB) as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            if ((fila["tipo"]) == tipo) and ((fila["modelo"]) == modelo):
                return ComponenteConId(**fila)

def leer_todos_distri():
    with open(DISTRIBUIDORES) as archivo:
        reader = csv.DictReader(archivo)
        return [DistriConId(**row) for row in reader]

def leer_todos_distri_eliminados():
    with open(ELIMINADOS_DISTRI) as archivo:
        reader = csv.DictReader(archivo)
        return [DistriConId(**row) for row in reader]

def leer_distri(id):
    with open(DISTRIBUIDORES) as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            if int(fila["id"]) == id:
                return DistriConId(**fila)

def busqueda_atributo_distri(nombre):
    with open(DISTRIBUIDORES) as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            if ((fila["nombre"]) == nombre):
                return DistriConId(**fila)

def obtener_siguiente_id_componentes():
    try:
        with open(COMPONENTES_DB, mode="r") as archivo:
            reader = csv.DictReader(archivo)
            max_id = max(int(row["id"]) for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1

def escribir_componente_csv(comp: ComponenteConId):
    with open(COMPONENTES_DB, mode="a", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
        writer.writerow(comp.model_dump())

def nuevo_componente(comp: Componente):
    id = obtener_siguiente_id_componentes()
    comp_con_id = ComponenteConId(id=id, **comp.model_dump())
    escribir_componente_csv(comp_con_id)
    return comp_con_id

def escribir_distri_csv(comp: DistriConId):
    with open(DISTRIBUIDORES, mode="a", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=CAMPOSDISTRI)
        writer.writerow(comp.model_dump())

def nuevo_distri(comp: Distribuidores):
    id = obtener_siguiente_id_distri()
    comp_con_id = DistriConId(id=id, **comp.model_dump())
    escribir_distri_csv(comp_con_id)
    return comp_con_id

def obtener_siguiente_id_distri():
    try:
        with open(DISTRIBUIDORES, mode="r") as archivo:
            reader = csv.DictReader(archivo)
            max_id = max(int(row["id"]) for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1
    
def modificar_componente(id: int, datos: dict):
    componentes = leer_todos_componentes()
    componente_actualizado = None

    for idx, c in enumerate(componentes):
        if c.id == id:
            if datos.get("nombre") is not None:
                componentes[idx].nombre = datos["nombre"]
            if datos.get("tipo") is not None:
                componentes[idx].tipo = datos["tipo"]
            if datos.get("marca") is not None:
                componentes[idx].marca = datos["marca"]
            if datos.get("modelo") is not None:
                componentes[idx].modelo = datos["modelo"]
            componente_actualizado = componentes[idx]
            break

    if componente_actualizado:
        with open(COMPONENTES_DB, mode="w", newline="") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
            writer.writeheader()
            for comp in componentes:
                writer.writerow(comp.model_dump())
        return componente_actualizado

    return None

def modificar_distri(id: int, datos: dict):
    distri = leer_todos_distri()
    distri_actualizado = None

    for idx, c in enumerate(distri):
        if c.id == id:
            if datos.get("nombre") is not None:
                distri[idx].nombre = datos["nombre"]
            if datos.get("direccion") is not None:
                distri[idx].direccion = datos["direccion"]
            distri_actualizado = distri[idx]
            break

    if distri_actualizado:
        with open(DISTRIBUIDORES, mode="w", newline="") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=CAMPOSDISTRI)
            writer.writeheader()
            for comp in distri:
                writer.writerow(comp.model_dump())
        return distri_actualizado

    return None

def eliminar_componente_mejorado(id: int):
    componentes = leer_todos_componentes()
    eliminado = None

    if not Path(ELIMINADOS_COMP).exists():
        with open(ELIMINADOS_COMP, mode="w", newline="") as archivo_eliminado:
            writer = csv.DictWriter(archivo_eliminado, fieldnames=CAMPOS)
            writer.writeheader()

    with open(COMPONENTES_DB, mode="w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
        writer.writeheader()

        for comp in componentes:
            if comp.id == id:
                eliminado = comp

                with open(ELIMINADOS_COMP, mode="a", newline="") as archivo_eliminado:
                    writer_eliminado = csv.DictWriter(archivo_eliminado, fieldnames=CAMPOS)
                    writer_eliminado.writerow(comp.model_dump())
                continue

            writer.writerow(comp.model_dump())

    return eliminado
#------------------------Operaciones Distribuidores------------------------------

def eliminar_distri_mejorado(id: int):
    distri = leer_todos_distri()
    eliminado = None

    if not Path(DISTRIBUIDORES).exists():
        with open(DISTRIBUIDORES, mode="w", newline="") as archivo_eliminado:
            writer = csv.DictWriter(archivo_eliminado, fieldnames=CAMPOSDISTRI)
            writer.writeheader()

    with open(DISTRIBUIDORES, mode="w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=CAMPOSDISTRI)
        writer.writeheader()

        for comp in distri:
            if comp.id == id:
                eliminado = comp

                with open(ELIMINADOS_DISTRI, mode="a", newline="") as archivo_eliminado:
                    writer_eliminado = csv.DictWriter(archivo_eliminado, fieldnames=CAMPOSDISTRI)
                    writer_eliminado.writerow(comp.model_dump())
                continue

            writer.writerow(comp.model_dump())

    return eliminado


