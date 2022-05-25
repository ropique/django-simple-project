"""add new columns on table

Revision ID: 69009f277970
Revises: 5002f5376dc8
Create Date: 2022-05-25 13:56:26.181086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69009f277970'
down_revision = '5002f5376dc8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('category', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column("posts", 'category')
    pass
