from starlette.responses import JSONResponse
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from db import get_session, init_db
from models import (
    ComponenteConId,
    Componente,
    ComponenteActualizado,
    Distribuidores,
    DistribuidorActualizar,
    DistriConId,
)
from operations import *


app = FastAPI()


@app.get("/optener_todos_los_componentes", response_model=list[ComponenteConId])
async def obtener_todos(session: AsyncSession = Depends(get_session)):
    componentes = await obtener_componentes(session)
    return [ComponenteConId.from_orm(comp) for comp in componentes]


@app.get("/optener_un_componente/{componente_id}", response_model=ComponenteConId)
async def obtener_uno(componente_id: int, session: AsyncSession = Depends(get_session)):
    comp = await obtener_componente(componente_id, session)
    if not comp:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return ComponenteConId.from_orm(comp)


@app.get("/optener_componente_con_atributo/{componente_tipo}/{componente_modelo}", response_model=ComponenteConId)
async def obtener_atributo_componente(
    componente_tipo: str,
    componente_modelo: str,
    session: AsyncSession = Depends(get_session),
):
    comp = await buscar_componente(componente_tipo, componente_modelo, session)
    if not comp:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return ComponenteConId.from_orm(comp)


@app.get("/optener_todos_los_distribuidores", response_model=list[DistriConId])
async def obtener_todos_distribuidores(session: AsyncSession = Depends(get_session)):
    distribuidores = await obtener_distribuidores(session)
    return [DistriConId.from_orm(dist) for dist in distribuidores]


@app.get("/optener_un_distribuidor/{distribuidor_id}", response_model=DistriConId)
async def obtener_un_distribuidor(distribuidor_id: int, session: AsyncSession = Depends(get_session)):
    dist = await obtener_distribuidor(distribuidor_id, session)
    if not dist:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")
    return DistriConId.from_orm(dist)


@app.post("/agregar_componente", response_model=ComponenteConId)
async def agregar_componente(comp: Componente, session: AsyncSession = Depends(get_session)):
    nuevo_comp = await crear_componente(comp, session)
    return ComponenteConId.from_orm(nuevo_comp)


@app.post("/agregar_distribuidor", response_model=DistriConId)
async def agregar_distribuidor(distri: Distribuidores, session: AsyncSession = Depends(get_session)):
    nuevo_distri = await crear_distribuidor(distri, session)
    return DistriConId.from_orm(nuevo_distri)


@app.put("/actualizar_componente/{componente_id}", response_model=ComponenteConId)
async def actualizar_componente(
    componente_id: int,
    comp_update: ComponenteActualizado,
    session: AsyncSession = Depends(get_session),
):
    actualizado = await actualizar_componente(componente_id, comp_update, session)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Componente no modificado")
    return ComponenteConId.from_orm(actualizado)


@app.put("/actualizar_distribuidor/{distribuidor_id}", response_model=DistriConId)
async def actualizar_distribuidor(
    distribuidor_id: int,
    comp_update: DistribuidorActualizar,
    session: AsyncSession = Depends(get_session),
):
    actualizado = await actualizar_distribuidor(distribuidor_id, comp_update, session)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Distribuidor no modificado")
    return DistriConId.from_orm(actualizado)


@app.delete("/eliminar_componente/{componente_id}", response_model=ComponenteConId)
async def eliminar_un_componente(componente_id: int, session: AsyncSession = Depends(get_session)):
    eliminado = await eliminar_componente(componente_id, session)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Componente no eliminado")
    return ComponenteConId.from_orm(eliminado)


@app.delete("/eliminar_distribuidor/{distribuidor_id}", response_model=DistriConId)
async def eliminar_un_distribuidor(distribuidor_id: int, session: AsyncSession = Depends(get_session)):
    eliminado = await eliminar_distribuidor(distribuidor_id, session)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Distribuidor no eliminado")
    return DistriConId.from_orm(eliminado)
