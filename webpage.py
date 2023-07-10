import streamlit as st

def main():
    # Set the width of the side menu
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            width: 30%;
            background-color: black;
            overflow: hidden;
            transition: width 0.3s ease;
        }
        
        .sidebar:hover .sidebar-content {
            width: 100%;
        }
        
        .sidebar .sidebar-content .stSelectbox label {
            color: red;
        }
        
        .css-17eq0hr {
            background-color: black;
            color: red;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a sidebar menu
    menu_items = ["Home", "About", "Contact"]
    choice = st.sidebar.selectbox("Menu", menu_items)

    # Display the selected page content
    if choice == "Home":
        st.title("Home Page")
        # Add content for the home page
    elif choice == "About":
        st.title("About Page")
        # Add content for the about page
    elif choice == "Contact":
        st.title("Contact Page")
        # Add content for the contact page

if __name__ == "__main__":
    main()
