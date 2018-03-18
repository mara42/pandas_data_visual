import click
from Analysis import PoolAnalysis, AccidentAnalysis, BirdAnalysis
from collections import namedtuple
import matplotlib.pyplot as plt
import inspect
from re import sub


class Interface:

    def __init__(self):
        self._pool = PoolAnalysis()
        self._accidents = AccidentAnalysis()
        self._birds = BirdAnalysis()
    
    def get_plots(self, dataset):
        """function taken from:
        https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class"""
        return [func for func in dir(dataset if callable(
            getattr(dataset, func)) and not func.startswith("__")]
        
    def show_plots(self, dataset):
        cleaned_names=[
            f"{sub('_', ' ', name).capitalize()} [{index}]" for index, name in enumerate(dataset)]
        return """Choose what to plot by typing the number next to the name\n\n{}""".format('\n'.join(cleaned_names[1:]))

    def generate_chosen_plot(self, cls, plots, pick):
        """This cool function was taken from:
        https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string"""
        return getattr(cls, plots[pick])()

    def get_stats(self, cls):
        pass self.cls.get_description()

    select_data_UI = """Select the dataset to present by typing a letter from the list below.

    Traffic Accidents in Helsinki [a]
    Visits at the City of Vantaa swimming pools [b]
    Finnish bird nesting Atlas [c]
    """

    select_operation = """Select Operation to perform on this dataset:

        Column statistics [s]
        Plot              [p]
    """


    @staticmethod
    @click.command()
    @click.option('--letter', prompt=select_data_UI,
                help='Please type a, b or c and press enter to proceed',
                type=click.Choice(['a', 'b', 'c']))
    @click.option('--operation', prompt=select_operation,
                help='Please type s, p and press enter to proceed',
                type=click.Choice(['s', 'p']))
    def initial_selection(letter, operation):
        """Simple program that greets NAME"""
        sets = {'a': self._pool,
                'b': self._accidents
                'c': self._birds
                }
        choices = namedtuple('choice', ['dataset', 'operation'])
        return choices(sets[letter], operation)

    def choose_operation(self, dataset, operation):
        if operation == 's':
            dataset.get_description()
        else:
            

class CLI:

    @click.command()
    @click.option('--letter', prompt=select_data_UI,
                  help='Please type a, b or c and press enter to proceed',
                  type=click.Choice(['a', 'b', 'c']))
    def choose_dataset(self, letter):
        """Simple program that greets NAME"""
        sets = {'a': PoolAnalysis()
                'b': AccidentAnalysis()
                'c': BirdAnalysis()
                }
        self._chosen_set = sets[letter]

    # def choose_plot(self, ui, count):
    #     plot = click.prompt(ui, 
    #                         type=click.Choice(list(range(1, count+1))))
    #     if return plot
    
    # def generate_pool_plot(n):
    #     if n == 1:
    #         self._pool.
    #     if n == 2:



    # @cli.command()
    # def choose_operation():
    #     op = click.prompt(select_operation, 
    #                       type=click.Choice(['s', 'p']))
    #     return op
    
    # @cli.command()
    # def choose_pool_plot():
    #     op = click.prompt(choose_pool_plot,
    #                       type=click.Choice(['1', '2']))
    #     if op == 1:
    #         return self._pool.
    #     elif op == 2:
    #         return self._pool
    
    # @cli.command()
    # def choose_accident_plot():
    #     op = click.prompt(choose_accident_plot,
    #                       type=click.Choice(['1', '2']))
    #     if op == 1:
    #         return self._accidents
    #     elif op == 2:
    #         return self._accidents
        

    # @cli.command()
    # def choose_bird_plot():
    #     op = click.prompt(choose_bird_plot,
    #                       type=click.Choice(['1', '2']))
    #     if op == 1:


    


    
def cli_testing():
    
    @cli.command()
    def menu():
    """Shows a simple menu."""
    menu = 'main'
    while 1:
        if menu == 'main':
            click.echo('Main menu:')
            click.echo(select_data_UI)
            click.echo('  q: quit')
            char = click.getchar()
            if char == 'a':
                menu = 'pool'
            elif char == 'b'
                menu = 'acc'
            elif char == 'c':
                menu = 'bird'
            elif char == 'q':
                menu = 'quit'
            else:
                click.echo('Invalid input')

        elif menu == 'pool':
            click.echo(choose_pool_plot)
            click.echo('  b: back')
            char = click.getchar()
            if char == 'b':
                menu = 'main'
            else:
                click.echo('Invalid input')

        elif menu == 'acc':
            click.echo(choose_accident_plot)
            click.echo('  b: back')
            char = click.getchar()
            if char == 'b':
                menu = 'main'
            else:
                click.echo('Invalid input')

        elif menu == 'bird':
            click.echo(choose_bird_plot)
            click.echo('  b: back')
            char = click.getchar()
            if char == 'b':
                menu = 'main'
            else:
                click.echo('Invalid input')
        elif menu == 'quit':
            return




if __name__ == '__main__':
    dset, op = initial_selection()
    choose_operation(dset, op)

