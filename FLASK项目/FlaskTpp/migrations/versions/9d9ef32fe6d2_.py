"""empty message

Revision ID: 9d9ef32fe6d2
Revises: 
Create Date: 2018-10-24 17:21:24.725055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d9ef32fe6d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('is_super', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cinema_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('is_verify', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('letter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('letter', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('letter')
    )
    op.create_table('movie_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('showname', sa.String(length=64), nullable=True),
    sa.Column('shownameen', sa.String(length=128), nullable=True),
    sa.Column('director', sa.String(length=64), nullable=True),
    sa.Column('leadingRole', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningmodel', sa.String(length=32), nullable=True),
    sa.Column('openday', sa.DateTime(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=256), nullable=True),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('p_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('p_name')
    )
    op.create_table('cinema_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=16), nullable=True),
    sa.Column('district', sa.String(length=16), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Float(), nullable=True),
    sa.Column('astrict', sa.Float(), nullable=True),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['c_user_id'], ['cinema_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cinema_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_cinema_id', sa.Integer(), nullable=True),
    sa.Column('c_movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_cinema_id'], ['cinema_user.id'], ),
    sa.ForeignKeyConstraint(['c_movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cinema_user_permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_user_id', sa.Integer(), nullable=True),
    sa.Column('c_permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_permission_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['c_user_id'], ['cinema_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('letter_id', sa.Integer(), nullable=True),
    sa.Column('c_id', sa.Integer(), nullable=True),
    sa.Column('c_parent_id', sa.Integer(), nullable=True),
    sa.Column('c_region_name', sa.String(length=16), nullable=True),
    sa.Column('c_city_code', sa.Integer(), nullable=True),
    sa.Column('c_pinyin', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['letter_id'], ['letter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hall',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('h_address_id', sa.Integer(), nullable=True),
    sa.Column('h_num', sa.Integer(), nullable=True),
    sa.Column('h_seats', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['h_address_id'], ['cinema_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hall_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('h_movie_id', sa.Integer(), nullable=True),
    sa.Column('h_hall_id', sa.Integer(), nullable=True),
    sa.Column('h_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['h_hall_id'], ['hall.id'], ),
    sa.ForeignKeyConstraint(['h_movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('o_user_id', sa.Integer(), nullable=True),
    sa.Column('o_hall_movie_id', sa.Integer(), nullable=True),
    sa.Column('o_time', sa.DateTime(), nullable=True),
    sa.Column('o_status', sa.Integer(), nullable=True),
    sa.Column('o_seats', sa.String(length=128), nullable=True),
    sa.Column('o_price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['o_hall_movie_id'], ['hall_movie.id'], ),
    sa.ForeignKeyConstraint(['o_user_id'], ['movie_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_order')
    op.drop_table('hall_movie')
    op.drop_table('hall')
    op.drop_table('city')
    op.drop_table('cinema_user_permission')
    op.drop_table('cinema_movie')
    op.drop_table('cinema_address')
    op.drop_table('permissions')
    op.drop_table('movies')
    op.drop_table('movie_user')
    op.drop_table('letter')
    op.drop_table('cinema_user')
    op.drop_table('admin_user')
    # ### end Alembic commands ###
