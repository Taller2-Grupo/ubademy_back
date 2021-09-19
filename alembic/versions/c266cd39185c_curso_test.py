"""Curso test

Revision ID: c266cd39185c
Revises: 
Create Date: 2021-09-19 17:56:39.094683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c266cd39185c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "cursos",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("cantidad_alumnos", sa.Integer, nullable=False),
        sa.Column("cantidad_condicionales", sa.Integer, nullable=False),
        sa.Column("nombre", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("cursos")

