"""empty message

Revision ID: bde7d853d7d0
Revises: b3e5acd0f1c0
Create Date: 2022-10-21 14:52:56.137536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bde7d853d7d0'
down_revision = 'b3e5acd0f1c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_name', sa.String(length=128), nullable=False),
    sa.Column('teacher_subject', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher')
    # ### end Alembic commands ###
