"""add new columns on table

Revision ID: 5002f5376dc8
Revises: 111904aee50c
Create Date: 2022-05-25 12:57:11.413049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5002f5376dc8'
down_revision = '111904aee50c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column("posts", 'content')
    pass
