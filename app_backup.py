import streamlit as st
import joblib
import pandas as pd
import time
# -------------------------
# Load the trained model
# -------------------------
model = joblib.load("models/network_model.pkl")
protocol_encoder = joblib.load("models/protocol_encoder.pkl")
service_encoder = joblib.load("models/service_encoder.pkl")
flag_encoder = joblib.load("models/flag_encoder.pkl")

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Network Anomaly Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Network Intrusion Detection System")
st.caption("Random Forest • NSL-KDD Dataset • Streamlit Dashboard")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Model Accuracy",
        value="79.61%"
    )

with col2:
    st.metric(
        label="Algorithm",
        value="Random Forest"
    )

with col3:
    st.metric(
        label="System Status",
        value="🟢 Ready"
    )

st.divider()
# -------------------------
# Input Section
# -------------------------
st.subheader("📥 Enter Network Traffic Details")
col1, col2 = st.columns(2)

with col1:
    duration = st.number_input("Duration", min_value=0, value=0)

    protocol = st.selectbox(
        "Protocol",
        protocol_encoder.classes_
    )

    service = st.selectbox(
        "Service",
        service_encoder.classes_
    )

    flag = st.selectbox(
        "Flag",
        flag_encoder.classes_
    )

    src_bytes = st.number_input(
        "Source Bytes",
        min_value=0,
        value=0
    )

with col2:
    dst_bytes = st.number_input(
        "Destination Bytes",
        min_value=0,
        value=0
    )

    count = st.number_input(
        "Count",
        min_value=0,
        value=0
    )

    srv_count = st.number_input(
        "Server Count",
        min_value=0,
        value=0
    )

    logged_in = st.selectbox(
        "Logged In",
        [0, 1]
    )

    serror_rate = st.slider(
        "Serror Rate",
        0.0,
        1.0,
        0.0
    )
# -------------------------
# Prediction
# -------------------------



    # Encode categorical inputs
    protocol_value = protocol_encoder.transform([protocol])[0]
    service_value = service_encoder.transform([service])[0]
    flag_value = flag_encoder.transform([flag])[0]

    # Create input dataframe
    input_data = pd.DataFrame([{
        "duration": duration,
        "protocol_type": protocol_value,
        "service": service_value,
        "flag": flag_value,
        "src_bytes": src_bytes,
        "dst_bytes": dst_bytes,
        "count": count,
        "srv_count": srv_count,
        "logged_in": logged_in,
        "serror_rate": serror_rate
    }])

# Make prediction
# -------------------------
# Prediction
# -------------------------

if st.button("🔍 Analyze Traffic"):

    # Encode categorical inputs
    protocol_value = protocol_encoder.transform([protocol])[0]
    service_value = service_encoder.transform([service])[0]
    flag_value = flag_encoder.transform([flag])[0]

    # Create input dataframe
    input_data = pd.DataFrame([{
        "duration": duration,
        "protocol_type": protocol_value,
        "service": service_value,
        "flag": flag_value,
        "src_bytes": src_bytes,
        "dst_bytes": dst_bytes,
        "count": count,
        "srv_count": srv_count,
        "logged_in": logged_in,
        "serror_rate": serror_rate
    }])

    # Loading animation
    status = st.empty()
    progress = st.progress(0)

    steps = [
        "📡 Collecting network traffic...",
        "⚙️ Encoding network features...",
        "🤖 Running Random Forest model...",
        "🛡️ Calculating threat score..."
    ]

    for step in steps:
        status.info(step)
        for i in range(25):
            progress.progress(min(progress._value + 1 if hasattr(progress, "_value") else i + 1, 100))
            time.sleep(0.02)

    progress.progress(100)
    status.success("✅ Analysis Complete!")
    time.sleep(0.5)

    status.empty()
    progress.empty()

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Confidence
    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities) * 100

    st.divider()
    st.subheader("📊 Prediction Result")

    if prediction == 0:

        st.success("🟢 Normal Traffic")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Confidence", f"{confidence:.2f}%")

        with col2:
            st.metric("Risk Level", "🟢 Low")

        st.info("""
### Recommendation
- No suspicious activity detected.
- Continue monitoring network traffic.
- No immediate action required.
""")

    else:

        st.error("🔴 Attack Detected")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Confidence", f"{confidence:.2f}%")

        with col2:
            st.metric("Risk Level", "🔴 High")

        st.warning("""
### Recommendation
- Investigate this connection immediately.
- Monitor firewall and IDS logs.
- Verify source and destination traffic.
""")