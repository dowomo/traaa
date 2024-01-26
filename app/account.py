import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore  #database salvestamise jaoks



cred = credentials.Certificate('C:/Users/Sten/coding/app/dowomoapp-734e0283870c.json')
firebase_admin.initialize_app(cred)

#db = firestore.client()
#doc_ref = db.collection('userInfo').document()
#doc_ref.set()

def app():

    st.title("Account")

    #choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    
    
    def f():
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.success('Login Successful!')

            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            st.session_state.signedout = True
            st.session_state.signout = True 

        except:
            st.warning('Login Failed! Please try again')



    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


    #Kui on account sisse logitud
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False


    #Login/Sign Up sektsioon
    if not st.session_state['signedout']:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')


        if choice == 'Sign Up':
            username = st.text_input('Username')

            if st.button('Create my account'):
                user = auth.create_user(email = email, password = password, uid = username,)

                st.success('Account Created Successfully!')
                st.markdown('Please :green[Login] using your email')
                

        else:
            st.button('Login', on_click=f)

            

    #Sign Out nupp
                
    if st.session_state.signout:
        st.text('👤 Name: '+st.session_state.username)
        st.text('📧 Email: '+st.session_state.useremail)
        st.button('Sign out', on_click=t)
