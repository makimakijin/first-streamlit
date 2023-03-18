
import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('澪ちゃんのハムスターは？')
expander1.write('くるくるクルミちゃんです！')
expander2 = st.expander('杏ちゃんが、いつも寝ているのを、起こすハムスターは？？？')
expander2.write('ゆきききだよーーん！')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
expander4 = st.expander('問い合わせ4')
expander4.write('問い合わせ4の回答')

# text = st.text_input("あなたの趣味を教えてください。")
# "あなたの好きな趣味：",text

# condition = st.slider('あなたの今の調子は？',0,10,5)
# "コンディション：",condition
# if st.checkbox('Show Image'):
#     img = Image.open('jin.jpeg')
#     st.image(img, caption="Jin Ymamamoto", use_column_width=True)


