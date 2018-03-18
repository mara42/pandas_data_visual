from Data import MotorAccidentData, SwimmingPoolData, BirdData
import pandas as pd


class PoolAnalysis(SwimmingPoolData):

    def __init__(self):
        SwimmingPoolData.__init__(self)

    def ten_most_popular_products(self, plot=False):
        products = self.data['Product']
        popular_products = products.value_counts().head(10)
        if plot:
            return popular_products.plot(kind='barh')
        else:
            return popular_products

    def sales_over_time(self, plot=False):
        def get_months(date):
            _, month, _ = date.split('.', 2)
            if len(month) == 1:
                month = '0'+month
            return month
        df = self.data.copy()
        df['Date'] = df['Date'].apply(get_months)
        sales_by_month = df['Date'].value_counts()
        sales_over_t = pd.DataFrame(
            {'Month': sales_by_month.index.values,
             "Sales": sales_by_month
             }).sort_index()
        if plot:
            sales_over_t.plot(kind='bar')
        else:
            return sales_over_t


class AccidentAnalysis(MotorAccidentData):

    def __init__(self):
        MotorAccidentData.__init__(self)
        self._format_data()

    def fatality_by_category(self, plot=False):
        fatalities = self.data.loc[self.data['Severity'] ==
                                   'fatality']['Category'].value_counts()
        if plot:
            return fatalities.plot(kind='pie')
        else:
            return fatalities

    def _accidents_over_time_by_category(self):
        category_by_year = self.data[['Category', 'Year']]
        multi_index_data = category_by_year.groupby(
            self.data[['Category', 'Year']].columns.tolist(), as_index=False)
        return multi_index_data.size().unstack(level=0)

    def _accidents_over_time_by_severity(self):
        severity_by_year = self.data[['Severity', 'Year']]
        multi_index_data = severity_by_year.groupby(
            self.data[['Severity', 'Year']].columns.tolist(), as_index=False).size()
        return multi_index_data.unstack(level=0)

    def accidents_over_time_by_severity_and_category(self, plot=False):
        severity = self._accidents_over_time_by_severity()
        category = self._accidents_over_time_by_category()
        severity_and_category = severity.merge(category, left_index=True,
                                              right_index=True)
        if plot:
            return severity_and_category.plot(kind='line')
        else:
            return severity_and_category


class BirdAnalysis(BirdData):

    def __init__(self):
        BirdData.__init__(self)
        self._format_data()
    
    def birds_with_less_than_10_certain_sightings(self, plot=False):
        series = self.data.loc[self.data['Nesting categories combined']
                        == 'Certain Nesting']['Species'].value_counts()
        less_than_10 = series.loc[series < 10]
        if plot:
            return less_than_10.plot('barh')
        else:
            return less_than_10


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # test_bird = BirdAnalysis()
    # test_bird.least_certainly_sighted()

    # test_pool = PoolAnalysis()
    # test_pool.ten_most_popular_products()
    # test_pool.sales_over_time().plot(kind='bar')

    # test_accident = AccidentAnalysis()
    # test_accident.fatality_by_category()
    # test_accident.accidents_over_time_by_category()
    # test_accident.accidents_over_time_by_severity().plot()
    # test_accident.accidents_over_time_by_severity_and_category().plot()
    
    plt.show()

