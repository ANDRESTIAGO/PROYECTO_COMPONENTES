from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Distribuidores(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    direccion: str

class DistribuidorActualizar(SQLModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class Componente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    tipo: str
    marca: str
    modelo: str
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
    fecha_modificacion: datetime = Field(default_factory=datetime.utcnow)

class ComponenteActualizar(SQLModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
