import streamlit as st

# The URL to redirect to
redirect_url = "https://github.com/"

# HTML code for the redirection
redirect_html = f"""
    <html>
        <head>
            <meta http-equiv="refresh" content="0;URL='{redirect_url}'" />
        </head>
        <body>
            <a href="{redirect_url}">Gyanvarsha</a>...
        </body>
    </html>
"""

# Display the HTML code
st.markdown(redirect_html, unsafe_allow_html=True)
