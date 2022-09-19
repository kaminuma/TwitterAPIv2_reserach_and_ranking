# %%
import tweepy
import numpy as np
import matplotlib.pyplot as plt
from csv import writer
import pandas as pd
import schedule
import time

#scheduleで定時的にプログラム実行するために関数job():を作成
def job():
    #TwitterAPIv2の準備　それぞれの入力値はTwitter開発者アカウントで準備
    consumer_key = '**********************'
    consumer_secret = '**********************'
    access_token = '**********************'
    access_token_secret = '**********************'
    bearer_token= '**********************'
    
    id = 'tweet_id'
    
    client = tweepy.Client(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret,
        bearer_token=bearer_token )
        
    #最新のツイートを取得
    tweets = client.search_recent_tweets(query='#MHrise',max_results=100)
    

    #変数に検索ワード内の調べたいワードを設定
    # (csv入出力時に0列、0行は見出しになるためダミーを置いた)

    dami = str(tweets).count('リオレウス')
    naruga = str(tweets).count('ナルガクルガ')
    jinouga= str(tweets).count('ジンオウガ')
    tiga= str(tweets).count('ティガレックス')
    reia= str(tweets).count('リオレイア')
    tama= str(tweets).count('タマミツネ')
    baru = str(tweets).count('バルファルク')
    rajan = str(tweets).count('ラージャン')
    
    #ツイートが取得できているかを確かめる指標として検索条件を変数として置く
    monhan = str(tweets).count('モンハン')

    #それぞれの変数をリストに格納
    mons_list = [dami, naruga, jinouga, tiga, reia, tama, baru, rajan]
    
    #表示させるリストを別途定めた
    mons_list_hyoji = [naruga, jinouga, tiga, reia, tama, baru, rajan]


    print(mons_list_hyoji)

    #csvに'mons.csv'を置いているので読み込みと取得した最新の値を追記
    with open('mons.csv', 'a',newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(mons_list)
        f_object.close()

    #上記で上書きされた'mons.csv'の値を読み込み、変数dfに格納
    pd.read_csv('mons.csv')
    df = pd.read_csv('mons.csv')
    
    #変数dfのそれそれの列をプログラム起動から最新の分まで合計した値をdf_listへ格納し出力
    df_list = ([df.iloc[:,1].sum(),df.iloc[:,2].sum(),df.iloc[:,3].sum(),df.iloc[:,4].sum(),df.iloc[:,5].sum(),df.iloc[:,6].sum(),df.iloc[:,7].sum()])
    print(df_list)
    
    #上記合計を棒グラフで表示する
    left = np.array([1, 2, 3, 4, 5, 6, 7,])
    height = np.array(df_list)
    label = ['naruga', 'jinouga', 'tiga', 'reia', 'tama', 'baru', 'rajan']
    plt.bar(left, height, tick_label=label, align="center")
    #プロットした最新結果の棒グラフを"image.png"に上書きする
    plt.savefig('image.png')
    
schedule.every(1).minutes.do(job)
#1分ごとにjob関数を実行するschedule予定文

while True:
    schedule.run_pending()
    time.sleep(1)
    #1分毎に実行する予定文を無限ループさせ、プログラムを動かし続ける


