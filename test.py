import streamlit as st
import pandas as pd
import numpy as np
import os
import time

st.set_page_config(layout="centered")
st.title('Label Tool')
colA, colB, colC = st.columns(3)
image_list = []
optiopn_list = []
for index, item in enumerate(os.listdir('images')):
    image_list.append(item)
    optiopn_list.append(item +"     #" + str(index))
index= colA.number_input('Index',min_value=0,max_value=len(image_list),step=1)
st.session_state.option_1 = optiopn_list[index]
var3 = st.empty()
var1 = st.empty()
var2 = st.empty()
tmp_img = image_list[index]
var1.empty()
option = colB.selectbox(
    'Images List',
    tuple(optiopn_list),key='option_1')


#if var2:
#var1.image('images/' + option, width = 512)
#index = image_list.index(option)

    


data = pd.read_csv('out.csv')

form = st.form(key="annotation")
with form:
    cols = st.columns((4))
    cols[0].image('images/' + tmp_img, width = 512)

    var2 = st.empty()
    #cols = st.columns((4))
    race = cols[3].selectbox(
        'race',
        ('asian', 'EU/NA'))
    #cols = st.columns((4))
    skin_color = cols[3].selectbox(
        'skin color',
        ('black', 'white','yellow'))

    hair_length = cols[3].selectbox(
        'hair length',
        ('long', 'middle', 'short', 'None'))
    
    hair_color = cols[3].text_input('hair color')
    
    hair_curl = cols[3].selectbox(
        'hair curl',
        ('None', 'wave', 'curly', 'coily'))
    cols = st.columns((4))
    hair_bang = cols[0].selectbox(
        'hair bang',
        ('left', 'right', 'air', 'full'))

    hair_side = cols[2].slider('face side?', 0, 10, 1)

    hair_style = cols[1].text_input('hair style')
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
    check = st.form_submit_button(label="check!")
    submitted = st.form_submit_button(label="submit!")
    c_time = time.time()
    addrow = {'name':tmp_img,'race':race, 'hair_length':hair_length,  
            'background':backgrond, 'skin_color':hair_color, 'hair_style':hair_style,'hair_color':hair_color,
            'hair_side':hair_side,'hair_curl':hair_curl,'hair_bang':hair_bang,'hair_loss':hair_loss,'beard':beard,
        'face_hair_rank_asian':face_hair_rank_asian,'face_shape':face_shape,'time':c_time}
    tmp = pd.read_csv('out.csv')
    if check:
        st.write(addrow)

    if submitted:
        nameList = data['name'].tolist()
        if addrow['name'] in nameList:
            st.text('duplicate')
        else:
            data = data.append(addrow, ignore_index= True)
            #frame = data.append(addrow, ignore_index= True)
            data.to_csv('out.csv', index=False)
            data = pd.read_csv('out.csv')
        st.write(data)



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
df = pd.read_csv('out.csv')
if st.button('show csv'):   
    st.write(df)
#del_data= st.number_input('line number',min_value=0,max_value=200,step=1)
del_data = st.selectbox(
    'Images List',
    tuple(image_list))
if st.button('Delete That Line!'):
    df.drop(df[df['name'] == del_data].index,inplace=True)
    df.to_csv('out.csv', index=False)

