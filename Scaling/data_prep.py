import pandas as pd

def main():
    dpath = 'samples/ratings_Amazon_Instant_Video.csv'
    columns=['user','item','rating','timestamp']
    df = pd.read_csv(dpath, header=None,names=columns)
    print(df.head())

if __name__ == '__main__':
    main()
