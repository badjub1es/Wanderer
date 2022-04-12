"""empty message

Revision ID: dddadf0e1e15
Revises: ffdc0a98111c
Create Date: 2022-04-12 13:13:12.018461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dddadf0e1e15'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type')
    )
    op.create_table('listings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('bed_number', sa.Integer(), nullable=False),
    sa.Column('bath_number', sa.Integer(), nullable=False),
    sa.Column('bedroom_number', sa.Integer(), nullable=False),
    sa.Column('maximum_guests', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('wifi_avail', sa.Boolean(), nullable=False),
    sa.Column('tv_avail', sa.Boolean(), nullable=False),
    sa.Column('kitchen_avail', sa.Boolean(), nullable=False),
    sa.Column('ac_avail', sa.Boolean(), nullable=False),
    sa.Column('washer_avail', sa.Boolean(), nullable=False),
    sa.Column('dryer_avail', sa.Boolean(), nullable=False),
    sa.Column('hair_dryer_avail', sa.Boolean(), nullable=False),
    sa.Column('parking_avail', sa.Boolean(), nullable=False),
    sa.Column('fridge_avail', sa.Boolean(), nullable=False),
    sa.Column('bbq_avail', sa.Boolean(), nullable=False),
    sa.Column('stove_avail', sa.Boolean(), nullable=False),
    sa.Column('pool_avail', sa.Boolean(), nullable=False),
    sa.Column('check_in', sa.String(length=255), nullable=False),
    sa.Column('check_out', sa.String(length=255), nullable=False),
    sa.Column('room_type_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['room_type_id'], ['room_types.id']),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=False),
    sa.Column('total_cost', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('phone_number', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_picture', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_picture')
    op.drop_column('users', 'phone_number')
    op.drop_table('reviews')
    op.drop_table('reservations')
    op.drop_table('images')
    op.drop_table('listings')
    op.drop_table('room_types')
    # ### end Alembic commands ###
