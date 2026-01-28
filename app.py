import streamlit as st
import cv2
from app_components.engine import LivenessEngine, face_mesh, hands



result_box = st.empty()

# SESSION STATE 
if "camera_on" not in st.session_state:
    st.session_state.camera_on = False

if "result" not in st.session_state:
    st.session_state.result = None

# PAGE CONFIG 
st.set_page_config(
    page_title="Liveness Verification",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}
.title {
    font-size: 38px;
    font-weight: 700;
    color: #ffff;
}
.subtitle {
    font-size: 16px;
    color: #6b7280;
    margin-bottom: 25px;
    margin-left:59px;
}
.card {
    background: white;
    padding: 15px;
    border-radius: 18px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
   
}
            
.card1 {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
    text-align:center;
   
}
.task {
    font-size: 18px;
    font-weight: 600;
    color: #2563eb;
    padding-left:10px;
    
    
    
}
.metric {
    background-color:#F9F6EE;
    font-size: 16px;
    margin-top: 10px;
    color:black;
    padding:15px;
    border-radius:20px;
}
.big-btn button {
    font-size: 18px;
    padding: 14px;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="title">🔐 Liveness Verification</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Secure, challenge-based real person verification</div>',
    unsafe_allow_html=True
)


# start verification Button
if not st.session_state.camera_on:
    col1, col2, col3 = st.columns([0.2, 2.0, 3.7])  
    with col2:
        if st.button("🔐 Start Verification"):
            st.session_state.camera_on = True
            st.session_state.result = None

            # 🔥 CLEAR OLD RESULT UI
            result_box.empty()

            st.rerun()



# Result Real or Spoof
if not st.session_state.camera_on:
    if st.session_state.result == "REAL":
        result_box.markdown("""
<div class="card1" style="border-left:8px solid #10b981;">
<h1 style="color:#065f46;">🎉 Verification Successful</h1>
<p style="font-size:20px;">
You are confirmed as a <b>REAL PERSON</b> ✅
</p>
<p style="color:#047857;">
Thank you for completing the liveness challenges.
</p>
</div>
""", unsafe_allow_html=True)

    elif st.session_state.result == "SPOOF":
        result_box.markdown("""
<div class="card1" style="border-left:8px solid #ef4444;">
<h1 style="color:#7f1d1d;">🚫 Verification Failed</h1>
<p style="font-size:20px;">
<b>Spoof attempt detected</b> ❌
</p>
<p style="color:#991b1b;">
Please try again with a real person.
</p>
</div>
""", unsafe_allow_html=True)



# CAMERA + VERIFICATION 
if st.session_state.camera_on:
    left_col, right_col = st.columns([2.2, 1])

    frame_box = left_col.empty()
    status_box = right_col.empty()

    engine = LivenessEngine()
    cap = cv2.VideoCapture(0)

    while st.session_state.camera_on:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_res = face_mesh.process(rgb)
        hand_res = hands.process(rgb)

        result = engine.update(face_res, hand_res)

        # DECISION 
        if result in ["REAL", "SPOOF"]:
            st.session_state.camera_on = False
            st.session_state.result = result
            cap.release()
            st.rerun()


        # STATUS PANEL
        status_box.markdown(
f"""
<div class="card">
<h3 style="color:black;">📋 Current Task</h3>
<div class="task">{engine.task}</div>

<div class="metric">✅ Success: <b>{engine.success}/3</b></div>
<div class="metric">❌ Mistakes: <b>{engine.mistakes}/3</b></div>
<div class="metric">⏱ Time Left: <b>{result} sec</b></div>

<p style="font-size:14px;color:#6b7280;margin-top:10px;">
Follow the instruction carefully.
</p>
</div>
""",
unsafe_allow_html=True
)


        frame_box.image(frame, channels="BGR")

# FOOTER 
st.markdown(
    '<div style="text-align:center; color:#9ca3af; margin-top:40px;">'
    'Secure Liveness Verification System</div>',
    unsafe_allow_html=True
)
