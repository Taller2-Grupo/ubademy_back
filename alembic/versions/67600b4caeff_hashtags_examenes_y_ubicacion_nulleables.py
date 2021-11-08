"""{HASHTAGS EXAMENES Y UBICACION NULLEABLES}

Revision ID: 67600b4caeff
Revises: 5aa674ccf3d6
Create Date: 2021-11-07 22:48:36.057639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67600b4caeff'
down_revision = '5aa674ccf3d6'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('cursos', 'hashtags', nullable=True)
    op.alter_column('cursos', 'examenes', nullable=True)
    op.alter_column('cursos', 'ubicacion', nullable=True)


def downgrade():
    op.alter_column('cursos', 'hashtags', nullable=False)
    op.alter_column('cursos', 'examenes', nullable=False)
    op.alter_column('cursos', 'ubicacion', nullable=False)
