from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class ComponenteBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float

class Componente(ComponenteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ComponenteConId(ComponenteBase):
    id: int

    class Config:
        from_attributes = True

class ComponenteActualizar(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None

    class Config:
        from_attributes = True
