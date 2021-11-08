"""{MODIFICO TABLA CURSOS}

Revision ID: 15d8c8bb2378
Revises: a91b3500a77d
Create Date: 2021-11-07 15:56:13.022191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15d8c8bb2378'
down_revision = 'a91b3500a77d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('cursos', sa.Column("hashtags", sa.String, nullable=False))
    op.add_column('cursos', sa.Column("tipo", sa.String, nullable=False))
    op.add_column('cursos', sa.Column("examenes", sa.String, nullable=False))
    op.add_column('cursos', sa.Column("suscripcion", sa.String, nullable=False))
    op.add_column('cursos', sa.Column("ubicacion", sa.String, nullable=False))


def downgrade():
    op.drop_column('cursos', "hashtags")
    op.drop_column('cursos', "tipo")
    op.drop_column('cursos', "examenes")
    op.drop_column('cursos', "suscripcion")
    op.drop_column('cursos', "ubicacion")
