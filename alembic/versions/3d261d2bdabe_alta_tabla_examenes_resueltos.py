"""Alta tabla examenes resueltos

Revision ID: 3d261d2bdabe
Revises: dc616bd6d3c5
Create Date: 2021-12-01 19:19:31.782001

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


# revision identifiers, used by Alembic.
revision = '3d261d2bdabe'
down_revision = 'dc616bd6d3c5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "examenes_resueltos",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("fecha_creacion", sa.DateTime, nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime, nullable=True),
        sa.Column("id_cursada", UUID(as_uuid=True), ForeignKey("cursadas.id"), nullable=False, index=True),
        sa.Column("id_examen", UUID(as_uuid=True), ForeignKey("examenes.id"), nullable=False, index=True),
        sa.Column("corrector", sa.String, nullable=True),
        sa.Column("estado", sa.String, nullable=False),
        sa.Column("nota", sa.INT, nullable=True)
    )


def downgrade():
    op.drop_table("examenes_resueltos")
