"""Alta colaboradores

Revision ID: d4963920f461
Revises: 67600b4caeff
Create Date: 2021-11-16 19:56:49.929563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

revision = 'd4963920f461'
down_revision = '67600b4caeff'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "colaboradores",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("fecha_creacion", sa.DateTime, nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime, nullable=True),
        sa.Column("id_curso", UUID(as_uuid=True), ForeignKey("cursos.id"), nullable=False, index=True),
        sa.Column("username", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("colaboradores")
