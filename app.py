import streamlit as st
import PyPDF2
import time

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="HireMe AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# SESSION STATE
# ---------------------------
pages = [
    "🏠 Home",
    "📊 Dashboard",
    "🧠 Skills Analysis",
    "🎤 Interview Coach",
    "📚 Theory Center",
    "📄 Report"
]

if "current_page" not in st.session_state:
    st.session_state.current_page = 0

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# ---------------------------
# CSS
# ---------------------------
st.markdown("""
<style>

body{
background:linear-gradient(135deg,#0f172a,#1e293b,#111827);
}

.block-container{
padding-top:0rem !important;
padding-bottom:2rem !important;
padding-left:2rem !important;
padding-right:2rem !important;
max-width:100% !important;
}

header{visibility:hidden;}

[data-testid="stHeader"]{
background:transparent !important;
height:0px !important;
}

[data-testid="stToolbar"]{
top:0.5rem !important;
right:2rem !important;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#0f172a,#1e3a8a);
}

.stButton>button{
width:100%;
border-radius:12px;
background:linear-gradient(90deg,#06b6d4,#3b82f6);
color:white;
font-weight:bold;
border:none;
padding:12px;
}

.stDownloadButton>button{
width:100%;
border-radius:12px;
background:linear-gradient(90deg,#10b981,#059669);
color:white;
font-weight:bold;
border:none;
padding:12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# FUNCTIONS
# ---------------------------
def extract_text(file):
    pdf = PyPDF2.PdfReader(file)
    txt = ""
    for page in pdf.pages:
        content = page.extract_text()
        if content:
            txt += content
    return txt

def analyze(text):
    txt = text.lower()

    skills = []
    keywords = [
        "python","sql","java","flutter","dart",
        "html","css","javascript","react",
        "communication","leadership","git"
    ]

    for k in keywords:
        if k in txt:
            skills.append(k)

    score = min(60 + len(skills)*5, 98)
    ats = min(65 + len(skills)*4, 96)

    return score, ats, skills

def next_page():
    if st.session_state.current_page < len(pages)-1:
        st.session_state.current_page += 1

def prev_page():
    if st.session_state.current_page > 0:
        st.session_state.current_page -= 1

# ---------------------------
# SIDEBAR
# ---------------------------
with st.sidebar:
    st.title("🤖 HireMe AI")

    selected = st.radio(
        "Navigation",
        pages,
        index=st.session_state.current_page
    )

    st.session_state.current_page = pages.index(selected)

page = pages[st.session_state.current_page]

# ---------------------------
# DATA
# ---------------------------
score = 0
ats = 0
skills = []

if st.session_state.analyzed:
    score, ats, skills = analyze(st.session_state.resume_text)

# =============================
# HOME
# =============================
if page == "🏠 Home":

    st.markdown("""
    <div style="
    background:white;
    padding:55px 40px;
    border-radius:28px;
    box-shadow:0 20px 45px rgba(0,0,0,0.08);
    text-align:center;
    margin-bottom:25px;">

    <div style="font-size:18px;font-weight:700;color:#2563eb;letter-spacing:2px;">
    🤖 AI CAREER PLATFORM
    </div>

    <div style="font-size:58px;font-weight:900;color:#0f172a;margin-top:10px;">
    HireMe AI
    </div>

    <div style="font-size:24px;font-weight:700;color:#334155;margin-top:10px;">
    AI-Powered Resume Intelligence Platform
    </div>

    <div style="font-size:18px;color:#64748b;margin-top:15px;">
    ATS analysis, skills gap detection, interview prep and career growth insights.
    </div>

    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("📄 Upload Resume PDF", type=["pdf"])

    if uploaded:
        if st.button("🚀 Analyze Resume"):
            with st.spinner("Analyzing Resume..."):
                time.sleep(2)

            st.session_state.resume_text = extract_text(uploaded)
            st.session_state.analyzed = True
            st.success("Resume analyzed successfully!")

# =============================
# DASHBOARD
# =============================
elif page == "📊 Dashboard":

    st.markdown("""
    <div style="
    background:white;
    padding:30px;
    border-radius:24px;
    margin-bottom:20px;">
    <div style="font-size:36px;font-weight:900;color:#0f172a;">
    📊 Resume Performance Dashboard
    </div>
    <div style="font-size:18px;color:#64748b;">
    AI scoring insights and recruiter readiness.
    </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.analyzed:
        c1,c2,c3 = st.columns(3)

        c1.metric("Resume Score", f"{score}/100")
        c2.metric("ATS Match", f"{ats}%")
        c3.metric("Skills Found", len(skills))
    else:
        st.warning("Please upload resume first.")

# =============================
# SKILLS
# =============================
elif page == "🧠 Skills Analysis":

    st.markdown("""
    <div style="
    background:white;
    padding:30px;
    border-radius:24px;
    margin-bottom:20px;">
    <div style="font-size:36px;font-weight:900;color:#0f172a;">
    🧠 Skills Intelligence Center
    </div>
    <div style="font-size:18px;color:#64748b;">
    Detect strengths and missing skills.
    </div>
    </div>
    """, unsafe_allow_html=True)

    if skills:
        for s in skills:
            st.success(s)
    else:
        st.info("Upload resume first.")

# =============================
# INTERVIEW
# =============================
elif page == "🎤 Interview Coach":

    st.markdown("""
    <div style="
    background:white;
    padding:30px;
    border-radius:24px;
    margin-bottom:20px;">
    <div style="font-size:36px;font-weight:900;color:#0f172a;">
    🎤 Smart Interview Coach
    </div>
    <div style="font-size:18px;color:#64748b;">
    Practice common HR & technical questions.
    </div>
    </div>
    """, unsafe_allow_html=True)

    qs = [
        "Tell me about yourself.",
        "Why should we hire you?",
        "Explain your project.",
        "What are your strengths?",
        "Where do you see yourself in 5 years?"
    ]

    for q in qs:
        st.success(q)

# =============================
# THEORY
# =============================
elif page == "📚 Theory Center":

    st.markdown("""
    <div style="
    background:white;
    padding:30px;
    border-radius:24px;
    margin-bottom:20px;">
    <div style="font-size:36px;font-weight:900;color:#0f172a;">
    📚 Career Learning Hub
    </div>
    <div style="font-size:18px;color:#64748b;">
    ATS mastery, resume psychology and interview strategy.
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("Use keywords from job description.")
    st.info("Use action verbs like Built, Led, Created.")
    st.info("Keep resume concise and clear.")

# =============================
# REPORT
# =============================
elif page == "📄 Report":

    st.markdown("""
    <div style="
    background:white;
    padding:30px;
    border-radius:24px;
    margin-bottom:20px;">
    <div style="font-size:36px;font-weight:900;color:#0f172a;">
    📄 Executive Resume Report
    </div>
    <div style="font-size:18px;color:#64748b;">
    Download your AI-generated summary.
    </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.analyzed:

        report = f"""
HireMe AI Report

Resume Score: {score}/100
ATS Match: {ats}%
Skills Found: {len(skills)}

Detected Skills:
{", ".join(skills)}
"""

        st.download_button(
            "📄 Download Report",
            report,
            file_name="hireme_ai_report.txt"
        )
    else:
        st.warning("Upload resume first.")

# ---------------------------
# NAV BUTTONS
# ---------------------------
st.write("")

left, center, right = st.columns([1,4,1])

with left:
    if st.session_state.current_page > 0:
        st.button("⬅ Previous", on_click=prev_page)

with right:
    if st.session_state.current_page < len(pages)-1:
        st.button("Next ➡", on_click=next_page)