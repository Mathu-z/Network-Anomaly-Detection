import streamlit as st
import streamlit.components.v1 as components

def show_home():
    components.html(
    """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    overflow:hidden;
    background:black;
}

canvas{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
}

</style>

</head>

<body>

<canvas id="matrix"></canvas>

<script>

const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const chars =
"01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@";

const fontSize = 16;

const columns = canvas.width / fontSize;

const drops = [];

for(let i=0;i<columns;i++){

    drops[i]=1;

}

function draw(){

    ctx.fillStyle="rgba(0,0,0,0.05)";
    ctx.fillRect(0,0,canvas.width,canvas.height);

    ctx.fillStyle="#00ff41";
    ctx.font=fontSize+"px monospace";

    for(let i=0;i<drops.length;i++){

        const text =
        chars.charAt(
            Math.floor(
                Math.random()*chars.length
            )
        );

        ctx.fillText(
            text,
            i*fontSize,
            drops[i]*fontSize
        );

        if(
            drops[i]*fontSize>canvas.height &&
            Math.random()>0.975
        ){

            drops[i]=0;

        }

        drops[i]++;

    }

}

setInterval(draw,35);

</script>

</body>

</html>
""",
height=0,
)

    st.markdown("""
    <style>

    .main > div{
        padding-top:40px;
    }

    .title{
        text-align:center;
        font-size:68px;
        font-weight:800;
        color:white;
        line-height:1.1;
    }

    .shield{
        text-align:center;
        font-size:85px;
    }

    .subtitle{
        text-align:center;
        font-size:24px;
        color:#b8c0cc;
    }

    .cards{
        display:flex;
        justify-content:center;
        gap:20px;
        margin-top:50px;
        margin-bottom:40px;
    }

    .card{
        background:#1d2433;
        border-radius:15px;
        padding:20px;
        width:180px;
        text-align:center;
        border:1px solid #2f3748;
    }

    .number{
        font-size:32px;
        font-weight:bold;
        color:#00d4ff;
    }

    .label{
        color:#c9d1d9;
        font-size:16px;
    }

    div.stButton > button{
        width:350px;
        height:65px;
        font-size:24px;
        font-weight:bold;
        border-radius:15px;
        background:linear-gradient(90deg,#00c6ff,#0072ff);
        color:white;
        border:none;
        transition:0.3s;
        display:block;
        margin:auto;
    }

    div.stButton > button:hover{
        transform:scale(1.05);
        box-shadow:0px 0px 20px #00c6ff;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="shield">🛡️</div>

        <div class="title">
        AI NETWORK <br>
        INTRUSION DETECTION <br>
        SYSTEM
        </div>

        <br>

        <div class="subtitle">
        Machine Learning Powered Security Dashboard
        </div>

        <div class="subtitle">
        Random Forest • NSL-KDD Dataset
        </div>

        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🎯 Accuracy", "79.61%")

    with col2:
        st.metric("🤖 Model", "Random Forest")

    with col3:
        st.metric("📦 Dataset", "NSL-KDD")

    with col4:
        st.metric("🛡 Status", "Ready")

    st.write("")
    st.write("")

    if st.button("🚀 ENTER SECURITY CONSOLE", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()

    st.write("")
    st.write("")

    st.info("""
### About

This project uses a **Random Forest Machine Learning model**
trained on the **NSL-KDD dataset** to detect malicious network
traffic and classify it as **Normal** or **Attack**.

Developed using **Python**, **Scikit-Learn**, and **Streamlit**.
""")