from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from models import Componente, ComponenteConId, ComponenteActualizar
from models import Distribuidores, DistriConId, DistriActualizado
from db import get_session, init_db

app = FastAPI(title="API para Componentes y Distribuidores", docs_url="/docs")

# Inicialización de la base de datos
@app.on_event("startup")
async def on_startup():
    await init_db()

# Endpoints de Componentes
@app.get("/componentes", response_model=List[ComponenteConId])
async def obtener_componentes(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Componente))
    componentes = result.scalars().all()
    return [ComponenteConId.from_orm(comp) for comp in componentes]

@app.get("/componentes/{id}", response_model=ComponenteConId)
async def obtener_componente(id: int, session: AsyncSession = Depends(get_session)):
    componente = await session.get(Componente, id)
    if not componente:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return ComponenteConId.from_orm(componente)

@app.post("/componentes", response_model=ComponenteConId)
async def crear_componente(datos: Componente, session: AsyncSession = Depends(get_session)):
    nuevo_componente = Componente.from_orm(datos)
    session.add(nuevo_componente)
    await session.commit()
    await session.refresh(nuevo_componente)
    return ComponenteConId.from_orm(nuevo_componente)

@app.put("/componentes/{id}", response_model=ComponenteConId)
async def actualizar_componente(
    id: int, datos: ComponenteActualizar, session: AsyncSession = Depends(get_session)
):
    componente = await session.get(Componente, id)
    if not componente:
        raise HTTPException(status_code=404, detail="Componente no encontrado")

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(componente, key, value)

    session.add(componente)
    await session.commit()
    await session.refresh(componente)
    return ComponenteConId.from_orm(componente)

@app.delete("/componentes/{id}", response_model=ComponenteConId)
async def eliminar_componente(id: int, session: AsyncSession = Depends(get_session)):
    componente = await session.get(Componente, id)
    if not componente:
        raise HTTPException(status_code=404, detail="Componente no encontrado")

    await session.delete(componente)
    await session.commit()
    return ComponenteConId.from_orm(componente)

# Endpoints de Distribuidores
@app.get("/distribuidores", response_model=List[DistriConId])
async def obtener_distribuidores(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Distribuidores))
    distribuidores = result.scalars().all()
    return [DistriConId.from_orm(dist) for dist in distribuidores]

@app.get("/distribuidores/{id}", response_model=DistriConId)
async def obtener_distribuidor(id: int, session: AsyncSession = Depends(get_session)):
    distribuidor = await session.get(Distribuidores, id)
    if not distribuidor:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")
    return DistriConId.from_orm(distribuidor)

@app.post("/distribuidores", response_model=DistriConId)
async def crear_distribuidor(datos: Distribuidores, session: AsyncSession = Depends(get_session)):
    nuevo_distribuidor = Distribuidores.from_orm(datos)
    session.add(nuevo_distribuidor)
    await session.commit()
    await session.refresh(nuevo_distribuidor)
    return DistriConId.from_orm(nuevo_distribuidor)

@app.put("/distribuidores/{id}", response_model=DistriConId)
async def actualizar_distribuidor(
    id: int, datos: DistriActualizado, session: AsyncSession = Depends(get_session)
):
    distribuidor = await session.get(Distribuidores, id)
    if not distribuidor:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(distribuidor, key, value)

    session.add(distribuidor)
    await session.commit()
    await session.refresh(distribuidor)
    return DistriConId.from_orm(distribuidor)

@app.delete("/distribuidores/{id}", response_model=DistriConId)
async def eliminar_distribuidor(id: int, session: AsyncSession = Depends(get_session)):
    distribuidor = await session.get(Distribuidores, id)
    if not distribuidor:
        raise HTTPException(status_code=404, detail="Distribuidor no encontrado")

    await session.delete(distribuidor)
    await session.commit()
    return DistriConId.from_orm(distribuidor)
