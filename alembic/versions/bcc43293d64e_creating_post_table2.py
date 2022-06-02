"""creating post table2

Revision ID: bcc43293d64e
Revises: e001668b1b7d
Create Date: 2022-06-02 14:46:01.287848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcc43293d64e'
down_revision = 'e001668b1b7d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
