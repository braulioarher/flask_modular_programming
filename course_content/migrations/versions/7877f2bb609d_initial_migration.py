"""Initial migration

Revision ID: 7877f2bb609d
Revises: 
Create Date: 2022-10-19 12:32:51.471189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7877f2bb609d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tagname', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blogpost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('pubish_date', sa.DateTime(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phoneno', sa.String(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blogpost_tags',
    sa.Column('blogpost_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blogpost_id'], ['blogpost.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogpost_tags')
    op.drop_table('contact')
    op.drop_table('blogpost')
    op.drop_table('user')
    op.drop_table('tag')
    # ### end Alembic commands ###
