"""empty message

Revision ID: 76ac506b822f
Revises: b5c3041bef18
Create Date: 2019-03-16 16:52:56.195603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76ac506b822f'
down_revision = 'b5c3041bef18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scans', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column('scans', sa.Column('tag_on', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('scans', 'tag_on')
    op.drop_column('scans', 'created')
    # ### end Alembic commands ###
