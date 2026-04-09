import streamlit as st
import face_recognition
import numpy as np

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Face Recognition Attendance",
    page_icon="📸",
    layout="centered"
)

# =========================
# THEME TOGGLE
# =========================
theme = st.toggle("🌙 Dark Theme", value=True)

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

# =========================
# CUSTOM CSS
# =========================
st.markdown(f"""
<style>
.stApp {{
    background: {bg_gradient};
    color: {text_color};
}}

.title {{
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-bottom: 18px;
    margin-top: 10px;
}}

.subtitle-box {{
    width: 100%;
    max-width: 700px;
    margin: 0 auto 25px auto;
    padding: 18px 20px;
    border-radius: 18px;
    background: {box_bg};
    backdrop-filter: blur(15px);
    border: 1px solid {border_color};
    box-shadow: 0 8px 20px {shadow_color};
    text-align: center;
}}

.subtitle-text {{
    font-size: 22px;
    font-weight: 700;
    color: {text_color};
}}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(
    '<div class="title">📸 Face Recognition Attendance</div>',
    unsafe_allow_html=True
)

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

# =========================
# LOAD KNOWN FACES ONCE
# =========================
@st.cache_resource
def load_known_faces():
    deb_image = face_recognition.load_image_file("Debalina Jana.jpeg")
    deb_encoding = face_recognition.face_encodings(deb_image)[0]

    ayu_image = face_recognition.load_image_file("Ayushi Choudhary.jpeg")
    ayu_encoding = face_recognition.face_encodings(ayu_image)[0]

    shreya_image = face_recognition.load_image_file("Shreya Shree.jpeg")
    shreya_encoding = face_recognition.face_encodings(shreya_image)[0]

    return [deb_encoding, ayu_encoding, shreya_encoding], ["Debalina", "Ayushi", "Shreya"]


try:
    known_encodings, known_names = load_known_faces()

except Exception as e:
    st.error(f"Known face image loading error: {e}")
    st.stop()

# =========================
# CAMERA INPUT
# =========================
uploaded_file = st.camera_input(" ")

if uploaded_file is not None:
    try:
        import numpy as np

        image = face_recognition.load_image_file(uploaded_file)
        test_encodings = face_recognition.face_encodings(image)

        if len(test_encodings) == 0:
            st.error("❌ No face detected")
        else:
            test_encoding = test_encodings[0]

            matches = face_recognition.compare_faces(
                known_encodings,
                test_encoding,
                tolerance=0.45
            )

            face_distances = face_recognition.face_distance(
                known_encodings,
                test_encoding
            )

            best_match_index = np.argmin(face_distances)

 

            if matches[best_match_index]:
                st.success(
                    f"✅ Attendance Marked | {known_names[best_match_index]}"
                )
            else:
                st.error("❌ Face Not Matched")

    except Exception as e:
        st.error(f"Face recognition error: {e}")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Built with Python • Streamlit • Face Recognition")