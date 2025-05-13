from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Distribuidores(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    direccion: str = Field(..., min_length=2, max_length=50)

class DistribuidorActualizar(SQLModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class Componente(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    tipo: str = Field(..., min_length=2, max_length=30)
    marca: str = Field(..., min_length=2, max_length=30)
    modelo: str = Field(..., min_length=2, max_length=30)


class ComponenteActualizado(SQLModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None

class ComponenteActualizar(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    tipo: Optional[str] = Field(None, min_length=2, max_length=30)
    marca: Optional[str] = Field(None, min_length=2, max_length=30)
    modelo: Optional[str] = Field(None, min_length=2, max_length=30)

class DistriActualizar(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    direccion: Optional[str] = Field(None, min_length=2, max_length=30)

class ComponenteConId(BaseModel):
    id: int
    nombre: str
    tipo: str
    marca: str
    modelo: str
    fecha_creacion: datetime
    fecha_modificacion: datetime

    class Config:
        from_attributes = True  

class DistriConId(BaseModel):
    id: int
    nombre: str
    direccion: str

    class Config:
        from_attributes = True  
