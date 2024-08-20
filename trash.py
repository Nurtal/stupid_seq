import pandas as pd
import numpy as np



def stupid_approach():
    """ """

    # load data
    df = pd.read_csv("data/data.csv")
    print(df)



def generate_deviation_plot():
    """ """
    
    # load data
    df = pd.read_csv("data/data.csv")
    df.set_index('ID')
    df = df.drop(columns=['ID'])

    # normalize
    # df=(df-df.min())/(df.max()-df.min())
    df=(df-df.mean())/df.std()
    df = df.replace(np.nan, 0)
    
    # replace by ecart à la moyenne
    df = df-df.mean()
    print(df)

    # reorder

    



if __name__ == "__main__":


    generate_deviation_plot()

    
