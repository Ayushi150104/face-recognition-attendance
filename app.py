import streamlit as st
import face_recognition

# Page config
st.set_page_config(
    page_title="Face Recognition Attendance",
    page_icon="📸",
    layout="centered"
)

# Theme toggle
theme = st.toggle("🌙 Dark Theme", value=True)
toggle_text_color = "#ffffff" if theme else "#111827"
# Theme colors
if theme:
    bg_gradient = "linear-gradient(90deg, #0f172a, #1e293b, #020617)"
    text_color = "white"
    box_bg = "rgba(255,255,255,0.08)"
    border_color = "rgba(255,255,255,0.15)"
    shadow_color = "rgba(0,0,0,0.25)"
else:
    bg_gradient = "linear-gradient(90deg, #0f172a, #134e4a, #022c22)"
    text_color = "#111827"
    box_bg = "rgba(255,255,255,0.75)"
    border_color = "rgba(0,0,0,0.08)"
    shadow_color = "rgba(0,0,0,0.10)"

# Custom CSS
st.markdown(f"""
<style>   
            /* Header buttons white */
[data-testid="stHeader"] {{
            background: transparent !important;
            box-shadow: none !important;
}}

[data-testid="stHeader"] button {{
    padding-top:2rem !important;
}}

[data-testid="stHeader"] svg {{
    fill: white !important;
}}
                     
/* Full page background */
.stApp {{
    background: {bg_gradient};
    color: {text_color};
}}

/* Deploy button text always white */
button[kind="header"] {{
    color: white !important;
}}

button[kind="header"] * {{
    color: white !important;
}}

button[kind="header"] svg {{
    fill: white !important;
}}

/* Main title */
.title {{
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-bottom: 18px;
    margin-top: 10px;
}}

/* Glass box */
.subtitle-box {{
    width: 100%;
    max-width: 700px;
    margin: 0 auto 25px auto;
    padding: 18px 20px;
    border-radius: 18px;
    background: {box_bg};
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid {border_color};
    box-shadow: 0 8px 20px {shadow_color};
    text-align: center;
}}

/* Bold box text */
.subtitle-text {{
    font-size: 22px;
    font-weight: 700;
    color: {text_color};
    letter-spacing: 0.4px;
}}

/* Camera input style */
[data-testid="stCameraInput"] {{
    border-radius: 20px;
    overflow: hidden;
}}

/* Camera button text always white */
[data-testid="stCameraInput"] button {{
    color: white !important;
}}

[data-testid="stCameraInput"] button p {{
    color: white !important;
}}

[data-testid="stCameraInput"] * {{
    color: white !important;
}}

/* Success glass */
.stSuccess {{
    background: {box_bg} !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 15px !important;
    border: 1px solid {border_color} !important;
    color: {text_color} !important;
}}

/* Error glass */
.stError {{
    background: rgba(255,0,0,0.08) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 15px !important;
    border: 1px solid {border_color} !important;
    color: {text_color} !important;
}}

</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    '<div class="title">📸 Face Recognition Attendance</div>',
    unsafe_allow_html=True
)

# First box
st.markdown(
    """
    <div class="subtitle-box">
        <div class="subtitle-text">
            Mark attendance instantly using face recognition
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Second box
st.markdown(
    """
    <div class="subtitle-box">
        <div class="subtitle-text">
            📷 Take your photo
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Camera section
with st.container():
    uploaded_file = st.camera_input(" ")

    if uploaded_file is not None:

        image = face_recognition.load_image_file(uploaded_file)

        test_encodings = face_recognition.face_encodings(image)

        if len(test_encodings) == 0:
            st.error("❌ No face detected")
        else:
            test_encoding = test_encodings[0]

            deb_image = face_recognition.load_image_file("Debalina Jana.jpeg")
            deb_encoding = face_recognition.face_encodings(deb_image)[0]

            ayu_image = face_recognition.load_image_file("Ayushi Choudhary.jpeg")
            ayu_encoding = face_recognition.face_encodings(ayu_image)[0]

            known_encodings = [deb_encoding, ayu_encoding]
            known_names = ["Debalina", "Ayushi"]

            matches = face_recognition.compare_faces(
                known_encodings,
                test_encoding
            )

            if True in matches:
                matched_index = matches.index(True)
                st.success(
                    f"✅ Attendance Marked | {known_names[matched_index]}"
                )
            else:
                st.error("❌ Face Not Matched")

# Footer
st.markdown("---")
st.caption("Built with Python • Streamlit • Face Recognition")