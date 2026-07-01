import streamlit as st
import joblib
import pandas as pd
import time


def show_dashboard():

    # -------------------------
    # Home Button
    # -------------------------

    if st.button("🏠 Home"):
        st.session_state.page = "home"
        st.rerun()

    # -------------------------
    # Load Model
    # -------------------------

    model = joblib.load("models/network_model.pkl")
    protocol_encoder = joblib.load("models/protocol_encoder.pkl")
    service_encoder = joblib.load("models/service_encoder.pkl")
    flag_encoder = joblib.load("models/flag_encoder.pkl")

    # -------------------------
    # Header
    # -------------------------

    st.title("🛡️ AI Network Intrusion Detection System")
    st.caption("Random Forest • NSL-KDD Dataset • Streamlit Dashboard")

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Model Accuracy", "79.61%")

    with c2:
        st.metric("Algorithm", "Random Forest")

    with c3:
        st.metric("System Status", "🟢 Ready")

    st.divider()

    # -------------------------
    # Input Form
    # -------------------------

    st.subheader("📥 Enter Network Traffic Details")

    left, right = st.columns(2)

    with left:

        duration = st.number_input(
            "Duration",
            min_value=0,
            value=0
        )

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

    with right:

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
    # Analyze Button
    # -------------------------

    if st.button("🔍 Analyze Traffic"):

        # Encode categorical values
        protocol_value = protocol_encoder.transform([protocol])[0]
        service_value = service_encoder.transform([service])[0]
        flag_value = flag_encoder.transform([flag])[0]

        # Create dataframe
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

        # -------------------------
        # Loading Animation
        # -------------------------

        status = st.empty()
        progress = st.progress(0)

        steps = [
            "📡 Collecting network traffic...",
            "⚙️ Encoding network features...",
            "🤖 Running Random Forest model...",
            "🛡️ Calculating threat score..."
        ]

        current_progress = 0

        for step in steps:

            status.info(step)

            for _ in range(25):

                current_progress += 1

                progress.progress(current_progress)

                time.sleep(0.02)

        status.success("✅ Analysis Complete!")

        time.sleep(0.5)

        status.empty()
        progress.empty()

        # -------------------------
        # Prediction
        # -------------------------

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        confidence = max(probabilities) * 100

        st.divider()

        st.subheader("📊 Prediction Result")
            # -------------------------
        # Display Results
        # -------------------------

        if prediction == 0:

            st.success("🟢 Normal Traffic Detected")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

            with col2:
                st.metric(
                    "Risk Level",
                    "🟢 LOW"
                )

            st.info("""
### Recommendation

✅ No suspicious activity detected.

- Continue monitoring the network.
- No immediate action required.
- Traffic appears to be legitimate.
""")

        else:

            st.error("🔴 Attack Detected!")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

            with col2:
                st.metric(
                    "Risk Level",
                    "🔴 HIGH"
                )

            st.warning("""
### Recommendation

⚠️ Suspicious traffic detected.

- Investigate this connection.
- Review firewall logs.
- Verify the source IP.
- Block the connection if necessary.
""")

        st.divider()

        st.subheader("📄 Traffic Summary")

        summary = pd.DataFrame({
            "Feature": [
                "Duration",
                "Protocol",
                "Service",
                "Flag",
                "Source Bytes",
                "Destination Bytes",
                "Count",
                "Server Count",
                "Logged In",
                "Serror Rate"
            ],
            "Value": [
                duration,
                protocol,
                service,
                flag,
                src_bytes,
                dst_bytes,
                count,
                srv_count,
                logged_in,
                serror_rate
            ]
        })

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )