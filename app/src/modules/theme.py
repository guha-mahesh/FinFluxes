import streamlit as st


def custom_style():
    st.set_page_config(layout='wide')
    st.markdown(
        """
        <style>
        /* Import Poppins font from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        [data-testid="stSidebar"] {
            background-color: #18435a;
        }
        

        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        .stApp {
            font-family: 'Poppins', sans-serif !important;
        }

        .stApp * {
            font-family: 'Poppins', sans-serif !important;
        }
        section[data-testid="stSidebar"] .stButton > button {
        color: black;
        border: none;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        border: 2px solid black;
        transition: all 0.3s ease;
        background: transparent;
    }

    section[data-testid="stSidebar"] .stButton > button:hover {
        transform: translateY(-2px);
        border: 2px solid #F0A76C
    }

        </style>
        
        """,
        unsafe_allow_html=True
    )

def welcome_banner(desc):
    st.markdown("""
    <style>
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .welcome-banner {{
        background: linear-gradient(90deg, rgba(240, 167, 108, 0.7) 0%, rgba(240, 146, 64, 0.7) 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        font-family: "Andale Mono", "Gill Sans", "Verdana", "Tahoma", sans-serif !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(240, 167, 108, 0.2);
        animation: fadeInUp 0.8s ease-out forwards;
        position: relative;
        overflow: hidden;
    }}
    
    .welcome-banner::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: shimmer 2s ease-in-out infinite;
    }}
    
    @keyframes shimmer {{
        0% {{
            left: -100%;
        }}
        100% {{
            left: 100%;
        }}
    }}
    
    .welcome-title {{
        color: #FFFFFF !important;
        margin: 0;
        font-family: "Trebuchet MS", "Gill Sans", "Tahoma", sans-serif !important;
        font-weight: 600;
        font-size: 3rem;
        animation: fadeInUp 0.8s ease-out 0.2s both;
    }}
    
    .welcome-picture {{
        color: rgba(255, 255, 255, 30) !important;
    }}
    
    .welcome-subtitle {{
        color: rgba(255, 255, 255, 0.9) !important;
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        animation: fadeInUp 0.8s ease-out 0.4s both;
    }}
    </style>
    
    <div class='welcome-banner'>
        <h1 class='welcome-title'>
            Welcome, {}
        </h1>
        <p class='welcome-subtitle'>
            {}
        </p>
    </div>
""".format(st.session_state['first_name'], desc), unsafe_allow_html=True)
    
def banner(title, desc):
        st.markdown("""
    <style>
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .animated-banner {{
        background: linear-gradient(90deg, rgba(240, 167, 108, 0.7) 0%, rgba(240, 146, 64, 0.7) 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(240, 167, 108, 0.2);
        animation: fadeInUp 0.8s ease-out forwards;
        position: relative;
        overflow: hidden;
    }}
    
    .animated-banner::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: shimmer 2s ease-in-out infinite;
    }}
    
    @keyframes shimmer {{
        0% {{
            left: -100%;
        }}
        100% {{
            left: 100%;
        }}
    }}
    
    .animated-title {{
        color: #FFFFFF !important;
        margin: 0;
        font-weight: 600;
        font-size: 3rem;
        animation: fadeInUp 0.8s ease-out 0.2s both;
    }}
    
    .animated-picture {{
        color: rgba(255, 255, 255, 30) !important;
    }}
    
    .animated-subtitle {{
        color: rgba(255, 255, 255, 0.9) !important;
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        animation: fadeInUp 0.8s ease-out 0.4s both;
    }}
    </style>
    
    <div class='animated-banner'>
        <h1 class='animated-title'>
            {}
        </h1>
        <p class='animated-subtitle'>
            {}
        </p>
    </div>
""".format(title, desc), unsafe_allow_html=True)

def banner2(title, desc):
             st.markdown("""
    <style>
    
    .banner2-background {{
        background: #F0A76C;
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    
    .banner2-title {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
        color:  #FFFFFF !important;
    }}
    
    .banner2-subtitle {{
        color: #e2e8f0;
        margin: 0;
        font-size: 1.1rem;
    }}
    </style>
    
    <div class='banner2-background'>
        <h2 class='banner2-title'>
            {}
        </h2>
        <p class='banner2-subtitle'>
            {}
        </p>
    </div>
""".format(title, desc), unsafe_allow_html=True)

def blue_banner(title, desc):
             st.markdown("""
    <style>
    
    .blue_banner-background {{
        background: #18435a;
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    
    .blue_banner-title {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
        color:  #FFFFFF !important;
    }}
    
    .blue_banner-subtitle {{
        color: #e2e8f0;
        margin: 0;
        font-size: 1.1rem;
    }}
    </style>
    
    <div class='blue_banner-background'>
        <h2 class='blue_banner-title'>
            {}
        </h2>
        <p class='blue_banner-subtitle'>
            {}
        </p>
    </div>
""".format(title, desc), unsafe_allow_html=True)


def logOut():
    pass
