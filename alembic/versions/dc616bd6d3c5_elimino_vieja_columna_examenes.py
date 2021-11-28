"""Elimino vieja columna examenes

Revision ID: dc616bd6d3c5
Revises: 9398f2c11ccf
Create Date: 2021-11-28 18:04:03.957020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc616bd6d3c5'
down_revision = '9398f2c11ccf'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("cursos", "examenes")


def downgrade():
    op.add_column("cursos", "examenes")
