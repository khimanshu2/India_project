import pandas as pd
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv(r'C:\Users\khima\Downloads\india1.csv')


state= list(df['State'].unique())
state.insert(0,'Overall India')

st.sidebar.title('India Ka Data Viz')

selected_state = st.sidebar.selectbox('Select a state',state)

primary = st.sidebar.selectbox('select Primary parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('select Secondary parameter',sorted(df.columns[5:]))
plot =st.sidebar.button('plot Graph')

if plot:
    st.text('size represent primary parameter')
    st.text('color represent secondary')
    if selected_state=='Overall India':
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=10,
                                mapbox_style='carto-positron',width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=10,
                                mapbox_style='carto-positron', width=1200, height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)