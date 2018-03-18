import click
from Analysis import PoolAnalysis, AccidentAnalysis, BirdAnalysis
import matplotlib.pyplot as plt
from re import sub


class UI:

    def __init__(self):
        self._pool = PoolAnalysis()
        self._accidents = AccidentAnalysis() # bugged showing inherited methods
        self._birds = BirdAnalysis()
        self.select_data_UI = (f"{UI.divider}\nMAIN MENU:\n\nSelect the dataset to present "
                               f"by typing a letter from the list below.\n\nVisits at the City of Vantaa "
                               f"swimming pools [a]\nTraffic Accidents in Helsinki [b]\nFinnish bird nesting "
                               f"Atlas [c]\n\n(type 'q' for quit)\n")
        self.select_operation = (f"{UI.divider}\nOPERATION MENU:\n\nSelect Operation to perform on this dataset: "
                                 f"\n\nColumn statistics [s]\nPlot [p]\n\n(type 'b' for back or 'q' for quit)\n")
        self.chosen_data_set = None
    
    divider = '='*40
    
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
        return ("{}\nPLOT MENU:\n\nChoose what to plot by typing the number next to the name\n\n{}"
                "\n(type 'b' for back or 'q' for quit)\n").format(UI.divider, '\n'.join(cleaned_names))

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
        menu = 'datasets'
        while 1:
            if menu == 'datasets':
                dataset = click.prompt(interface.select_data_UI,
                                        type=click.Choice(['a', 'b', 'c', 'q']))
                if dataset == 'q':
                    menu = 'quit'
                else:
                    interface.set_chosen_data_set(dataset)
                    menu = 'operations'
            elif menu == 'operations':
                op = click.prompt(interface.select_operation,
                                  type=click.Choice(['s', 'p', 'b', 'q']))
                if op == 'q':
                    menu = 'quit'
                elif op == 'b':
                    menu = 'datasets' 
                elif op == 's':
                    print(interface.chosen_data_set.get_description(), '\n')
                elif op == 'p':
                    menu = 'plots'
            elif menu == 'plots':
                names = interface.get_plot_names(interface.chosen_data_set)
                choices = [str(n) for n in range(len(names))]
                choices.extend(['b', 'q'])
                plot_choice = click.prompt(interface.generate_plot_UI(names),
                                           type=click.Choice(choices))
                if plot_choice == 'q':
                    menu = 'quit'
                elif plot_choice == 'b':
                    menu = 'operations'
                else:
                    interface.generate_chosen_plot(
                        interface.chosen_data_set, names, int(plot_choice))
                    plt.show()
            elif menu == 'quit':
                return

    a = UI()
    plotting_ui(a)

