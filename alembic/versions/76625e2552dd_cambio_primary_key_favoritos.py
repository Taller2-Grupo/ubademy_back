"""cambio primary key favoritos

Revision ID: 76625e2552dd
Revises: 360aaa3f8640
Create Date: 2021-12-09 18:37:32.948172

"""
from alembic import op
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '76625e2552dd'
down_revision = '360aaa3f8640'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("favoritos", "username")
    op.drop_column("favoritos", "curso_id")
    op.drop_column("favoritos", "id")
    op.add_column('favoritos', sa.Column("username", sa.String, nullable=False, primary_key=True))
    op.add_column('favoritos', sa.Column("curso_id", sa.String, nullable=False, primary_key=True))


def downgrade():
    op.drop_column("favoritos", "username")
    op.drop_column("favoritos", "curso_id")
    op.add_column('favoritos', sa.Column("username", sa.String))
    op.add_column('favoritos', sa.Column("curso_id", sa.String))
    op.add_column('favoritos', sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4))
