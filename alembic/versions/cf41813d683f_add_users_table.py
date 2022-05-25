"""add users table

Revision ID: cf41813d683f
Revises: 69009f277970
Create Date: 2022-05-25 14:03:23.272051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf41813d683f'
down_revision = '69009f277970'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable = False), 
    sa.Column('email', sa.String(), nullable = False), sa.Column('password', sa.String(), nullable = False),
    sa.Column('company', sa.String(), nullable = False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
    server_default=sa.text('now()'), nullable = False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
