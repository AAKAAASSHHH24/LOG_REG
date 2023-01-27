
import streamlit as st
from utils import PrepProcesor, columns 

import numpy as np
import pandas as pd
import pickle

#st.set_option('server.host', '0.0.0.0')
#st.set_option('server.port', 8080)
st.header('WILL MY WIFE :red[CHEAT] ON ME? :woman: :high_heel:')
#st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')
#st.set_page_config(page_title='WILL MY WIFE CHEAT ON ME?', page_icon=':woman:', layout="centered", initial_sidebar_state="auto", menu_items=None)
model = pickle.load(open('log_model.pkl','rb'))
st.title('Created by: Akash Rakshit')

# ['rate_marriage', 'yrs_married', 'children', 'religious', 'educ', 'occupation', 'occupation_husb']


rate_marriage = st.selectbox(
    'Rate your marriage on scale of 1 to 5',
    ('1', '2', '3','4','5'))

st.write('You selected!!:', rate_marriage)

#rate_marriage = st.number_input("Rate your marriage on scale of 1 to 5", 1,5)
yrs_married = st.number_input("Choose no: of years married",0,100)
children = st.number_input("No: of children",0,30)
religious = int(st.selectbox('How religious is your wife on scale of 1 to 4?', ('1', '2', '3','4')))

educ = int(st.selectbox("How much educated is your wife?\n 9 = grade school',\n '12 = high school',\n '14 = some college',\'16 = college graduate',\n '17 = some graduate school',\n '20= advanced degree'", 
                                                                      (9, 12, 14,16, 17, 20)))
                                                                      

occupation = st.selectbox("Occupation of your wife:\n 1 = student\n 2 = farming/semi-skilled/unskilled\n 3 = white collar\n 4 = teacher/nurse/writer/technician/skilled\n 5 = managerial/business\n 6 = professional with advanced degree", 
                          ('1', '2', '3','4','5','6'))
# occ_2	occ_3	occ_4	occ_5	occ_6	occ_husb_2	occ_husb_3	occ_husb_4	occ_husb_5	occ_husb_6

if occupation =='1':
    occ_2= occ_3 =  occ_4 =occ_5 =occ_6 =0
elif occupation == '2':
    occ_2= 1 
    occ_3 =  occ_4 =occ_5 =occ_6 =0
elif occupation == '3':
    occ_3= 1 
    occ_2 =  occ_4 = occ_5 =occ_6 =0
elif occupation == '4':
    occ_4= 1 
    occ_2 =  occ_3 = occ_5 =occ_6 =0
elif occupation == '5':
    occ_5= 1 
    occ_2 =  occ_4 = occ_3 = occ_6 =0
elif occupation == '6':
    occ_6= 1 
    occ_2 =  occ_4 = occ_5 =occ_3 =0
    
occupation_husb = st.selectbox("Your Occupation:\n 1 = student\n 2 = farming/semi-skilled/unskilled\n 3 = white collar\n 4 = teacher/nurse/writer/technician/skilled\n 5 = managerial/business\n 6 = professional with advanced degree", 
                          ('1', '2', '3','4','5','6'))

if occupation_husb =='1':
    occ_husb_2= occ_husb_3 =  occ_husb_4 =occ_husb_5 =occ_husb_6 =0
elif occupation_husb == '2':
    occ_husb_2= 1 
    occ_husb_3 =  occ_husb_4 =occ_husb_5 =occ_husb_6 =0
elif occupation_husb == '3':
    occ_husb_3= 1 
    occ_husb_2 =  occ_husb_4 = occ_husb_5 =occ_husb_6 =0
elif occupation_husb == '4':
    occ_husb_4= 1 
    occ_husb_2 =  occ_husb_3 = occ_husb_5 =occ_husb_6 =0
elif occupation_husb == '5':
    occ_husb_5= 1 
    occ_husb_2 =  occ_husb_4 = occ_husb_3 = occ_husb_6 =0
elif occupation_husb == '6':
    occ_husb_6= 1 
    occ_husb_2 =  occ_husb_4 = occhusb__5 =occ_husb_3 =0


def predict(): 
    row = np.array([occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage,yrs_married,children,religious,educ]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    
    st.write('Prediction', prediction[0])
    if prediction[0] == 1: 
        st.success('BAD NEWS! BE CAREFUL:heavy_exclamation_mark: :eggplant: :thumbsdown:')
    else: 
        st.error('GOOD NEWS SHE IS LOYAL :thumbsup: :chocolate_bar: :champagne:') 

trigger = st.button('Predict', on_click=predict)