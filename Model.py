import pandas as pd
 

class MotorAccidentData():

    def __init__(self):
        self.data = pd.read_csv('hki_liikenneonnettomuudet.csv',
                                ';',
                                # removed location data as it overcomplicates everything)
                                usecols=[0, 3, 4],
                                names=['Category', 'Severity', 'Year'],
                                skiprows=[0])

    def format_data(self):
        severity = {1: 'property damage',
                    2: "injury",
                    3: "fatality"}

        accident_type = {"JK": "pedestrian",
                            "PP": "bicycle",
                            "MP": "motorbike",
                            "MA": "car"}

        self.data['Category'] = self.data['Category'].map(accident_type)
        self.data['Severity'] = self.data['Severity'].map(severity)


class SwimmingPoolData():
    def __init__(self):
        self.data = pd.read_csv('Uimahallien kÑyntitapahtumatv2.csv',
                                     ';', encoding='ISO-8859-1')
    


class BirdData():

    def __init__(self):
        self.sightings = pd.read_csv('lintuatlas12.zip Folder/havainnot.csv',
                                     header=None,
                                     usecols=[0, 3, 4, 5, ], # removed location data as it overcomplicates everything
                                     names=['Species',
                                            'Nesting category 1974-79',
                                            'Nesting category 1986-89',
                                            'Nesting categories combined'])
        self.species = pd.read_csv('/Users/matt/Dropbox/University/2018 Spring/CS1527/mini-assessment/lintuatlas12.zip Folder/lajit.csv',
                                   encoding='ISO-8859-1',
                                   usecols=[0, 4],
                                   squeeze=True,
                                   index_col=0,
                                   header=None)
    
    def format_data(self):
        """Information on how to map the data was taken from
        the accompanying file 'ohje.txt'"""
        nesting_categories = {0: 'No sighting',
                              1: 'Unlikely nesting',
                              2: 'Possible nesting',
                              3: 'Likely nesting',
                              4: 'Certain Nesting'}

        self.sightings['Species'] = self.sightings['Species'].map(self.species)
        self.sightings['Nesting category 1974-79'] = self.sightings['Nesting category 1974-79'].map(
            nesting_categories)
        self.sightings['Nesting category 1986-89'] = self.sightings['Nesting category 1986-89'].map(
            nesting_categories)
        self.sightings['Nesting categories combined'] = self.sightings['Nesting categories combined'].map(
            nesting_categories)


# stats = BirdData()
# stats.rename_bird_sighting()

# print(stats.sightings)


# acc_stats = MotorAccidentData()
# acc_stats.format_data()
# print(acc_stats.data)

# pool_stats = SwimmingPoolData()
# print(pool_stats.data)
