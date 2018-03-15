import click
from Analysis import PoolAnalysis, AccidentAnalysis, BirdAnalysis
from collections import namedtuple


select_data_UI = """Select the dataset to present by typing a letter from the list below.

DATA 1      [a]
DATA 2      [b]
DATA 3      [c]
"""

select_operation = """Select Operation to perform on this dataset:

    Column statistics [s]
    Plot              [p]
"""

choose_pool_plot = """Choose what to plot:

    Option A
    Option B
    Option C
"""
choose_accident_plot = """Choose what to plot:

    Option A
    Option B
    Option C
"""
choose_bird_plot = """Choose what to plot:

    Option A
    Option B
    Option C
"""


@click.command()
@click.option('--letter', prompt=select_data_UI,
              help='Please type a, b or c and press enter to proceed',
              type=click.Choice(['a', 'b', 'c']))
@click.option('--operation', prompt=select_operation,
              help='Please type s, p and press enter to proceed',
              type=click.Choice(['s', 'p']))
def initial_selection(letter, operation):
    """Simple program that greets NAME"""
    choices = namedtuple('choice', ['dataset', 'operation'])
    return choices(letter, operation)


def choose_operation(**kwargs):
        if dataset == 'a':
            if operation == s:
                pool = PoolAnalaysis()
                pool.get_describtion()
            else:

        elif dataset == 'b':
            pass
        elif dataset == 'c':
            pass
    





if __name__ == '__main__':
    initial_selection()

