# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


# ------------------------ General ------------------------


def HomeNav():

    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


# ------------------------ Economist ------------------------
def economy_home():
    st.sidebar.page_link(
        "pages/31_Economist_Home.py", label="Home", icon="🏦"
    )


def PolStratAdvHomeNav():
    st.sidebar.page_link(
        "pages/32_Historical_Data.py", label="Historical Data Viewer", icon="💰"
    )


def viewFavoritesNav():
    st.sidebar.page_link(
        "pages/saved_drafts.py", label="Proposed Policy", icon="🧾"
    )


# ------------------------ Lobbyist ----------------------------


def MakeNoteNav():
    st.sidebar.page_link("pages/40_Lobbyist.py",
                         label="Make a New Note", icon="✍️")


def ViewNotesNav():
    st.sidebar.page_link("pages/43_Lobbyist2.py", label="View Notes", icon="📝")


# ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("Home.py", label="Go Home", icon="🏠")

# ------------------------ Policy Maker Role ------------------------


def PolicyMakerNav():
    st.sidebar.page_link("pages/00_Policy_Maker_Home.py",
                         label="Test New Set", icon="🗒️")
    st.sidebar.page_link(
        "pages/46_PolicyMaker_ViewFavorites.py", label="View Saved Policies", icon="⌨️"
    )


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "economist":
            economy_home()
            PolStratAdvHomeNav()
            viewFavoritesNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()

        if st.session_state["role"] == "Lobbyist":
            MakeNoteNav()
            ViewNotesNav()

        if st.session_state['role'] == "Policy Maker":
            PolicyMakerNav()

            # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.session_state.clear()
            st.switch_page("Home.py")
