"""empty message

Revision ID: daa350e8784d
Revises: c260ce0a9935
Create Date: 2023-03-04 19:46:02.441205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daa350e8784d'
down_revision = 'c260ce0a9935'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('valla', sa.Column('province', sa.String(length=100), nullable=True))
    op.add_column('valla', sa.Column('address', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('valla', 'address')
    op.drop_column('valla', 'province')
    # ### end Alembic commands ###