"""{CURSO_ID EN CURSADA DE VARCHAR A UUID}

Revision ID: 5aa674ccf3d6
Revises: 59376d4fb83b
Create Date: 2021-11-07 20:57:23.870907

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID
import uuid


# revision identifiers, used by Alembic.
revision = '5aa674ccf3d6'
down_revision = '59376d4fb83b'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('cursadas', 'curso_id')
    op.add_column('cursadas', sa.Column("curso_id", UUID(as_uuid=True), default=uuid.uuid4))


def downgrade():
    op.drop_column('cursadas', 'curso_id')
    op.add_column('cursadas', sa.Column("curso_id", sa.String, nullable=False))

