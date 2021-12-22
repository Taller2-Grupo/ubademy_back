# ubademy_back
API de cursos para Ubademy

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

### Variables de entorno necesarias:

DATABASE_URL: URL de la base de datos postgres, si se usa heroku se setea automaticamente al agregarle una base de datos a la aplicacion.

TEST_DATABASE_URL: URL de la base de pruebas.

Para monitoreo datadog:

DD_API_KEY: api key de datadog

DD_DYNO_HOST=false

DD_APM_ENABLED=true

DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true