"""add last columns to post table

Revision ID: d8637b87d309
Revises: 3129273900c1
Create Date: 2022-05-26 12:33:27.799501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8637b87d309'
down_revision = '3129273900c1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
    'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
    'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
