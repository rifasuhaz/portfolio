import streamlit as st # type: ignore
st.set_page_config(layout="wide")

home = st.Page("navpage/Home.py")
acads = st.Page("navpage/Acads.py")
projs = st.Page("navpage/Projects.py")
travel = st.Page("navpage/Travel.py")

pages = st.navigation([home,acads,projs,travel], position='hidden')

col1, col2, col3, col4 = st.columns(4)
col1.page_link("navpage/Home.py")
col2.page_link("navpage/Acads.py")
col3.page_link("navpage/Projects.py")
col4.page_link("navpage/Travel.py")

pages.run()



# with st.container(width=300):
# st.image("wallpaper.png")
# row1 = st.columns(3)
# row2 = st.columns(3)

# for col in row1 + row2:
#     tile = col.container(height=120)
#     tile.title(":balloon:")
