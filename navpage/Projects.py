import streamlit as st # type: ignore
import pandas as pd

st.subheader("Projects")

data = {
    'Title': ['Estimation of L-curve in a Seismic Tomography Inverse Problem', 'Elastic Wave Modelling', 'Estimation of Model Resolution in Ambient Seismic Noise Source Inversion', 'Waveform modeling and ML-based tomography of volcanic edifices'],
    'Year': ['2022', '2023', '2023', '2024-25'],
    'Institute': ['IISER Pune', 'IIT Bombay', 'IISER Pune', 'Goethe University Frankfurt']
}

df = pd.DataFrame(data)

# Display table using st.table
st.dataframe(df, hide_index=True, use_container_width=True)