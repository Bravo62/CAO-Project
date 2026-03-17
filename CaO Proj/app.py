import streamlit as st
import pandas as pd

from analyzer.instruction_parser import parse_trace
from analyzer.cycle_model import compute_ideal_cycles
from analyzer.hazard_detector import detect_hazards
from analyzer.bottleneck_detector import detect_bottleneck

from visualizations.charts import instruction_mix_chart, cycle_loss_chart
from visualizations.metrics import compute_efficiency


st.set_page_config(page_title="CPU Bottleneck Analyzer", layout="wide")

st.title("CPU Bottleneck Analyzer")
st.write("Instruction-Level Performance Diagnosis Tool")

uploaded_file = st.file_uploader("Upload Instruction Trace", type=["txt"])

if uploaded_file:

    with open("temp_trace.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())

    df = parse_trace("temp_trace.txt")

    st.subheader("Instruction Trace")
    st.dataframe(df)

    # Instruction mix
    st.subheader("Instruction Mix")
    fig = instruction_mix_chart(df)
    st.plotly_chart(fig)

    # Ideal cycles
    ideal_cycles = compute_ideal_cycles(df)

    # Hazards
    penalties = detect_hazards(df)

    # Efficiency
    actual_cycles, efficiency = compute_efficiency(ideal_cycles, penalties)

    # Bottleneck detection
    bottleneck, scores = detect_bottleneck(penalties, df)

    st.subheader("Cycle Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Ideal Cycles", ideal_cycles)
    col2.metric("Actual Cycles", actual_cycles)
    col3.metric("CPU Efficiency", f"{efficiency:.2f}%")

    st.subheader("Cycle Loss Breakdown")
    fig2 = cycle_loss_chart(penalties)
    st.plotly_chart(fig2)

    st.subheader("Primary Bottleneck")

    st.success(f"Main Performance Bottleneck: {bottleneck}")

else:
    st.info("Upload an instruction trace file to begin analysis.")