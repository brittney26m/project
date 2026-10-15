import os
import streamlit as st
import requests

st.set_page_config(page_title="Market Intelligence & Retention Copilot", layout="wide")

st.title("🛡️ Market Intelligence & Customer Retention Copilot")
st.caption("Enterprise Risk Monitoring & AI-Driven Churn Mitigation Platform")

st.sidebar.header("Customer Overview")
customer = st.sidebar.selectbox("Select Account", ["TechCorp Inc.", "CloudScale Systems", "DataFlow Ltd."])
st.sidebar.metric("CSM Assigned", "Jordan Patel")
st.sidebar.metric("Contract Tier", "Enterprise")
st.sidebar.metric("ARR", "$86,000")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Internal Telemetry (Risk Signals)")
    st.warning("⚠️ High Risk Detected")
    st.write("- **Active Users**: Down 65% in 30 days")
    st.write("- **Last Login**: 18 days ago")
    st.write("- **Feature Adoption**: Dropped 40%")

with col2:
    st.subheader("⚔️ Market Intelligence (Competitor Watch)")
    st.error("🚨 Active Competitor Threat")
    st.write("- **CloudX**: Offering 20% migration discount for mid-market accounts.")
    st.write("- **Feature Launch**: CloudX launched automated SOC2 compliance suite.")

st.markdown("---")

if st.button("🚀 Run AI Dual-Engine Analysis", type="primary"):
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key.strip()
    }
    
    with st.spinner("Analyzing risk signals & generating retention strategy..."):
        try:
            # 直接使用官方推荐的最新模型 gemini-3.8-flash
            url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"
            prompt_text = f"""
            Account: {customer}
            Internal Logs: 65% usage drop, 18 days inactive.
            External News: Competitor CloudX offering 20% discount.
            
            Provide a 3-bullet point executive churn risk analysis and draft a quick emergency retention email for the CSM.
            """
            
            payload = {
                "contents": [{
                    "parts": [{"text": prompt_text}]
                }]
            }
            
            response = requests.post(url, json=payload, headers=headers)
            res_data = response.json()
            
            if response.status_code == 200:
                ai_output = res_data['candidates'][0]['content']['parts'][0]['text']
                st.success("Analysis Complete! (Powered by gemini-2.5-flash)")
                st.markdown("### 🤖 AI Dual-Engine Strategy Report")
                st.write(ai_output)
            else:
                st.error(f"调用 Gemini 失败 ({response.status_code}): {res_data}")
                
        except Exception as e:
            st.error(f"执行异常: {e}")
