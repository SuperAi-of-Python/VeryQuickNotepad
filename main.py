try:
    print("メモ帳です。再起動したら消えちゃうよ。")
    print("read [num]で読み出し、del [num]で削除、readallで全部読み出し。それ以外で書き込み。忘れたらhelpでどうぞ")
    memos=list()
    while True:
        text=input()
        if text=="readall":
            for i,n in enumerate(memos):
                print(i,n)

        elif text=="end":
            print("3秒後に終了するよ。")
            __import__("time").sleep(3)
            exit()

        elif text=="help":
            print("read [num]で読み出し、del [num]で削除、readallで全部読み出し。それ以外で書き込み")

        elif "read" in text:
            try:
                print(memos[int(text.split()[1])])
            except (ValueError,IndexError):
                print("その番号にメモは保存されてないよ。readallで確認してね")

        elif "del" in text:
            try:
                memos[int(text.split()[1])]
            except (ValueError,IndexError):
                print("その番号にメモは保存されてないよ。readallで確認してね")
            else:
                del memos[int(text.split()[1])]
                print("削除したよ。")

        else:
            memos.append(str(text))
            print(f"Num{len(memos)-1}として保存したよ。")

except KeyboardInterrupt:
    print("3秒後に終了するよ。")
    __import__("time").sleep(3)
    exit()