import streamlit as st
import pandas as pd
from inference import predict_emotions

# App Title Layout
st.set_page_config(page_title="Emotion Detection Engine", layout="wide")
st.title("🧠 Emotion Detection & Learning Support Engine")
st.subheader("Transforming student challenges into empathetic guidance solutions.")

st.markdown("---")

# Create Left and Right Split Columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📥 Input Student Challenge")
    student_input = st.text_area(
        "Paste the text or student message below:",
        placeholder="Type something here (e.g., 'I have been stuck on this recursion loop for hours and nothing makes sense...')"
    )

    analyze_btn = st.button("Analyze & Generate Support", type="primary")

with col2:
    st.markdown("### 📊 Real-Time Emotion Breakdown")
    if analyze_btn and student_input:
        # Call the inference logic function
        predictions = predict_emotions(student_input)

        # Convert dictionary to DataFrame for table presentation
        df = pd.DataFrame(list(predictions.items()), columns=["Emotion", "Confidence Score"])
        df = df.sort_values(by="Confidence Score", ascending=False)

        # Display as a clean status bar chart
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.bar_chart(data=df, x="Emotion", y="Confidence Score")

        # Rule Based Empathy Response Placeholder
        top_emotion = df.iloc[0]["Emotion"]
        st.success(f"**Detected Primary State:** {top_emotion}")
    else:
        st.info("Enter student text on the left panel and click 'Analyze' to view data insights.")