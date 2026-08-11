import requests
import time
import random
from datetime import datetime, timezone, timedelta

# ---------- 設定 ----------
TARGET_EMAIL = "taisei.y1001@gmail.com"  # ★ここを友達のアドレスに書き換えてね！
SEND_COUNT_PER_TIME = 1                # 各時間帯に何通送るか（例:朝に3通）
# -------------------------

# 日本時間（JST）を取得
JST = timezone(timedelta(hours=9))
now = datetime.now(JST)
hour = now.hour

# 時間帯に応じて件名と本文を変更（ここを編集してドッキリメッセージをカスタマイズ！）
if 5 <= hour < 12:  # 朝 (5:00〜11:59)
    SUBJECT = "🌅 今日も素晴らしい朝ですね"
BASE_BODY = """おはようございます。

今日は実に気持ちの良い晴天ですね。窓を開けると、風が頬を優しく撫で、小鳥たちのさえずりが耳に心地よい。なんと平和な朝でしょう。

この一時の静けさを、どうかあなたも噛みしめてください。今日一日が、穏やかな光に包まれますように。

心より安らぎを感じる、そんな朝です。"""
elif 12 <= hour < 18:  # 昼 (12:00〜17:59)
    SUBJECT = "🌞 お腹空いた？"
BASE_BODY = """ねえねえねえねえ！
お昼！お昼だよ！！何食べるの？カレー？ラーメン？パン？？
あ、でもさ、ラーメンって麺の固さあるじゃん。バリカタ？ふつう？ヤワ？
ていうかさ、今何してる？暇そうじゃん。返事してよ～。
あ、別に急いでないけど。でも早く返して。
…って言いながらもう3行も書いちゃった。なんか負けた気分。
あー、つまんない。何か面白いことない？ないよね。だって君だもん。"""
else:  # 夜 (18:00〜4:59)
    SUBJECT = "🌙 眠れない夜だね..."
BASE_BODY = """もう夜も遅いし、布団の中はどうですか？

ちょっと聞いてくださいよ。
今日の疲れが溜まってるのか、なんかもう…おっ！ぱい！ぱいーん！って感じじゃないですか？（急に）

せっかくの夜だし、せつくすしない？って言いたくなる気持ち、わかりますよね？
いや、マジで。せっくす。セ・ッ・ク・ス。
…って、まさか本気にしてないですよね？冗談ですよ（半分）。
でももし君が「いいよ」って言ったら…あ、やっぱやめとく。恥ずかしい。
今夜はこのへんでオナニー…もとい、オヤスミなさい。
続きはこれを、、 https://www.youtube.com/watch?v=dQw4w9WgXcQ """


def create_address():
    """ランダムな捨てメアドを生成（無限パターン）"""
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    domains = ['1secmail.com', '1secmail.org', '1secmail.net']
    domain = random.choice(domains)
    return f"{name}@{domain}"


def send_horror_mail(sender, recipient, subject, body):
    """1secmail APIを使ってメールを送信"""
    api_url = "https://www.1secmail.com/api/v1/"
    params = {
        "action": "sendMessage",
        "from": sender,
        "to": recipient,
        "subject": subject,
        "body": body
    }
    try:
        response = requests.post(api_url, data=params, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"エラー: {e}")
        return False


# ---------- 実行 ----------
print(f"🕒 現在時刻: {now.strftime('%H:%M')}  ({SUBJECT})")

for i in range(SEND_COUNT_PER_TIME):
    fake_addr = create_address()
    # 同じ時間帯でも少しバリエーションを持たせる
    body = f"{BASE_BODY} （{i+1}/{SEND_COUNT_PER_TIME}）"
    
    success = send_horror_mail(fake_addr, TARGET_EMAIL, SUBJECT, body)
    if success:
        print(f"✅ {fake_addr} から送信成功！")
    else:
        print(f"❌ {fake_addr} から送信失敗...")
    
    time.sleep(5)  # 間隔を空けてスパム扱いを回避

print("🎯 この時間帯のドッキリ完了！")
