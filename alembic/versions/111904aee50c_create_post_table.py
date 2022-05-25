"""create post table

Revision ID: 111904aee50c
Revises: 
Create Date: 2022-05-25 12:13:31.161542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '111904aee50c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), 
    nullable = False, primary_key = True), sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
