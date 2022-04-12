import streamlit as st
import pandas as pd
import numpy as np
import os
import time


st.set_page_config(layout='wide')
st.title('Label Tool')
labeler_name = st.selectbox(
    'your name',
     ('steve', 'qiqi','charlie','eric','pengfei')
)
#labeler_name = st.text_input("your id")
ln = st.session_state.name = labeler_name
st.write(ln)
colA, colB, colC = st.columns(3)
image_list = []
optiopn_list = []
if ln == 'steve':
    folder = 'images_steve'
    file = 'out_steve.csv'
elif ln == 'qiqi':
    folder = 'images_qiqi'
    file = 'out_qiqi.csv'
elif ln == 'eric':
    folder = 'images_eric'
    file = 'out_eric.csv'
elif ln == 'charlie':
    folder = 'images_charlie'
    file = 'out_charlie.csv'
elif ln == 'pengfei':
    folder = 'images_pengfei'
    file = 'out_pengfei.csv'
for index, item in enumerate(os.listdir(folder)):
    image_list.append(item)
    optiopn_list.append(item +"     #" + str(index))
index= colA.number_input('Index',min_value=0,max_value=len(image_list)-1,step=1)
st.session_state.option_1 = optiopn_list[index]
var3 = st.empty()
var1 = st.empty()
var2 = st.empty()
tmp_img = image_list[index]
var1.empty()
option = colB.selectbox(
    'Images List',
    tuple(optiopn_list),key='option_1')
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 666px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#if var2:
#var1.image('images/' + option, width = 512)
#index = image_list.index(option)
with st.sidebar:
    st.title("标记步骤")
    st.text("1.在 ‘your name’ 中选择好自己的名字")
    st.text("2.根据出现的图片进行标记，可以自行选择标记顺序")
    st.text("3.所有左右均相对于图片")
    st.text("4.每一张图片可标记一次，如果重复标记会提示duplicate")
    st.text("5.如果需要修改，请在下方输入框中输入或选择目标图片，然后通过Delete that line按钮删除目标图片。")
    st.text("6.show csv按钮可显示目前所有的label结果")
    st.text("7.耐心标记，不要着急！")
    st.title("标记帮助")
    helps = st.selectbox('HELP!',
        ('male', 'afro', 'bob','bowl','buzz','caesar',
        'crew','undercut','pixie','ponytail','bun',
        'straight','wavy','face','curly_type'))
    st.image('helps/' + helps + '.png')

data = pd.read_csv(file)
dup = 0
form = st.form(key="annotation")
with form:
    cols = st.columns((4))
    cols[1].image(folder+'/' + tmp_img, width = 512)

    var2 = st.empty()
    cols = st.columns((4))
    race = cols[0].selectbox(
        'race',
        ('asian', 'EU/NA'))
    #cols = st.columns((4))
    skin_color = cols[1].selectbox(
        'skin color',
        ('black', 'white','yellow', 'brown'))

    hair_length = cols[2].selectbox(
        'hair length',
        ('long', 'middle', 'short', 'None'))
    
    hair_color = cols[3].selectbox(
        'hair color',
        ('black', 'white','blonde','grey','mixed'))

    cols = st.columns((4))
    hair_curl = cols[0].selectbox(
        'hair curl',
        ('None', 'wave', 'curly', 'coily'))
    #cols = st.columns((4))
    hair_bang = cols[1].selectbox(
        'hair bang',
        ('None','left', 'right', 'air', 'full'))

    hair_side = cols[2].slider('hair side?', 0, 10, 1)

    hair_style = cols[3].selectbox('hair style',
        ('afro', 'bob','bowl','buzz','caesar','crew','undercut','pixie','ponytail','bun','straight','wavy','hat','severe_hair_loss'))
    cols = st.columns((4))
    hair_loss = cols[0].selectbox(
        'hair loss',
        ('None', 'can tell', 'all'))

    backgrond = cols[1].selectbox(
        'backgrond',
        ('Good', 'Bad'))
    
    beard = cols[3].checkbox('Have beard?')
    face_shape = cols[2].selectbox(
        'face shape',
        ('oval', 'diamond', 'rectangle', 'round', 'square'))
    cols = st.columns((1))
    face_hair_rank_asian = st.slider('face hair rank?', 0, 10, 1)
    cols = st.columns((4))
    check = cols[0].form_submit_button(label="check!")
    submitted = cols[1].form_submit_button(label="submit!")
    
    c_time = time.time()
    addrow = {'name':tmp_img,'race':race, 'hair_length':hair_length,  
            'background':backgrond, 'skin_color':hair_color, 'hair_style':hair_style,'hair_color':hair_color,
            'hair_side':hair_side,'hair_curl':hair_curl,'hair_bang':hair_bang,'hair_loss':hair_loss,'beard':beard,
        'face_hair_rank_asian':face_hair_rank_asian,'face_shape':face_shape,'time':c_time,'labeler':labeler_name}
    tmp = pd.read_csv(file)
    if check:
        st.write(addrow)

    if submitted:
        nameList = data['name'].tolist()
        if addrow['name'] in nameList:
            
            st.text('duplicate!')
            st.text('The label will not write in, if you want to modify your label, you have to delete it from the button below and relabel it.')                  
            
        else:
            data = data.append(addrow, ignore_index= True)
            #frame = data.append(addrow, ignore_index= True)
            data.to_csv(file, index=False)
            data = pd.read_csv(file)
            dup = 0
        st.write(data)
 


    # if var4.button('Still Submit!'):
    #     st.text('updating...')
    #     st.text('updating...')
    #     st.text('updating...')
    #     data.drop(data[data['name'] == addrow['name']].index,inplace=True)
    #     #data = data.append(addrow, ignore_index= True)
    #     data.to_csv(file, index=False)
    #     data = pd.read_csv(file)
    #     st.write(data)
    # else:
    #     st.text('updating...')



    # if st.button('Submit!'):
    #     nameList = data['name'].tolist()
    #     if addrow['name'] in nameList:
    #         st.text('duplicate')
    #     else:
    #         data = data.append(addrow, ignore_index= True)
    #         #frame = data.append(addrow, ignore_index= True)
    #         data.to_csv('out.csv', index=False)
    #         tmp = pd.read_csv('out.csv')
    #     st.write(tmp)
cols = st.columns((3))
df = pd.read_csv(file)
cols[0].text('This button will show current csv')
if cols[0].button('show csv'):   
    st.write(df)
#del_data= st.number_input('line number',min_value=0,max_value=200,step=1)
del_data = cols[1].selectbox(
    'Images List',
    tuple(image_list))
if cols[1].button('Delete That Line!'):
    df.drop(df[df['name'] == del_data].index,inplace=True)
    df.to_csv(file, index=False)

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')
dl = convert_df(df)
cols[2].text('This button will download your labels')
cols[2].download_button(label=' Download Current Result',
                                data=dl ,
                                file_name= 'label.csv')
