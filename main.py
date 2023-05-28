import requests
from tkinter import *
from tkinter import ttk
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def get_pokemon(pokemon_id):
    url = "https://pokeapi.co/api/v2/pokemon/"
    
    while True:
        judge = 0 <= int(pokemon_id) < 1009
        if not judge:
            print("存在しないよ,再入力してください")
        else:
            break
    
    url = url + pokemon_id #urlに図鑑idを追加
    response = requests.get(url) #urlリクエスト
    response = response.json() #json形式に整形
    
    #ラベルの更新
    label_id_sc['text'] = response['id'] #ID
    label_name_sc['text'] = response['name'] #なまえ
    label_types_sc['text'] = response['types'][0]['type']['name']#タイプ
    
    image = response['sprites']['front_default'] #jsonからの画像情報
    dst_path = 'pokemon.png'
    download_file(image, dst_path) #画像をダウンロードする
    global img
    canvas.delete('pokemon_image') #canvasをいったんクリア
    img = PhotoImage(file = 'pokemon.png') #ダウンロードした画像を読み込む
    canvas.create_image(50, 50, image=img, tags='pokemon_image')#canvas更新

root=Tk()
root.title("ポケモンゲットだぜ!")

label1 = ttk.Label(text="ポケモン番号を入れてね♡")
entry1 = ttk.Entry(width=5)
button1 = ttk.Button(text="ポケモンの表示", command=lambda:get_pokemon(entry1.get()))
label_id = ttk.Label(text="ポケモンID：")
label_id_sc = ttk.Label(text="")
label_name = ttk.Label(text="名前：")
label_name_sc = ttk.Label(text="")
label_types = ttk.Label(text="タイプ：")
label_types_sc = ttk.Label(text="")

label1.grid(row=0,column=1)
entry1.grid(row=1,column=1)
button1.grid(row=2,column=1)
label_id.grid(row=3,column=0)
label_id_sc.grid(row=3,column=1)
label_name.grid(row=4,column=0)
label_name_sc.grid(row=4,column=1)
label_types.grid(row=5,column=0)
label_types_sc.grid(row=5,column=1)

canvas = Canvas(root, width=100, height=100, bg="white", highlightthickness=0)
canvas.grid(row=6, column=1)
canvas.create_image(50, 50, tags='pokemon_image')

root.mainloop()
