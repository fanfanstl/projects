"""empty message

Revision ID: 6dff1fc4c2a1
Revises: 9f430ccb7afa
Create Date: 2018-10-17 21:42:03.464725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dff1fc4c2a1'
down_revision = '9f430ccb7afa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('axf_foodtype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('typeid', sa.Integer(), nullable=True),
    sa.Column('typename', sa.String(length=32), nullable=True),
    sa.Column('childtypenames', sa.String(length=255), nullable=True),
    sa.Column('typesort', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('axf_foodtype')
    # ### end Alembic commands ###
