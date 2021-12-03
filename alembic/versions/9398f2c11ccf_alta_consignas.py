"""Alta consignas

Revision ID: 9398f2c11ccf
Revises: 2f9b6fb06133
Create Date: 2021-11-28 15:17:16.443948

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

# revision identifiers, used by Alembic.
revision = '9398f2c11ccf'
down_revision = '2f9b6fb06133'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "consignas",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("fecha_creacion", sa.DateTime, nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime, nullable=True),
        sa.Column("id_examen", UUID(as_uuid=True), ForeignKey("examenes.id"), nullable=False, index=True),
        sa.Column("enunciado", sa.String, nullable=False),
        sa.Column("puntaje", sa.INT, nullable=False)
    )


def downgrade():
    op.drop_table("consignas")
