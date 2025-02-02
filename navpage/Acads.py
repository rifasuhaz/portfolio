import streamlit as st # type: ignore
import pandas as pd

st.subheader("Academics")

data = {
    'Qualification': ['Research Exchange Student', 'Integrated BS-MS', 'Senior Secondary', 'Higher Secondary'],
    'Year': ['June 2024-present','2021-present', '2020', '2018'],
    'Institute': [ 'Goethe University Frankfurt, Germany','IISER Pune, India', 'GHPS Wayanad, India', 'PIES Abu Dhabi, UAE']
}

df = pd.DataFrame(data)

# Display table using st.table
st.dataframe(df, hide_index=True, use_container_width=True)

st.divider()

st.subheader("Achievements")

grep = ' Winter 2024-25'
insp = ' 2021-present'
st.text(f'Goethe Research Experience Program(GREP) Fellow  {grep.rjust(60,'-')}')

st.text(f'INSPIRE-SHE Scholar {insp.rjust(99,'-')}')
