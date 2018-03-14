from Model import MotorAccidentData, SwimmingPoolData, BirdData
import matplotlib.pyplot as plt


class PoolPlot(SwimmingPoolData):

    def __init__(self):
        SwimmingPoolData.__init__(self)

    def ten_most_popular_products(self):
        products = self.data['Product']
        products.value_counts().head(10).plot(kind='bar')

    def product_popularity(self):
        # missing dates from the bottom
        def remove_day(date):
            _, month_year = date.split('.', 1)
            if len(month_year) == 6:
                month_year = '0'+month_year
            return month_year
        dates = self.data['Date']
        dates.apply(remove_day).value_counts().sort_index().plot()


class AccidentPlot(MotorAccidentData):

    def __init__(self):
        MotorAccidentData.__init__(self)
        self.format_data()

    def fatality_by_category(self):
        self.data.loc[self.data['Severity'] ==
        'fatality']['Category'].value_counts().plot(kind='pie')

    def accidents_over_time_by_category(self):
        category_by_year = self.data[['Category', 'Year']]
        multi_index_data = category_by_year.groupby(
            self.data[['Category', 'Year']].columns.tolist(), as_index=False)
        multi_index_data.size().unstack(level=0).plot(subplots=True)

    def accidents_over_time_by_severity(self):
        severity_by_year = self.data[['Severity', 'Year']]
        multi_index_data = severity_by_year.groupby(
            self.data[['Severity', 'Year']].columns.tolist(), as_index=False).size()
        multi_index_data.unstack(level=0).plot(subplots=True)


class BirdPlot(BirdData):

    def __init__(self):
        BirdData.__init__(self)
        self.format_data()

    def least_certainly_sighted(self):
        sighting_series = self.data.loc[self.data['Nesting categories combined'] ==
                    'Certain Nesting']['Species'].value_counts()
        sighting_series.loc[sighting_series < 100].plot('barh')


if __name__ == '__main__':
    test_bird = BirdPlot()
    test_bird.least_certainly_sighted()

    test_pool = PoolPlot()
    test_pool.ten_most_popular_products()
    test_pool.product_popularity()

    test_accident = AccidentPlot()
    test_accident.fatality_by_category()
    test_accident.accidents_over_time_by_category()
    test_accident.accidents_over_time_by_severity()

    plt.show()

