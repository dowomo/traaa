import streamlit as st 
from streamlit_option_menu import option_menu

import about, account, dashboard, data

st.set_page_config(
    page_title="Dowomo App",
    page_icon="🗃️"
)

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['Account', 'Dashboard', 'Data', 'About'],
                icons=['person-circle', 'clipboard', 'file-earmark-bar-graph', 'patch-question'],
                menu_icon='three-dots',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"color":"white","font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "darkgrey"},
        "nav-link-selected": {"background-color": "#196590"},}
                
                )
            st.markdown(
        '''
        <div style="position: fixed; bottom: 0; width: 50%; text-align: left;">
            <p>📧homo@hot.ee ┃ ☎️54541010 </p>
        </div>


        ''',
        unsafe_allow_html=True
    )
        if app == 'Account':
            account.app()
        if app == 'Dashboard':
            dashboard.app()
        if app == 'Data':
            data.app()
        if app == 'About':
            about.app()

    run()