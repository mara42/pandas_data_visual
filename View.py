import click

select_data_UI = """Select the dataset to present by typing a letter from the list below.

DATA 1      [A]
DATA 2      [B]
DATA 3      [C]
"""

select_operation = """Select Operation to perform on this dataset:

    Column statistics [S]
    Plot              [P]
"""

choose_plot = """Choose what to plot:

    Option A
    Option B
    Option C
"""


@click.command()
@click.option('--letter', prompt=select_data_UI,
              help='Please type A, B or C and press enter to proceed')
@click.option('--operation', prompt=select_operation,
              help='Please type A, B or C and press enter to proceed')
def initial_selection(letter, operation):
    """Simple program that greets NAME"""
    click.echo(f"You chose {letter} and {operation}")


if __name__ == '__main__':
    initial_selection()

