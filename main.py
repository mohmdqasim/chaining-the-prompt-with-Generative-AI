import streamlit as st
from utlis import get_restaurant_and_menu_items
st.title("Restaurant Menu Application")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "American", "Maxican", "Thai", "Punjabi", "Pakistan"))

if cuisine:
    response = generate_restaurant_name_and_intems(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
