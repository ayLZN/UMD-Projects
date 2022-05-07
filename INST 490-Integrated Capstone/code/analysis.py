import pandas as pd
pd.set_option('display.max_rows', 6000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
pd.set_option('display.max_colwidth', None)
import numpy as np

# The class takes in a dataframe and a state name, and returns a dataframe with the state's metrics compared to the
# national average
class Analysis:
    def __init__(self, df, state):
        self.df = df
        self.state = state

    def process(self):
        self.df = self.df[:-1]
        df2 = self.df.drop(columns=['StateCodes','State', 'Region','Division', 'Coast','Great Lakes'])
        col_names = list(df2)

        National_averages = {}
        for x in col_names:
            var = df2['{}'.format(x)].mean()
            National_averages.update({'{}'.format(x): var})

        Metrics = {}
        for ind, row in self.df.iterrows():
            if row['State'] == self.state:
                for k,v in National_averages.items():
                    Metrics.update({'{}'.format(k):{'{}'.format(self.state): round(row['{}'.format(k)],2),'National Average':round(v,2)}})
            else:
                pass

        df = pd.DataFrame(Metrics)
        df = df.T

        df['Difference'] = np.subtract(df['{}'.format(self.state)], df['National Average'])
        df['Analysis'] = np.where(df['{}'.format(self.state)] < df['National Average'], "{} is below than the National Average".format(self.state), "{} is greater than the National Average".format(self.state))
        
        return df

def main(state):
    ana = Analysis(pd.read_csv('data/Energy Census and Economic Data US 2010-2014.csv'), state)
    print(ana.process())

if __name__ == '__main__':
    state = 'Maryland'
    main(state)

