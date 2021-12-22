"""{AGREGO TABLA CURSADAS}

Revision ID: 59376d4fb83b
Revises: 15d8c8bb2378
Create Date: 2021-11-07 16:07:15.967480

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

import uuid


# revision identifiers, used by Alembic.
revision = '59376d4fb83b'
down_revision = '15d8c8bb2378'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "cursadas",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("fecha_creacion", sa.DateTime, nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime, nullable=True),
        sa.Column("username", sa.String, nullable=False),
        sa.Column("curso_id", sa.String, nullable=False),
        sa.Column("estado", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("cursadas")
