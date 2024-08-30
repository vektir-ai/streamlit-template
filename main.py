import streamlit as st

# Page config ---------------------------------------------------------------
st.set_page_config(
    page_title="vektir.ai", 
    page_icon="images/vektir-ai-black.png", 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items=None
    )

# Initialize session state ---------------------------------------------------
if "role" not in st.session_state:
    st.session_state.role = None
if "email" not in st.session_state:
    st.session_state.email = None
if "password" not in st.session_state:
    st.session_state.password = None

# Global variables -----------------------------------------------------------
ROLES = [None, "Client", "Admin"]
CLIENT_EMAIL = "client@email.com"
CLIENT_PASSWORD = "client"
ADMIN_EMAIL = "admin@email.com"
ADMIN_PASSWORD = "admin"

# Account ----------------------------------------------------------------------
def login():
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()

def logout():
    st.session_state.role = None
    st.rerun()

role = st.session_state.role

# Pages ----------------------------------------------------------------------
logout_page = st.Page(
    logout, 
    title="Log out", 
    icon=":material/logout:")

settings = st.Page(
    "settings.py", 
    title="Settings", 
    icon=":material/settings:")

support = st.Page(
    "client_panel/ask_question.py",
    title="Support",
    icon=":material/help:",
    )

client = st.Page(
    "client_panel/client.py",
    title="Client Panel",
    icon=":material/help:",
    default=(role == "Client"),)

admin = st.Page(
    "admin_panel/admin.py",
    title="Admin Panel",
    icon=":material/person_add:",
    default=(role == "Admin"),)



account_pages = [logout_page, support, settings]
client_panels = [client ]
admin_panels = [admin]


# Main -----------------------------------------------------------------------
st.title("Welcome to vektir.ai :wave:")
st.logo("images/vektir-ai-black.png", icon_image="images/vektir-ai-black.png")

page_dict = {}
if st.session_state.role in ["Client", "Admin"]:
    page_dict["Client"] = client_panels
    # page_dict["Support"] = support todo: bug

if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_panels

if len(page_dict) > 0:
    pg = st.navigation(page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()