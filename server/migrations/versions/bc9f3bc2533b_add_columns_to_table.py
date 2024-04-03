"""add columns to table

Revision ID: bc9f3bc2533b
Revises: 75a23a1b9adc
Create Date: 2024-04-02 22:33:04.102052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc9f3bc2533b'
down_revision = '75a23a1b9adc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_column('price')
        batch_op.drop_column('image')
        batch_op.drop_column('name')

    # ### end Alembic commands ###