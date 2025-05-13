
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from models import *
from operations import *

app = FastAPI()

@app.get("/optener_todos_los_componentes", response_model=list[ComponenteConId])
async def obtener_todos():
    return leer_todos_componentes()

@app.get("/mostrar_componentes_eliminados", response_model=list[ComponenteConId])
async def obtener_todos_los_eliminados_():
    return leer_todos_componentes_eliminados()

@app.get("/optener_un_componente/{componente_id}", response_model=ComponenteConId)
async def obtener_uno(componente_id: int):
    comp = leer_componente(componente_id)
    if not comp:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return comp
@app.get("/optener_componente_con_atributo/{componente_tipo}/{componente_modelo}", response_model=ComponenteConId)
async def obtener_atributo_componente(componente_tipo:str, componente_modelo: str):
    comp = busqueda_atributo_componente(componente_tipo, componente_modelo)
    if not comp:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return comp

@app.get("/opetener_todos_los_distribuidores", response_model=list[DistriConId])
async def obtener_todos_distribuidores():
    return leer_todos_distri()

@app.get("/optener_distribuidores_eliminados", response_model=list[DistriConId])
async def obtener_todos_los_eliminados_distri():
    return leer_todos_distri_eliminados()

@app.get("/optener_un_distribuidor/{componente_id}", response_model=DistriConId)
async def obtener_un_distribuidor(componente_id: int):
    comp = leer_distri(componente_id)
    if not comp:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")
    return comp

@app.get("/optener_distribuidor_con_atributo/{distribuidor_nombre}", response_model=DistriConId)
async def obtener_atributo_distri(distribuidor_nombre:str):
    comp = busqueda_atributo_distri(distribuidor_nombre)
    if not comp:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")
    return comp

@app.post("/agregar_componente", response_model=ComponenteConId)
def agregar_componente(comp: Componente):
    return nuevo_componente(comp)

@app.post("/agregar_distribuidor", response_model=DistriConId)
def agregar_distribuidor(comp: Distribuidores):
    return nuevo_distri(comp)

@app.put("/actualizar_componente/{componente_id}", response_model=ComponenteConId)
def actualizar_componente(componente_id: int, comp_update: ComponenteActualizado):
    actualizado = modificar_componente(componente_id, comp_update.model_dump(exclude_unset=True))
    if not actualizado:
        raise HTTPException(status_code=404, detail="Componente no modificado")
    return actualizado

@app.put("/actualizar_distribuidor/{distribuidor_id}", response_model=DistriConId)
def actualizar_distribuidor(distribuidor_id: int, comp_update: DistriActualizado):
    actualizado = modificar_distri(distribuidor_id, comp_update.model_dump(exclude_unset=True))
    if not actualizado:
        raise HTTPException(status_code=404, detail="Distribuidor no modificado")
    return actualizado

@app.delete("/eliminar_componente/{componente_id}", response_model=ComponenteConId)
def eliminar_un_componente_mejorado(componente_id: int):
    eliminado = eliminar_componente_mejorado(componente_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Componente no eliminado")
    return eliminado
@app.delete("/eliminar_distribuidor/{distribuidor_id}", response_model=DistriConId)
def eliminar_un_distribuidor_mejorado(distribuidor_id: int):
    eliminado = eliminar_distri_mejorado(distribuidor_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Distribuidor no eliminado")
    return eliminado

@app.get("/")
async def inicio():
    return {"mensaje": "API de compatibilidad de componentes"}

@app.exception_handler(HTTPException)
async def manejador_excepciones(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "mensaje": "Ocurrió un error",
            "detalle": exc.detail,
            "ruta": str(request.url)
        },
    )
