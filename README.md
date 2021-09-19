# ubademy_back
Ubademy BackEnd

### Para levantar la base de datos usando docker:

Crear Volume: \
docker volume create --name postgresql-volume -d local

Levantar postgres usando volume: \
docker run --rm --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 -v postgresql-volume:/var/lib/postgresql/data postgres