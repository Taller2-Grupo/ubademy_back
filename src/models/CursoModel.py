import datetime
import enum
from sqlalchemy import Column, Enum, String
from sqlalchemy.dialects import postgresql
from src.models.Entity import Entity
from src.db.database import Base


class EstadoCursoEnum(str, enum.Enum):
    activo = 'activo'
    bloqueado = 'bloqueado'
    eliminado = 'eliminado'


class Curso(Base, Entity):
    __tablename__ = "cursos"
    id_creador = Column(postgresql.UUID(as_uuid=True), nullable=False, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(Enum(EstadoCursoEnum), nullable=False)
    alumnos = {}

    def __init__(self, id_creador, titulo, descripcion):
        self.id_creador = id_creador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = EstadoCursoEnum.activo
        self.fecha_creacion = datetime.datetime.now()
        self.alumnos = {}

    def eliminar(self):
        self.estado = EstadoCursoEnum.eliminado
        self.actualizar()

    def cambiarTitulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def cambiarDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def agregarAlumno(self, alumno):
        self.alumnos[alumno.padron] = alumno

    def alumnoEstaInscripto(self, alumno):
        return alumno.padron in self.alumnos

    def obtenerListadoAlumnos(self):
        alumnos = []
        for alumno in self.alumnos:
            alumnos.append(self.alumnos[alumno])
        return alumnos

