"""add last columns

Revision ID: 827e2ae8fd9a
Revises: 50faf8496e18
Create Date: 2022-05-25 14:40:09.711443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '827e2ae8fd9a'
down_revision = '50faf8496e18'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False,
    server_default= 'TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone= True), nullable= False, 
    server_default= sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

    pass
