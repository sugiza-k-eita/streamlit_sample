import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image
import time
#↑画像を読み取るためのライブラリ


st.title("タイトル")

st.write("print")


#表の表示の仕方1
df = pd.DataFrame({
    "1列目": [1,2,3,4],
    "2列目": [10,20,30,40]
})

st.write(df)

#表の表示の仕方2
st.dataframe(df, width=100, height=100)
#縦と横の長さを引数として渡せる
#ハイライト付け方
st.dataframe(df.style.highlight_max(axis=0))

#表の表示の仕方3
st.table(df)
#静的な氷ができる


#マジックコマンド
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np 
import pandas as pd 
```
"""

#グラフの表示の仕方
#折れ線グラフ
st.line_chart(df)
#エリアチャート
#st.eria_chart(df)
#棒グラフ
st.bar_chart(df)


#mapを表示
df2 =pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df2)


#画像を表示
img = Image.open('画像.png')
#同じ階層に画像がある時
st.image(img, caption="Sugizaki Keita", use_columns_width=True)


#動的処理
#チェックボックス
#チェックボックスは返し値は、True or False
if st.checkbox("Show image"):
    img2 = Image.open('クラゲ.jpg')
    st.image(img2, caption="クラゲ", use_columns_width=True)

#セレクトボックス
option = st.selectbox(
    "あなたの好きな数字は",
    list(range(1,11))
)
"あなたの好きな数字は",option, "です"

#テキスト入力
option2 = st.text_input("あなたの趣味はなんですか")
"あなたの趣味は",option2

#スライダー
condition = st.slider("あなたの調子は？",0, 100, 50)
#0から100の間で、デフォルトが50
"コンディション", condition


#サイドバーにする方法
#st.sidebar.slider　みたいに　st.sidebar.XXX でやる

#2カラムにする方法
left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムを表示しますか？")
if button:
    right_column.write("右カラムが表示されました")

#エキスパンダーについて
expander1 =st.beta_expander("問い合わせ1")
expander1.write("問い合わせ１に関する回答")
expander2 =st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2に関する回答")
expander3 =st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3に関する回答")

#プログレスバーの表示
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text_input(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done"