"""Agrego latitud y longitud al curso

Revision ID: 1b95cb407a82
Revises: 8974219bd844
Create Date: 2021-12-18 12:19:13.508435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b95cb407a82'
down_revision = '8974219bd844'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("cursos", sa.Column("latitud", sa.DECIMAL, nullable=True))
    op.add_column("cursos", sa.Column("longitud", sa.DECIMAL, nullable=True))


def downgrade():
    op.drop_column("cursos", "latitud")
    op.drop_column("cursos", "longitud")
