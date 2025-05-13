import csv
from pathlib import Path
from typing import Optional
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException
from models import Componente, ComponenteConId, ComponenteActualizar
from models import Distribuidores, DistriConId, DistriActualizado
from db import get_session

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola, mundo"}


@app.get("/componentes", response_model=list[ComponenteConId])
async def obtener_componentes_endpoint(session: AsyncSession = Depends(get_session)):
    componentes = await obtener_todos_componentes(session)
    return [ComponenteConId.from_orm(comp) for comp in componentes]

@app.get("/componentes/{id}", response_model=ComponenteConId)
async def obtener_componente_endpoint(id: int, session: AsyncSession = Depends(get_session)):
    componente = await obtener_componente(id, session)
    if not componente:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return ComponenteConId.from_orm(componente)

@app.post("/componentes", response_model=ComponenteConId)
async def crear_componente_endpoint(datos: Componente, session: AsyncSession = Depends(get_session)):
    nuevo_componente = await crear_componente(datos, session)
    return ComponenteConId.from_orm(nuevo_componente)

@app.put("/componentes/{id}", response_model=ComponenteConId)
async def actualizar_componente_endpoint(
    id: int, datos: ComponenteActualizar, session: AsyncSession = Depends(get_session)
):
    componente_actualizado = await actualizar_componente(id, datos, session)
    if not componente_actualizado:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return ComponenteConId.from_orm(componente_actualizado)

@app.delete("/componentes/{id}", response_model=ComponenteConId)
async def eliminar_componente_endpoint(id: int, session: AsyncSession = Depends(get_session)):
    componente_eliminado = await eliminar_componente(id, session)
    if not componente_eliminado:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return ComponenteConId.from_orm(componente_eliminado)


@app.get("/distribuidores", response_model=list[DistriConId])
async def obtener_distribuidores_endpoint(session: AsyncSession = Depends(get_session)):
    distribuidores = await obtener_todos_distribuidores(session)
    return [DistriConId.from_orm(dist) for dist in distribuidores]

@app.get("/distribuidores/{id}", response_model=DistriConId)
async def obtener_distribuidor_endpoint(id: int, session: AsyncSession = Depends(get_session)):
    distribuidor = await obtener_distribuidor(id, session)
    if not distribuidor:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")
    return DistriConId.from_orm(distribuidor)

@app.post("/distribuidores", response_model=DistriConId)
async def crear_distribuidor_endpoint(datos: Distribuidores, session: AsyncSession = Depends(get_session)):
    nuevo_distribuidor = await crear_distribuidor(datos, session)
    return DistriConId.from_orm(nuevo_distribuidor)

@app.put("/distribuidores/{id}", response_model=DistriConId)
async def actualizar_distribuidor_endpoint(
    id: int, datos: DistriActualizado, session: AsyncSession = Depends(get_session)
):
    distribuidor_actualizado = await actualizar_distribuidor(id, datos, session)
    if not distribuidor_actualizado:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")
    return DistriConId.from_orm(distribuidor_actualizado)

@app.delete("/distribuidores/{id}", response_model=DistriConId)
async def eliminar_distribuidor_endpoint(id: int, session: AsyncSession = Depends(get_session)):
    distribuidor_eliminado = await eliminar_distribuidor(id, session)
    if not distribuidor_eliminado:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")
    return DistriConId.from_orm(distribuidor_eliminado)


async def obtener_todos_componentes(session: AsyncSession) -> list[Componente]:
    result = await session.execute(select(Componente))
    return result.scalars().all()

async def obtener_componente(id: int, session: AsyncSession) -> Optional[Componente]:
    return await session.get(Componente, id)

async def crear_componente(datos: Componente, session: AsyncSession) -> Componente:
    nuevo_componente = Componente.from_orm(datos)
    session.add(nuevo_componente)
    await session.commit()
    await session.refresh(nuevo_componente)
    return nuevo_componente

async def actualizar_componente(id: int, datos: ComponenteActualizar, session: AsyncSession) -> Optional[Componente]:
    componente = await session.get(Componente, id)
    if not componente:
        return None

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(componente, key, value)

    session.add(componente)
    await session.commit()
    await session.refresh(componente)
    return componente

async def eliminar_componente(id: int, session: AsyncSession) -> Optional[Componente]:
    componente = await session.get(Componente, id)
    if not componente:
        return None

    await session.delete(componente)
    await session.commit()
    return componente

async def obtener_todos_distribuidores(session: AsyncSession) -> list[Distribuidores]:
    result = await session.execute(select(Distribuidores))
    return result.scalars().all()

async def obtener_distribuidor(id: int, session: AsyncSession) -> Optional[Distribuidores]:
    return await session.get(Distribuidores, id)

async def crear_distribuidor(datos: Distribuidores, session: AsyncSession) -> Distribuidores:
    nuevo_distribuidor = Distribuidores.from_orm(datos)
    session.add(nuevo_distribuidor)
    await session.commit()
    await session.refresh(nuevo_distribuidor)
    return nuevo_distribuidor

async def actualizar_distribuidor(id: int, datos: DistriActualizado, session: AsyncSession) -> Optional[Distribuidores]:
    distribuidor = await session.get(Distribuidores, id)
    if not distribuidor:
        return None

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(distribuidor, key, value)

    session.add(distribuidor)
    await session.commit()
    await session.refresh(distribuidor)
    return distribuidor

async def eliminar_distribuidor(id: int, session: AsyncSession) -> Optional[Distribuidores]:
    distribuidor = await session.get(Distribuidores, id)
    if not distribuidor:
        return None

    await session.delete(distribuidor)
    await session.commit()
    return distribuidor
