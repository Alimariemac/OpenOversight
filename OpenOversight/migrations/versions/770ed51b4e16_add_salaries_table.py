"""Add salaries table

Revision ID: 770ed51b4e16
Revises: 9e2827dae28c
Create Date: 2019-01-25 15:47:13.812837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '770ed51b4e16'
down_revision = '9e2827dae28c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'salaries',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('officer_id', sa.Integer(), nullable=False),
        sa.Column('salary', sa.Numeric(), nullable=False),
        sa.Column('overtime_pay', sa.Numeric(), nullable=True),
        sa.Column('total_pay', sa.Numeric(), nullable=True),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('is_fiscal_year', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['officer_id'], ['officers.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_salary_overtime_pay'), 'salaries', ['overtime_pay'], unique=False)
    op.create_index(op.f('ix_salary_salary'), 'salaries', ['salary'], unique=False)
    op.create_index(op.f('ix_salary_total_pay'), 'salaries', ['total_pay'], unique=False)
    op.create_index(op.f('ix_salary_year'), 'salaries', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_salary_year'), table_name='salaries')
    op.drop_index(op.f('ix_salary_total_pay'), table_name='salaries')
    op.drop_index(op.f('ix_salary_salary'), table_name='salaries')
    op.drop_index(op.f('ix_salary_overtime_pay'), table_name='salaries')
    op.drop_table('salaries')
    # ### end Alembic commands ###
