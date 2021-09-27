import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects import postgresql
from datetime import datetime


class Entity:
    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    fecha_creacion = Column(DateTime, nullable=False, default=datetime.now())
    fecha_actualizacion = Column(DateTime, nullable=True)

    def actualizar(self):
        self.fecha_actualizacion = datetime.utcnow()
