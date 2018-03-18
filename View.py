import click
from Analysis import PoolAnalysis, AccidentAnalysis, BirdAnalysis
import matplotlib.pyplot as plt
from re import sub


class UI:

    def __init__(self):
        self._pool = PoolAnalysis()
        self._accidents = AccidentAnalysis() # bugged showing inherited methods
        self._birds = BirdAnalysis()
        self.select_data_UI = "MAIN MENU:\n\nSelect the dataset to present by typing a letter from the list below.\n\nVisits at the City of Vantaa swimming pools [a]\nTraffic Accidents in Helsinki [b]\nFinnish bird nesting Atlas [c]\n"
        self.select_operation = "OPERATION MENU:\n\nSelect Operation to perform on this dataset: \n\nColumn statistics [s]\nPlot [p]\n"
        self.chosen_data_set = None
    
    def set_chosen_data_set(self, letter):
        sets = {'a': self._pool,
                'b': self._accidents,
                'c': self._birds
                }
        self.chosen_data_set = sets[letter]
            
    def get_plot_names(self, dataset):
        """function taken from:
        https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class"""
        return [func for func in dir(dataset) if callable(
            getattr(dataset, func)) and (not func.startswith("_") and not func == 'get_description')]
        
    def generate_plot_UI(self, dataset_names):
        cleaned_names = [
            f"{sub('_', ' ', name).capitalize()} [{index}]" for index, name in enumerate(dataset_names)]
        return """PLOT MENU:\n\nChoose what to plot by typing the number next to the name\n\n{}\n""".format('\n'.join(cleaned_names))

    def generate_chosen_plot(self, dataset, plots, pick):
        """This cool function was taken from:
        https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string"""
        return getattr(dataset, plots[pick])(plot=True)

    
# def cli_testing():
    
#     @cli.command()
#     def menu():
#     """Shows a simple menu."""
#     menu = 'main'
#     while 1:
#         if menu == 'main':
#             click.echo('Main menu:')
#             click.echo(select_data_UI)
#             click.echo('  q: quit')
#             char = click.getchar()
#             if char == 'a':
#                 menu = 'pool'
#             elif char == 'b'
#                 menu = 'acc'
#             elif char == 'c':
#                 menu = 'bird'
#             elif char == 'q':
#                 menu = 'quit'
#             else:
#                 click.echo('Invalid input')

#         elif menu == 'pool':
#             click.echo(choose_pool_plot)
#             click.echo('  b: back')
#             char = click.getchar()
#             if char == 'b':
#                 menu = 'main'
#             else:
#                 click.echo('Invalid input')

#         elif menu == 'acc':
#             click.echo(choose_accident_plot)
#             click.echo('  b: back')
#             char = click.getchar()
#             if char == 'b':
#                 menu = 'main'
#             else:
#                 click.echo('Invalid input')

#         elif menu == 'bird':
#             click.echo(choose_bird_plot)
#             click.echo('  b: back')
#             char = click.getchar()
#             if char == 'b':
#                 menu = 'main'
#             else:
#                 click.echo('Invalid input')
#         elif menu == 'quit':
#             return




if __name__ == '__main__':
    
    def plotting_ui(interface):
        menu = 'main'
        while 1:
            if menu == 'main':
                dataset = click.prompt(interface.select_data_UI,
                                        type=click.Choice(['a', 'b', 'c', 'q']))
                interface.set_chosen_data_set(dataset)
                op = click.prompt(interface.select_operation,
                                  type=click.Choice(['s', 'p', 'b', 'q']))
            if op == 's':
                print(interface.chosen_data_set.get_description(), '\n')
            elif op == 'p':
                names = interface.get_plot_names(interface.chosen_data_set)
                choices = [str(n) for n in range(len(names))]
                choices.extend(['b', 'q'])
                print(names)
                plot_choice = click.prompt(interface.generate_plot_UI(names),
                                           type=click.Choice(choices))
                interface.generate_chosen_plot(
                    interface.chosen_data_set, names, int(plot_choice))
                plt.show()

    a = UI()
    plotting_ui(a)

