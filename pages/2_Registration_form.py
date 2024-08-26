import streamlit as st
from Home import face_rec
from streamlit_webrtc import webrtc_streamer
import av
import numpy as np

# st.set_page_config(page_title='Registration Form',layout='centered')
st.subheader('Registration Form')

class RegistrationForm:
    def __init__(self):
        self.face_embedding = None

    def get_embedding(self, img):
        # Mock implementation; replace this with your actual face embedding code
        return img, np.random.rand(128)

    def save_data_in_redis_db(self, name, role):
        # Mock implementation; replace this with your actual data saving code
        print(f"Saving data for {name} with role {role}")
        return True

# init registration form
registration_form = face_rec.RegistrationForm()

# Step-1: Collect person name and role
# form
person_name = st.text_input(label='Name', placeholder='First & Last Name')
role = st.selectbox(label='Select your Role', options=('Student', 'Teacher'))

# step-2: Collect facial embedding of that person
def video_callback_func(frame):
    img = frame.to_ndarray(format='bgr24')  # 3d array bgr
    reg_img, embedding = registration_form.get_embedding(img)

    # two step process
    # 1st step save data into local computer txt
    if embedding is not None:
        with open('face_embedding.txt', mode='ab') as f:
            np.savetxt(f, embedding)

    return av.VideoFrame.from_ndarray(reg_img, format='bgr24')

webrtc_streamer(key='registration', video_frame_callback=video_callback_func,
                rtc_configuration={  # Add this config
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    })

# step-3: save the data in redis database
if st.button('Submit'):
    return_val = registration_form.save_data_in_redis_db(person_name, role)
    if return_val == True:
        st.success(f"{person_name} registered successfully")
    elif return_val == 'name_false':
        st.error('Please enter the name: Name cannot be empty or spaces')
    elif return_val == 'file_false':
        st.error('face_embedding.txt is not found. Please refresh the page and execute again.')

        
        
       

