"""add content table to post

Revision ID: 9ead1de6ec17
Revises: 55301fd0b7e2
Create Date: 2022-05-26 12:10:22.059260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ead1de6ec17'
down_revision = '55301fd0b7e2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
