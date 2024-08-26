import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title='Attendance System',
    layout='wide'
)

name = 'attendence:logs'

def load_logs(name, end=-1):
    logs_list = face_rec.r.lrange(name, start=0, end=end)  # Extract all data from the Redis database
    return logs_list

def start_face_recognition():
    with st.spinner('Retrieving data from Redis DB...'):
        redis_face_db = face_rec.retrive_data(name='academy:register')
        st.dataframe(redis_face_db)
    
    st.success("Data successfully retrieved from Redis.")

# Initialize session state for toggles
if 'current_expander' not in st.session_state:
    st.session_state['current_expander'] = None

# Function to handle toggle visibility
def toggle_expander(expander_name):
    if st.session_state['current_expander'] == expander_name:
        st.session_state['current_expander'] = None
    else:
        st.session_state['current_expander'] = expander_name

# Custom CSS for a modern, minimalistic look
st.markdown("""
    <style>
    body {
        background-color: #eef2f7;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stHeader {
        font-size: 36px;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 20px;
    }
    .stSubHeader {
        font-size: 24px;
        color: #EEE;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 30px;
    }
    .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        margin-bottom: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px 20px;
        margin-top: 10px;
        width: 100%;
    }
    .stSuccess {
        color: #28a745;
        font-weight: bold;
    }
    .stSpinner {
        color: #1f77b4;
    }
    footer {
        text-align: center;
        font-size: 16px;
        color: #CCC;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Display header and subheader with styled class
st.markdown('<h1 class="stHeader">Attendance System using Face Recognition</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="stSubHeader">Efficient and Secure Attendance Management</h3>', unsafe_allow_html=True)

# GIF URL
gif_url = "https://arabinfotechllc.com/img/timeAttendance.gif"

# Display the GIF
st.image(gif_url, caption="Face Recognition Technology", use_column_width=True)

# Add a brief introduction or description
st.markdown("""
    <p style="font-size:18px; color:#EEE; text-align:center;">
    Leverage cutting-edge face recognition technology for efficient and accurate attendance management.
    </p>
""", unsafe_allow_html=True)

# Load models and connect to Redis db with a more descriptive spinner message
with st.spinner("Initializing: Loading models and connecting to Redis database..."):
    import face_rec

# Display success messages with styled class
st.success('Model loaded successfully')
st.success('Redis db successfully connected')

# Add a section for the dashboard
st.markdown('<h3 class="stHeader">System Dashboard</h3>', unsafe_allow_html=True)

# Create additional buttons and layout for more interactions with individual toggles
col1, col2, col3 = st.columns(3)

# Button for "Start Attendance"
with col1:
    if st.button('Start Attendance'):
        toggle_expander('start_attendance')
    if st.session_state['current_expander'] == 'start_attendance':
        with st.expander("Start Attendance", expanded=True):
            st.info('Starting the face recognition process...')
            time.sleep(2)  # Simulate processing
            person_name = st.text_input(
                label='Enter Your Name',
                placeholder='Enter your first and last name'
            )
            role = st.radio(
                label='Choose Your Role',
                options=['Student', 'Teacher']
            )

# Button for "Stop Attendance"
with col1:
    if st.button('Stop Attendance'):
        toggle_expander('stop_attendance')
    if st.session_state['current_expander'] == 'stop_attendance':
        with st.expander("Stop Attendance", expanded=True):
            with st.spinner('Stopping face recognition process...'):
                time.sleep(2)  # Simulate processing
            st.warning('STOPPED!')

# Button for "View Attendance Records"
with col2:
    if st.button('View Attendance Records'):
        toggle_expander('view_records')
    if st.session_state['current_expander'] == 'view_records':
        with st.expander("View Attendance Records", expanded=True):
            st.info('Fetching attendance records...')
            with st.spinner('Retrieving Data from Redis DB ...'):
                redis_face_db = face_rec.retrive_data(name='academy:register')
                st.dataframe(redis_face_db[['Name', 'Role']])

# Button for "Export Records"
with col2:
    if st.button('Export Records'):
        toggle_expander('export_records')
    if st.session_state['current_expander'] == 'export_records':
        with st.expander("Export Records", expanded=True):
            st.success('Exporting attendance records...')
            st.write(load_logs(name=name))

# Button for "Register"
with col3:
    if st.button('Register'):
        st.info('Opening Registration form...')
        time.sleep(2)
        toggle_expander('settings')
    if st.session_state['current_expander'] == 'settings':
        with st.expander("Settings", expanded=True):
            person_name = st.text_input(label='Name', placeholder='First & Last Name')
            role = st.selectbox(label='Select your Role', options=('Student', 'Teacher'))

# Button for "Refresh Data"
with col3:
    if st.button('Registered Students'):
        toggle_expander('refresh_data')
    if st.session_state['current_expander'] == 'refresh_data':
        with st.expander("Refresh Data", expanded=True):
            with st.spinner('Retrieving Data from Redis DB ...'):
                time.sleep(1)  # Simulate processing
                redis_face_db = face_rec.retrive_data(name='academy:register')
                st.dataframe(redis_face_db[['Name', 'Role']])

# Add a footer with centered text
st.markdown("""
    <footer>
        &copy; 2023 Attendance System | Powered by Face Recognition and Redis
    </footer>
""", unsafe_allow_html=True)
