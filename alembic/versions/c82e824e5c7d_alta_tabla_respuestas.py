"""Alta tabla respuestas

Revision ID: c82e824e5c7d
Revises: 3d261d2bdabe
Create Date: 2021-12-01 19:25:42.292955

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

# revision identifiers, used by Alembic.
revision = 'c82e824e5c7d'
down_revision = '3d261d2bdabe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "respuestas",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("fecha_creacion", sa.DateTime, nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime, nullable=True),
        sa.Column("id_examen_resuelto", UUID(as_uuid=True), ForeignKey("examenes_resueltos.id"), nullable=False, index=True),
        sa.Column("consigna", sa.String, nullable=False),
        sa.Column("resolucion", sa.String, nullable=False),
        sa.Column("estado", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("respuestas")
