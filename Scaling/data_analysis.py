import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def main():
    growthRates()

def growthRates():
    datapaths = ['samples/ratings_Books.csv',
                'samples/ratings_Movies_and_TV.csv',
                'samples/ratings_Amazon_Instant_Video.csv']

    columns=['user','item','rating','timestamp']

    fig, ax = plt.subplots()
    for dpath in datapaths:
        print("importing %s" %dpath)
        df = pd.read_csv(dpath, header=None,names=columns)
        plotGrowth(df,ax)
    ax.legend([cleanLabel(s) for s in datapaths])
    fig = ax.get_figure()
    fig.savefig('scale.png')

def cleanLabel(s):
    return(s.replace('samples/ratings_','').replace('.csv','').replace('_',' '))

def plotGrowth(df,ax):
    dates = df['timestamp'].astype('datetime64[s]')
    dates = dates.apply(lambda x:dt.datetime(x.year, x.month, 1)).value_counts()
    dates.plot(ax=ax)




if __name__ == '__main__':
    main()

    """
    # Load data
    df = pd.read_csv('ratings_Amazon_Instant_Video.csv', header=None,
    names=['user','item','rating','timestamp'])

    # Count number of reviews per user (show longtail)

    num_reviews = df.groupby(['user']).size()
    num_reviews[num_reviews.values > 10] = 11
    print(num_reviews.value_counts())


    # Reviews by time

    dates = df['timestamp'].astype('datetime64[s]').apply(lambda x: x.strftime('%Y-%m')).value_counts()
    ax = dates.plot()
    fig = ax.get_figure()
    fig.savefig('scale.png')

    #print(dates)
    dd = df['timestamp'].astype('datetime64[s]')
    print(dd)
    ax = dd.groupby([dd.values.year, dd.values.month]).count().plot(kind="bar")
    fig = ax.get_figure()
    fig.savefig('scale.png')
    """
