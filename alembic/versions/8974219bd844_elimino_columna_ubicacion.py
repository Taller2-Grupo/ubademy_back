"""Elimino columna ubicacion

Revision ID: 8974219bd844
Revises: 76625e2552dd
Create Date: 2021-12-18 11:52:54.355463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8974219bd844'
down_revision = '76625e2552dd'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("cursos", "ubicacion")


def downgrade():
    op.add_column("cursos", sa.Column("ubicacion", sa.String, nullable=True))
