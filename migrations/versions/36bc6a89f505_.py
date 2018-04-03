"""empty message

Revision ID: 36bc6a89f505
Revises: afd3edfe6b04
Create Date: 2018-04-02 21:27:34.377395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36bc6a89f505'
down_revision = 'afd3edfe6b04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bus_route',
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.Column('bus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bus_id'], ['buses.id'], ),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], )
    )
    op.create_table('bus_stop_route',
    sa.Column('stop_id', sa.Integer(), nullable=True),
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], ),
    sa.ForeignKeyConstraint(['stop_id'], ['bus_stops.id'], )
    )
    op.drop_table('bus_stop-route')
    op.drop_table('bus-route')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bus-route',
    sa.Column('route_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bus_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['bus_id'], ['buses.id'], name='bus-route_bus_id_fkey'),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], name='bus-route_route_id_fkey')
    )
    op.create_table('bus_stop-route',
    sa.Column('stop_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('route_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], name='bus_stop-route_route_id_fkey'),
    sa.ForeignKeyConstraint(['stop_id'], ['bus_stops.id'], name='bus_stop-route_stop_id_fkey')
    )
    op.drop_table('bus_stop_route')
    op.drop_table('bus_route')
    # ### end Alembic commands ###