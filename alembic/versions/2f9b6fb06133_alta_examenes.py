"""Alta examenes

Revision ID: 2f9b6fb06133
Revises: d4963920f461
Create Date: 2021-11-28 15:05:34.340248

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
# revision identifiers, used by Alembic.
revision = '2f9b6fb06133'
down_revision = 'd4963920f461'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "examenes",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("fecha_creacion", sa.DateTime, nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime, nullable=True),
        sa.Column("id_curso", UUID(as_uuid=True), ForeignKey("cursos.id"), nullable=False, index=True),
        sa.Column("nombre", sa.String, nullable=False),
        sa.Column("estado", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("examenes")
