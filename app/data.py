import streamlit as st

def app():
    
    st.title("Data")
    st.divider()

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    if st.session_state['signedout']:
        st.text('Work in Progress...')

        elements = st.empty()
        elements.bar_chart(range(11))

    else:
        st.warning('Please :green[Login] to continue')