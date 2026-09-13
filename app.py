# Import packages
import streamlit as st
import pandas as pd
from assets.styling import

# Add a title
st.title('This is a title')

# Markdown for text formatting
md_heading = """
# Heading level 1
## Heading level 2
### Heading level 3
###### Heading level 6
"""
st.markdown(md_heading)

md_list = """
- item 1
- item 2

1. numbered item 1
2. numbered item 2
4. numbered item 3
"""
st.markdown(md_list)

md_txt = """
This is a sentence.   
**This sentence is in bold text.** *This sentence is in italic text.*
"""
st.markdown(md_txt)

# insert an image
# st.image('assets/pikachu.jpg', width=300)

# columns
col1, col2 = st.columns(2, border=False)
with col1:
    st.image('assets/pikachu.jpg', width=300)
with col2:
    with st.container(border=True, height=300):
        md_txt = 'A suprised Pikachu'
        st.markdown(md_txt)

# Metrics
st.metric('Score:', 97, border=True)

# CSV

# Read data
df = pd.read_csv('assets/penguins.csv')

def hide_toolbar(key):
    st.markdown(
        f"""
        <style>
        .st-key-{key} [data-testid="stElementToolbar"] {{
            display: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

with st.container(key='no_download'):
    hide_toolbar(key='no_download')
    st.dataframe(df)


