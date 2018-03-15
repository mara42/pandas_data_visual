from Data import MotorAccidentData, SwimmingPoolData, BirdData
import pandas as pd


class PoolAnalysis(SwimmingPoolData):

    def __init__(self):
        SwimmingPoolData.__init__(self)

    def ten_most_popular_products(self):
        products = self.data['Product']
        return products.value_counts().head(10)

    def sales_over_time(self):
        def get_months(date):
            _, month, _ = date.split('.', 2)
            if len(month) == 1:
                month = '0'+month
            return month
        df = self.data.copy()
        # dates = self.data['Date']
        df['Date'] = df['Date'].apply(get_months)  # .value_counts().sort_index()
        sales_by_month = df['Date'].value_counts()
        return pd.DataFrame(
            {'Month': sales_by_month.index.values,
             "Sales": sales_by_month
             }).sort_index()


class AccidentAnalysis(MotorAccidentData):

    def __init__(self):
        MotorAccidentData.__init__(self)
        self.format_data()

    def fatality_by_category(self):
        return self.data.loc[self.data['Severity'] ==
                            'fatality']['Category'].value_counts()  # .plot(kind='pie')

    def _accidents_over_time_by_category(self):
        category_by_year = self.data[['Category', 'Year']]
        multi_index_data = category_by_year.groupby(
            self.data[['Category', 'Year']].columns.tolist(), as_index=False)
        return multi_index_data.size().unstack(level=0)  # .plot(subplots=True)

    def _accidents_over_time_by_severity(self):
        severity_by_year = self.data[['Severity', 'Year']]
        multi_index_data = severity_by_year.groupby(
            self.data[['Severity', 'Year']].columns.tolist(), as_index=False).size()
        return multi_index_data.unstack(level=0)  # .plot(subplots=True)

    def accidents_over_time_by_severity_and_category(self):
        severity = self._accidents_over_time_by_severity()
        category = self._accidents_over_time_by_category()
        return severity.merge(category, left_index=True,
                              right_index=True)  # .plot(kind='line')


class BirdAnalysis(BirdData):

    def __init__(self):
        BirdData.__init__(self)
        self.format_data()

    # def sighting_counts(self):
    #     sighting_series = self.data.loc[self.data['Nesting categories combined'] ==
    #                                     'Certain Nesting']['Species'].value_counts()
    #     return sighting_series  # .loc[sighting_series < 100] # .plot('barh')

    def sighting_counts(self, atlas, certainty):
        sightings = self.data.loc[self.data[atlas] == certainty]  # ['Species']


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # test_bird = BirdAnalysis()
    # test_bird.least_certainly_sighted()

    # test_pool = PoolAnalysis()
    # test_pool.ten_most_popular_products()
    # test_pool.sales_over_time().plot(kind='bar')

    test_accident = AccidentAnalysis()
    # test_accident.fatality_by_category()
    # test_accident.accidents_over_time_by_category()
    # test_accident.accidents_over_time_by_severity().plot()
    test_accident.accidents_over_time_by_severity_and_category().plot()
    
    plt.show()

