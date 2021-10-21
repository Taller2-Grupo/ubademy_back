from unittest import TestCase
from src.models.CursoModel import Curso
from src.models.AlumnoModel import Alumno

class CursoTest(TestCase):

    def testVerificarAlumnoAgregadoACurso(self):
        curso = Curso(1, 'Taller II', 'Rojas, Agustín')
        alumno = Alumno('Renzo', 'Jacinto', '100627')
        curso.agregarAlumno(alumno)

        self.assertTrue(curso.alumnoEstaInscripto(alumno))

    def testVerificarAlumnosAgregadosACurso(self):
        curso = Curso(1, 'Taller II', 'Rojas, Agustín')
        alumno1 = Alumno('Renzo', 'Jacinto', '100627')
        alumno2 = Alumno('Agustin', 'Hejeij', '100628')
        alumno3 = Alumno('Francisco', 'Nasif', '100629')
        curso.agregarAlumno(alumno1)
        curso.agregarAlumno(alumno2)
        curso.agregarAlumno(alumno3)

        print([alumno1, alumno2, alumno3])
        print(curso.obtenerListadoAlumnos())
        self.assertEquals([alumno1, alumno2, alumno3], curso.obtenerListadoAlumnos())