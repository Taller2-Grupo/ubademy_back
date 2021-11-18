# ubademy_back
Ubademy BackEnd

### Para levantar la base de datos usando docker:

Crear Volume: \
docker volume create --name postgresql-volume -d local

Levantar postgres usando volume: \
docker run --rm --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 -v postgresql-volume:/var/lib/postgresql/data postgres

### Agregar migration usando alembic:

1. alembic revision -m "{NOMBRE_MIGRATION}"
2. Ir a alembics/versions y completar la migration
3. alembic upgrade head

### Uso del .env
Para correr localmente se debe crear un archivo .env en el root, esta commiteado un .env-example que se puede copiar.
