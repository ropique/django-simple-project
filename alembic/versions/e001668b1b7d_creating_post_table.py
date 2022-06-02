"""creating post table

Revision ID: e001668b1b7d
Revises: 
Create Date: 2022-06-02 14:32:39.940793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e001668b1b7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
    primary_key=True), sa.Column('title', sa.String(), nullable=False), sa.Column('category', sa.String(), nullable=False))
    pass
    


def downgrade():
    op.drop_table('posts')
    pass
