import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd

# Initialize Supabase connection
conn = st.connection("supabase", type=SupabaseConnection)

# Fetch roundwise prices
@st.cache_data(ttl=600)  # Cache results for 10 minutes
def get_roundwise_prices():
    response = conn.query("*", table="roundwise_prices").execute()
    return pd.DataFrame(response.data)

# Load data
df = get_roundwise_prices()

# Display in Streamlit
st.title("Roundwise Prices Dashboard")

if df.empty:
    st.warning("No data found!")
else:
    st.dataframe(df)
    st.line_chart(df.set_index("round")["price"])  # Adjust column names accordingly
