import streamlit as st

def app():
    
    st.title("Dashboard")
    st.divider()

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    if st.session_state['signedout']:
        st.text('Work in Progress...')
        

    else:
        st.warning('Please :green[Login] to continue')
