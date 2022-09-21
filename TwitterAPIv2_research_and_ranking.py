import tweepy
import Twitter_key
import numpy as np
import matplotlib.pyplot as plt
from csv import writer
import pandas as pd
import schedule
import time

#scheduleで定時的にプログラム実行するために関数job():を作成
def job():
    
    #Twitter_keyの関数を変数に格納
    client = Twitter_key.twitter_key()

    #最新のツイートを取得
    tweets = client.search_recent_tweets(query='#MHrise',max_results=100)


    #変数に検索ワード内の調べたいワードを設定
    # (csv入出力時に0列、0行は見出しになるため変数dami(ダミー)を置いた)

    dami = str(tweets).count('リオレウス')
    word1 = str(tweets).count('ナルガクルガ')
    word2= str(tweets).count('ジンオウガ')
    word3= str(tweets).count('ティガレックス')
    word4= str(tweets).count('リオレイア')
    word5= str(tweets).count('タマミツネ')
    word6 = str(tweets).count('バルファルク')
    word7 = str(tweets).count('ラージャン')
    
    #ツイートが取得できているかを確かめる指標として検索条件を変数として置く
    word0 = str(tweets).count('モンハン')

    #それぞれの変数をリストに格納
    get_list = [dami, word1, word2, word3, word4, word5, word6, word7]
    
    #表示させるリストを別途定めた
<<<<<<< Updated upstream
    mons_list_hyoji = [naruga, jinouga, tiga, reia, tama, baru, rajan]
    
    #一回の取得での各ワードの出現率をプリント
    print(mons_list_hyoji)

    #カレントディレクトリに'mons.csv'を置いているので読み込みと取得した最新の値を追記
    with open('mons.csv', 'a',newline='') as f_object:
=======
    get_list_hyoji = [word1, word2, word3, word4, word5, word6, word7]

    print(get_list_hyoji)

    #csvに'mons.csv'を置いているので読み込みと取得した最新の値を追記
    with open('get_list.csv', 'a',newline='') as f_object:
>>>>>>> Stashed changes
        writer_object = writer(f_object)
        writer_object.writerow(get_list)
        f_object.close()

    #上記で上書きされた'mons.csv'の値を読み込み、変数dfに格納
    pd.read_csv('get_list.csv')
    df = pd.read_csv('get_list.csv')
    
    #変数dfのそれそれの列を「プログラム起動から最新の分まで」合計した値をdf_listへ格納し出力
    df_list = ([df.iloc[:,1].sum(),df.iloc[:,2].sum(),df.iloc[:,3].sum(),df.iloc[:,4].sum(),df.iloc[:,5].sum(),df.iloc[:,6].sum(),df.iloc[:,7].sum()])
    print(df_list)
    
    #上記合計を棒グラフで表示する
    left = np.array([1, 2, 3, 4, 5, 6, 7,])
    height = np.array(df_list)
    label = ['naruga', 'jinouga', 'tiga', 'reia', 'tama', 'baru', 'rajan']
    plt.bar(left, height, tick_label=label, align="center")
    
    #プロットした最新結果の棒グラフを"image.png"に上書きする
    plt.savefig('image.png')

#1分ごとにjob関数を実行するschedule予定文
schedule.every(1).minutes.do(job)

#1分毎に実行する予定文を無限ループさせ、プログラムを動かし続ける
while True:
    schedule.run_pending()
