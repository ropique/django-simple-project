"""add foreign key for post table

Revision ID: 50faf8496e18
Revises: cf41813d683f
Create Date: 2022-05-25 14:29:44.579620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50faf8496e18'
down_revision = 'cf41813d683f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table= "posts", referent_table= "usrs", 
    local_cols= ['owner_id'], remote_cols= ['id'], ondelete= "CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name = "posts")
    op.drop_column('posts', 'owner_id')
    pass
