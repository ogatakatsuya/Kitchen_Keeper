"""empty message

Revision ID: 2252374139ef
Revises: 8f810cdb2d2e
Create Date: 2024-02-21 16:24:56.344406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2252374139ef'
down_revision = '8f810cdb2d2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_foods_users', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.drop_constraint('fk_foods_users', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
