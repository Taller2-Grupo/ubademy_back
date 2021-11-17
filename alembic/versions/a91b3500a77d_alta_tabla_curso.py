"""Alta tabla Curso

Revision ID: a91b3500a77d
Revises: 
Create Date: 2021-09-25 22:50:47.853448

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

import uuid

# revision identifiers, used by Alembic.
revision = 'a91b3500a77d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "cursos",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("fecha_creacion", sa.DateTime, nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime, nullable=True),
        sa.Column("id_creador", sa.String, nullable=False, index=True),
        sa.Column("titulo", sa.String, nullable=False),
        sa.Column("descripcion", sa.String, nullable=False),
        sa.Column("estado", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("cursos")
