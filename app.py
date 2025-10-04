"""
Streamlit Resume Matcher Application - SECURE VERSION with Password Protection & Rate Limiting
"""

import streamlit as st
from matcher import rank_resumes
from utils import extract_text
from gemini_api import generate_fit_summary, MissingAPIKeyError
import base64
from concurrent.futures import ThreadPoolExecutor
from logger import logger
import time
import os
from collections import defaultdict
from datetime import datetime

# ============================================
# SECURITY CONFIGURATION
# ============================================

# Rate Limiting Settings
MAX_REQUESTS_PER_HOUR = 5  # Each user can process 5 resume batches per hour
MAX_DAILY_REQUESTS = 20     # Maximum 20 batches per day per user
request_timestamps = defaultdict(list)
daily_requests = defaultdict(lambda: {'date': None, 'count': 0})

# Demo Mode (set to True to disable AI features and use pre-computed results)
DEMO_MODE = os.getenv('DEMO_MODE', 'false').lower() == 'true'

# Maintenance Mode (emergency kill switch)
MAINTENANCE_MODE = os.getenv('MAINTENANCE_MODE', 'false').lower() == 'true'


# ============================================
# SECURITY FUNCTIONS
# ============================================

def check_password():
    """Returns True if user entered correct password."""
    
    def password_entered():
        # Check against secrets or environment variable
        correct_password = st.secrets.get("app_password", os.getenv("APP_PASSWORD", "demo123"))
        
        if st.session_state["password"] == correct_password:
            st.session_state["password_correct"] = True
            st.session_state["user_authenticated_at"] = datetime.now()
            del st.session_state["password"]  # Don't store password
            logger.info("User authenticated successfully")
        else:
            st.session_state["password_correct"] = False
            logger.warning("Failed authentication attempt")

    # First run - show password input
    if "password_correct" not in st.session_state:
        st.info("🔐 **Portfolio Demo Access Required**")
        st.markdown("""
        This is a demonstration application for portfolio purposes.
        
        **For Recruiters/Employers:** Contact me for access credentials.
        - Email: abhinavbajpai@example.com
        - LinkedIn: [Your LinkedIn]
        
        **Demo Credentials:** Use `demo123` for limited access (5 requests/hour)
        """)
        
        st.text_input(
            "Enter Access Password", 
            type="password", 
            on_change=password_entered, 
            key="password"
        )
        return False
    
    # Incorrect password
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Enter Access Password", 
            type="password", 
            on_change=password_entered, 
            key="password"
        )
        st.error("😕 Incorrect password. Please try again or contact the developer.")
        return False
    
    # Authenticated
    else:
        return True


def get_user_id():
    """Generate a unique user ID for rate limiting."""
    # Use session ID as user identifier
    if '_user_id' not in st.session_state:
        st.session_state._user_id = str(hash(str(st.session_state)))[:16]
    return st.session_state._user_id


def check_hourly_rate_limit(user_id):
    """Check if user has exceeded hourly rate limit."""
    now = time.time()
    hour_ago = now - 3600
    
    # Clean old requests (older than 1 hour)
    request_timestamps[user_id] = [
        ts for ts in request_timestamps[user_id] 
        if ts > hour_ago
    ]
    
    # Check limit
    current_count = len(request_timestamps[user_id])
    if current_count >= MAX_REQUESTS_PER_HOUR:
        logger.warning(f"User {user_id} exceeded hourly rate limit ({current_count}/{MAX_REQUESTS_PER_HOUR})")
        return False, current_count
    
    return True, current_count


def check_daily_rate_limit(user_id):
    """Check if user has exceeded daily rate limit."""
    today = datetime.now().date()
    
    # Reset counter if it's a new day
    if daily_requests[user_id]['date'] != today:
        daily_requests[user_id] = {'date': today, 'count': 0}
    
    # Check limit
    current_count = daily_requests[user_id]['count']
    if current_count >= MAX_DAILY_REQUESTS:
        logger.warning(f"User {user_id} exceeded daily rate limit ({current_count}/{MAX_DAILY_REQUESTS})")
        return False, current_count
    
    return True, current_count


def record_request(user_id):
    """Record a request for rate limiting."""
    now = time.time()
    request_timestamps[user_id].append(now)
    daily_requests[user_id]['count'] += 1
    
    logger.info(f"Request recorded for user {user_id} | Hourly: {len(request_timestamps[user_id])}/{MAX_REQUESTS_PER_HOUR} | Daily: {daily_requests[user_id]['count']}/{MAX_DAILY_REQUESTS}")


def log_usage(action, user_id, details=None):
    """Log usage for monitoring and analytics."""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'user_id': user_id,
        'action': action,
        'details': details or {}
    }
    
    # Log to file for monitoring
    try:
        import json
        with open('usage_logs.json', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    except Exception as e:
        logger.error(f"Failed to write usage log: {e}")


# ============================================
# STREAMLIT APP
# ============================================

st.set_page_config(
    page_title="Resume Matcher - AI-Powered Candidate Ranking",
    page_icon="🔍",
    layout="wide"
)

# Check for maintenance mode
if MAINTENANCE_MODE:
    st.error("🔧 **System Under Maintenance**")
    st.info("The application is temporarily unavailable for updates. Please check back later.")
    st.markdown("**Contact:** abhinavbajpai@example.com")
    st.stop()

# Check authentication
if not check_password():
    st.stop()

# Show demo mode warning
if DEMO_MODE:
    st.warning("🎭 **Demo Mode Active:** AI summaries disabled. Using basic matching only.")

# Title and description
st.title("🔍 Candidate Recommendation Engine")
st.markdown("""
**AI-Powered Resume Ranking System** | Built with Google Gemini AI & Scikit-learn

Upload job descriptions and candidate resumes to get instant AI-powered matching and ranking.
""")

# Sidebar with info
with st.sidebar:
    st.markdown("### 👤 About This Tool")
    st.markdown("""
    This application uses:
    - 🤖 **Google Gemini AI** for embeddings & summaries
    - 📊 **Scikit-learn** for similarity scoring
    - 🎨 **Streamlit** for the interface
    
    **For Portfolio/Demo Purposes**
    
    Rate Limits:
    - 5 batches per hour
    - 20 batches per day
    """)
    
    # Show current usage
    user_id = get_user_id()
    hourly_ok, hourly_count = check_hourly_rate_limit(user_id)
    daily_ok, daily_count = check_daily_rate_limit(user_id)
    
    st.markdown("### 📊 Your Usage")
    st.progress(hourly_count / MAX_REQUESTS_PER_HOUR)
    st.caption(f"Hourly: {hourly_count}/{MAX_REQUESTS_PER_HOUR}")
    
    st.progress(daily_count / MAX_DAILY_REQUESTS)
    st.caption(f"Daily: {daily_count}/{MAX_DAILY_REQUESTS}")
    
    st.markdown("---")
    st.markdown("""
    ### 🔗 Links
    - [Source Code](https://github.com/Abhinav-SU/resume-matcher-app)
    - [Portfolio](https://abhinavbajpai.online)
    - [LinkedIn](https://linkedin.com/in/yourprofile)
    """)
    
    st.markdown("---")
    st.caption("© 2025 Abhinav Bajpai")


# Initialize session state
if "results" not in st.session_state:
    st.session_state.results = []
if "job_desc" not in st.session_state:
    st.session_state.job_desc = ""


# ============================================
# MAIN PAGE
# ============================================

if "selected" not in st.session_state:
    # Input section
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Job Description")
        job_desc = st.text_area(
            "Enter the job requirements, skills, and qualifications",
            height=300,
            placeholder="Example:\n\nWe are looking for a Senior Python Developer with:\n- 5+ years of Python experience\n- Experience with Django/Flask\n- Strong SQL skills\n- Cloud experience (AWS/Azure)\n..."
        )
    
    with col2:
        st.subheader("📤 Upload Resumes")
        resumes = st.file_uploader(
            "Upload candidate resumes (PDF or DOCX)",
            type=["pdf", "docx"],
            accept_multiple_files=True,
            help="You can upload multiple resumes at once"
        )
        
        if resumes:
            st.success(f"✅ {len(resumes)} resume(s) uploaded")
    
    st.markdown("---")
    
    if st.button("🚀 Match & Rank Candidates", type="primary", use_container_width=True):
        # Get user ID for rate limiting
        user_id = get_user_id()
        
        # Check rate limits
        hourly_ok, hourly_count = check_hourly_rate_limit(user_id)
        daily_ok, daily_count = check_daily_rate_limit(user_id)
        
        if not hourly_ok:
            st.error(f"⏰ **Hourly Rate Limit Exceeded**")
            st.warning(f"You've used {hourly_count}/{MAX_REQUESTS_PER_HOUR} requests this hour. Please try again later.")
            st.info("Limit resets in less than 1 hour from your first request.")
            log_usage("rate_limit_exceeded", user_id, {"type": "hourly", "count": hourly_count})
            st.stop()
        
        if not daily_ok:
            st.error(f"📅 **Daily Rate Limit Exceeded**")
            st.warning(f"You've used {daily_count}/{MAX_DAILY_REQUESTS} requests today. Please come back tomorrow.")
            st.info("Daily limit resets at midnight UTC.")
            log_usage("rate_limit_exceeded", user_id, {"type": "daily", "count": daily_count})
            st.stop()
        
        # Validate inputs
        if not job_desc or not resumes:
            st.warning("⚠️ Please provide both job description and resumes")
            st.stop()
        
        # Record this request
        record_request(user_id)
        log_usage("match_started", user_id, {"resume_count": len(resumes)})
        
        try:
            with st.spinner("🔄 Processing resumes... This may take a moment."):
                results = rank_resumes(job_desc, resumes)
                st.session_state.results = results
                st.session_state.job_desc = job_desc
                
                log_usage("match_completed", user_id, {
                    "resume_count": len(resumes),
                    "top_score": results[0]["score"] if results else 0
                })
                
                st.success(f"✅ Successfully ranked {len(results)} candidates!")
                st.rerun()
                
        except MissingAPIKeyError:
            st.error("❌ **API Key Missing**")
            st.info("The Gemini API key is not configured. Please contact the administrator.")
            log_usage("error_missing_api_key", user_id)
            
        except Exception as e:
            st.error(f"❌ **Error:** {str(e)}")
            logger.error(f"Matching error: {e}", exc_info=True)
            log_usage("error_general", user_id, {"error": str(e)})

else:
    # Results page (same as original app.py)
    st.subheader(f"📊 Top Candidates for: {st.session_state.job_desc[:100]}...")
    
    if st.button("← Back to Upload"):
        del st.session_state.selected
        st.rerun()

    results = st.session_state.results[:10]
    
    for idx, res in enumerate(results):
        with st.expander(f"🏆 Rank {idx+1}: {res['filename']} - Match Score: {res['score']:.1%}", expanded=(idx < 3)):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                if "summary" in res and res["summary"]:
                    st.markdown("**💡 AI-Generated Summary:**")
                    st.info(res["summary"])
                else:
                    st.markdown("**💡 Why this candidate?**")
                    if st.button(f"Generate AI Summary", key=f"sum_{idx}"):
                        if DEMO_MODE:
                            st.warning("AI summaries disabled in demo mode.")
                        else:
                            user_id = get_user_id()
                            with st.spinner("Generating summary..."):
                                try:
                                    summary = generate_fit_summary(
                                        st.session_state.job_desc,
                                        res["resume_text"]
                                    )
                                    st.session_state.results[idx]["summary"] = summary
                                    log_usage("summary_generated", user_id, {"filename": res['filename']})
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Failed to generate summary: {str(e)}")
                                    log_usage("error_summary", user_id, {"error": str(e)})
            
            with col2:
                st.metric("Match Score", f"{res['score']:.1%}")
                
                # Download resume text
                b64 = base64.b64encode(res["resume_text"].encode()).decode()
                href = f'<a href="data:text/plain;base64,{b64}" download="{res["filename"]}.txt">📥 Download Text</a>'
                st.markdown(href, unsafe_allow_html=True)
            
            # Show resume preview
            with st.expander("📄 View Full Resume Text"):
                st.text_area(
                    "Resume Content",
                    res["resume_text"],
                    height=300,
                    key=f"text_{idx}",
                    disabled=True
                )

    st.markdown("---")
    st.caption("💡 Tip: Click 'View' to see detailed AI analysis of why each candidate matches the job description.")


# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with ❤️ by Abhinav Bajpai | <a href='https://abhinavbajpai.online'>Portfolio</a> | <a href='https://github.com/Abhinav-SU/resume-matcher-app'>GitHub</a></p>
    <p style='font-size: 0.8em;'>For demonstration and portfolio purposes. Rate limited to prevent abuse.</p>
</div>
""", unsafe_allow_html=True)
