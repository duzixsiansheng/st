import streamlit as st
import pandas as pd
import numpy as np
import os
import time

def run():
    

    accounts = {'steve':'yangzk960324',
                '王争争':'wangzhengzheng',
                '孙文丽':'sunwenli',
                '房潇潇':'fangxiaoxiao',
                'test':'test'}
    #username = var_user.text_input('用户名')
    
    st.title('Label Tool')
    labeler_name = st.selectbox(
        'your name',
        ('steve', '王争争','孙文丽','房潇潇','test')
    )
    passcode = st.text_input('密码', type="password")
    #labeler_name = st.text_input("your id")
    ln = st.session_state.name = labeler_name
    #st.write(ln)
    colA, colB, colC = st.columns(3)
    image_list = []
    optiopn_list = []
    unlabeled_list = []
    labeled_list = []
    if ln == 'steve':
        folder = 'images_steve'
        file = 'out_steve.csv'
    elif ln == '王争争':
        folder = 'images_qiqi'
        file = 'out_qiqi.csv'
    elif ln == '孙文丽':
        folder = 'images_eric'
        file = 'out_eric.csv'
    elif ln == '房潇潇':
        folder = 'images_charlie'
        file = 'out_charlie.csv'
    elif ln == 'test':
        folder = 'images_pengfei'
        file = 'out_pengfei.csv'
    if accounts.get(labeler_name) == passcode:
        list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(folder, x)),
                            os.listdir(folder) ) )
        for index, item in enumerate(list_of_files):
            image_list.append(item)
            optiopn_list.append(item +"     #" + str(index))
        index= colA.number_input('Index',min_value=0,max_value=len(image_list)-1,step=1)
        st.session_state.option_1 = optiopn_list[index]
        cur = st.session_state.option_2 = image_list[index]
        start_time = time.time()
        var3 = st.empty()
        var1 = st.empty()
        var2 = st.empty()
        tmp_img = image_list[index]
        var1.empty()
        colB.write('')
        colB.write('')
        colB.write(optiopn_list[index])
        #option = colB.selectbox(
        #    'Images List',
        #    tuple(optiopn_list),key='option_1')
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 500px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 400px;
                margin-left: -400px;
            
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
            st.text("3.所有左右均相对于人物")
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
        for item in image_list:
            if item in data['name'].tolist():
                labeled_list.append(item)
            else:
                unlabeled_list.append(item)
        st.write("您已经标记", len(labeled_list), 'out of', len(image_list), '张图片了!')
        if cur in labeled_list:
            new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">您已经标记过这张图片了</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            dup = 1
        else:    
            dup = 0
        #if dup == 1:
        race_list = ['asian', 'EU/NA']
        skin_color_list = ['black', 'white','yellow', 'brown']
        hair_length_list = ['long', 'middle', 'short', 'None']
        hair_color_list = ['black', 'white','blonde','grey','mixed','purple','green','blue','red']
        hair_curl_list = ['None', 'wave', 'curly', 'coily']
        hair_bang_list = ['None','left', 'right', 'air', 'full']
        #hair_side_list = []
        hair_style_list = ['afro', 'bob','bowl','buzz','caesar','crew','undercut','pixie','ponytail','bun','straight','wavy','hat','severe_hair_loss']
        hair_loss_list = ['None', 'can tell', 'all']
        background_list = ['Good', 'Bad']
        #beard_list = []
        face_shape_list = ['oval', 'diamond', 'rectangle', 'round', 'square']
        #face_hair_rank_asian_list = []
        ###########################################
        
        form = st.form(key="annotation")
        with form:
            cols = st.columns((4))
            cols[0].write('还未标记的图片')
            cols[0].write(pd.DataFrame(unlabeled_list))
            cols[1].image(folder+'/' + tmp_img, width = 512)
            cols[3].write('已经标记的图片')
            cols[3].write(pd.DataFrame(labeled_list))
            var2 = st.empty()
            cols = st.columns((4))
            #cols = st.columns((4))
            if dup == 1:
                race = cols[0].selectbox(
                        '人种 race',
                        ('asian', 'EU/NA'),
                        index = race_list.index((data.loc[data["name"] == cur, "race"]).tolist()[0]))
                skin_color = cols[1].selectbox(
                    '肤色 skin color',
                    ('black', 'white','yellow', 'brown'),
                    index = skin_color_list.index((data.loc[data["name"] == cur, "skin_color"]).tolist()[0]))
                hair_length = cols[2].selectbox(
                    '头发长度 hair length',
                    ('long', 'middle', 'short', 'None'),
                    index = hair_length_list.index((data.loc[data["name"] == cur, "hair_length"]).tolist()[0]))
                hair_color = cols[3].selectbox(
                    '头发颜色 hair color',
                    ('black', 'white','blonde','grey','mixed','purple','green','blue','red'),
                    index = hair_color_list.index((data.loc[data["name"] == cur, "hair_color"]).tolist()[0]))

            elif dup == 0:
                race = cols[0].selectbox(
                        '人种 race',
                        ('asian', 'EU/NA'))
                skin_color = cols[1].selectbox(
                    '肤色 skin color',
                    ('black', 'white','yellow', 'brown'))
                hair_length = cols[2].selectbox(
                    '头发长度 hair length',
                    ('long', 'middle', 'short', 'None'),index = 1)
                hair_color = cols[3].selectbox(
                    '头发颜色 hair color',
                    ('black', 'white','blonde','grey','mixed','purple','green','blue','red'))

            cols = st.columns((4))
            if dup == 1:
                hair_curl = cols[0].selectbox(
                    '头发卷曲程度 hair curl',
                    ('None', 'wave', 'curly', 'coily'),
                        index = hair_curl_list.index((data.loc[data["name"] == cur, "hair_curl"]).tolist()[0]))
                
                hair_bang = cols[1].selectbox(
                    '刘海状况 hair bang',
                    ('None','left', 'right', 'air', 'full'),
                        index = hair_bang_list.index((data.loc[data["name"] == cur, "hair_bang"]).tolist()[0]))

                hair_side = cols[2].slider('发分线 hair side?', 0, 10, (data.loc[data["name"] == cur, "hair_side"]).tolist()[0])

                hair_style = cols[3].selectbox('发型 hair style',
                    ('afro', 'bob','bowl','buzz','caesar','crew','undercut','pixie','ponytail','bun','straight','wavy','hat','severe_hair_loss'),
                        index = hair_style_list.index((data.loc[data["name"] == cur, "hair_style"]).tolist()[0]))    
            
            elif dup == 0:
                hair_curl = cols[0].selectbox(
                    '头发卷曲程度 hair curl',
                    ('None', 'wave', 'curly', 'coily'))
                
                hair_bang = cols[1].selectbox(
                    '刘海状况 hair bang',
                    ('None','left', 'right', 'air', 'full'))

                hair_side = cols[2].slider('发分线 hair side?', 0, 10, 5)

                hair_style = cols[3].selectbox('发型 hair style',
                    ('afro', 'bob','bowl','buzz','caesar','crew','undercut','pixie','ponytail','bun','straight','wavy','hat','severe_hair_loss','pose too bad'))

            cols = st.columns((4))

            if dup == 1:
                hair_loss = cols[0].selectbox(
                    '秃头程度 hair loss',
                    ('None', 'can tell', 'all'),
                        index = hair_loss_list.index((data.loc[data["name"] == cur, "hair_loss"]).tolist()[0]))    

                background = cols[1].selectbox(
                    '背景情况 backgrond',
                    ('Good', 'Bad'),
                        index = background_list.index((data.loc[data["name"] == cur, "background"]).tolist()[0]))    
                
                beard = cols[3].checkbox('Have beard?', value = (data.loc[data["name"] == cur, "beard"]).tolist()[0])

                face_shape = cols[2].selectbox(
                    '脸型 face shape',
                    ('oval', 'diamond', 'rectangle', 'round', 'square'),
                        index = face_shape_list.index((data.loc[data["name"] == cur, "face_shape"]).tolist()[0]))           
            elif dup == 0:    
                hair_loss = cols[0].selectbox(
                    '秃头程度 hair loss',
                    ('None', 'can tell', 'all'))

                background = cols[1].selectbox(
                    '背景情况 background',
                    ('Good', 'Bad'))
                
                beard = cols[3].checkbox('Have beard?')

                face_shape = cols[2].selectbox(
                    '脸型 face shape',
                    ('oval', 'diamond', 'rectangle', 'round', 'square'))


            cols = st.columns((1))
            if dup == 1:
                face_hair_rank_asian = st.slider('脸和头发的匹配程度，根据个人审美评分 face hair rank?', 0, 10, (data.loc[data["name"] == cur, "face_hair_rank_asian"]).tolist()[0])
            elif dup == 0:    
                face_hair_rank_asian = st.slider('脸和头发的匹配程度，根据个人审美评分 face hair rank?', 0, 10, 5)
            cols = st.columns((4))
            check = cols[0].form_submit_button(label="检查 check!")
            submitted = cols[1].form_submit_button(label="提交 submit!")
            
            
            addrow = {'name':tmp_img,'race':race, 'hair_length':hair_length,  
                    'background':background, 'skin_color':skin_color, 'hair_style':hair_style,'hair_color':hair_color,
                    'hair_side':hair_side,'hair_curl':hair_curl,'hair_bang':hair_bang,'hair_loss':hair_loss,'beard':beard,
                'face_hair_rank_asian':face_hair_rank_asian,'face_shape':face_shape,'time':'0','labeler':labeler_name}
            tmp = pd.read_csv(file)
            if check:
                st.write(addrow)

            if submitted:
                end_time = time.time()
                nameList = data['name'].tolist()
                addrow = {'name':tmp_img,'race':race, 'hair_length':hair_length,  
                    'background':background, 'skin_color':skin_color, 'hair_style':hair_style,'hair_color':hair_color,
                    'hair_side':hair_side,'hair_curl':hair_curl,'hair_bang':hair_bang,'hair_loss':hair_loss,'beard':beard,
                'face_hair_rank_asian':face_hair_rank_asian,'face_shape':face_shape,'time':time.localtime( time.time() ),'labeler':labeler_name}
                if addrow['name'] in nameList:
                    
                    st.text('重复!')
                    st.text('这次标记不会被记录，如果您想要修改请先用下方的删除按钮删除该标记之后再进行标记！The label will not write in, if you want to modify your label, you have to delete it from the button below and relabel it.')                  
                    
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
        cols[0].text('显示目前全部已标记内容 This button will show current csv')
        if cols[0].button('show csv'):   
            st.write(df)
        #del_data= st.number_input('line number',min_value=0,max_value=200,step=1)
        del_data = cols[1].selectbox(
            '选择图片，按下按钮后删除该图片的标记',
            tuple(image_list))
        if cols[1].button('Delete That Line!'):
            df.drop(df[df['name'] == del_data].index,inplace=True)
            df.to_csv(file, index=False)

        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        dl = convert_df(df)
        cols[2].text('下载当前已标记内容 This button will download your labels')
        cols[2].download_button(label=' Download Current Result',
                                        data=dl ,
                                        file_name= 'label.csv')


if __name__ == "__main__":
    st.set_page_config(layout='wide')
    run()
    # var_user = st.empty()
    # var_pc = st.empty()
    # accounts = {'steve':'stevey960324'}
    # username = var_user.text_input('用户名')
    # passcode = var_pc.text_input('密码')
    # if st.button('登录'): 
    #     if username in accounts:
    #         if accounts.get(username) == passcode:
                
    #             run(var_pc)
    #         else:
    #             st.write("用户名密码错误！")
    #     else:
    #         st.write('没有该账户！')