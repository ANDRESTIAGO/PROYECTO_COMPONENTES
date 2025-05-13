import csv
from pathlib import Path
from typing import Optional
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Componente, ComponenteConId, ComponenteActualizar
from models import Distribuidores, DistriConId, DistriActualizado

# Funciones relacionadas con componentes
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

# Funciones relacionadas con distribuidores
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
