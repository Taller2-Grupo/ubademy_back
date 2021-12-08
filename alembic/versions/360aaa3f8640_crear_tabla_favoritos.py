"""crear tabla favoritos

Revision ID: 360aaa3f8640
Revises: c82e824e5c7d
Create Date: 2021-12-08 15:45:29.673797

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid


# revision identifiers, used by Alembic.
revision = '360aaa3f8640'
down_revision = 'c82e824e5c7d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "favoritos",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column("username", sa.String, nullable=False),
        sa.Column("curso_id", sa.String, nullable=False)
    )


def downgrade():
    op.drop_table("favoritos")
