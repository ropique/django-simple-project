"""user table

Revision ID: 8673bf2237a2
Revises: 9ead1de6ec17
Create Date: 2022-05-26 12:17:41.181326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8673bf2237a2'
down_revision = '9ead1de6ec17'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('company', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
