from Model import MotorAccidentData, SwimmingPoolData, BirdData


class PoolPlot(SwimmingPoolData):

    def ten_most_popular_products(self):
        products = self.data['Product']
        products.value_counts().head(10).plot(kind='bar')

    def product_popularity(self):
        def remove_day(date):
            _, month_year = date.split('.', 1)
            if len(month_year) == 6:
                month_year = '0'+month_year
            return month_year
        dates = self.data['Date']
        dates.apply(remove_day).value_counts().sort_index().plot()


class AccidentPlot(MotorAccidentData):

    def __init__(self):
        self.format_data()

    def fatality_by_category(self):
         self.data.loc[self.data['Severity'] ==
         'fatality']['Category'].value_counts().plot(kind='pie')

    def accidents_over_time_by_category(self):
        category_by_year = self.data[['Category', 'Year']]
        multi_index_data = category_by_year.groupby(
            df[['Category', 'Year']].columns.tolist(), as_index=False)
        multi_index_data.size().unstack(level=0).plot(subplots=True)

    def accidents_over_time_by_severity(self):
        severity_by_year = self.data[['Severity', 'Year']]
        multi_index_data = severity_by_year.groupby(
            self.data[['Severity', 'Year']].columns.tolist(), as_index=False).size()
        multi_index_data.unstack(level=0).plot(subplots=True)


class BirdPlot(BirdData):

    def __init__(self):
        self.format_data()

    def least_certainly_sighted(self):
        sighting_series = self.data.loc[self.data['Nesting categories combined'] ==
                    'Certain Nesting']['Species'].value_counts()
        sighting_series.loc[sighting_series < 100].plot('barh')
