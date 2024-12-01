import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import io

# Streamlit page configuration
st.set_page_config(
    page_title="Graph Generator",
    page_icon="📊",
    layout="wide",
)

# Header
st.title("📊 Best Graph Generator")
st.markdown("### Create and copy a customizable graph for your presentations or reports.")

# Upload data
st.markdown("### Upload your dataset")
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])

if uploaded_file:
    # Load data
    data = pd.read_csv(uploaded_file)
    st.markdown("### Dataset Preview")
    st.dataframe(data)

    # User input for graph options
    st.markdown("### Graph Options")
    graph_type = st.selectbox("Select Graph Type:", ["Line Plot", "Bar Plot", "Scatter Plot", "Pie Chart"])
    x_column = st.selectbox("Select X-axis Column:", data.columns)
    y_column = None
    if graph_type != "Pie Chart":
        y_column = st.selectbox("Select Y-axis Column:", data.columns)

    title = st.text_input("Graph Title:", "My Graph")
    xlabel = st.text_input("X-axis Label:", x_column)
    ylabel = st.text_input("Y-axis Label:", y_column if y_column else "")

    # Generate and display the graph
    st.markdown("### Generated Graph")
    fig, ax = plt.subplots(figsize=(10, 6))

    if graph_type == "Line Plot":
        ax.plot(data[x_column], data[y_column], marker="o", linestyle="-")
    elif graph_type == "Bar Plot":
        ax.bar(data[x_column], data[y_column])
    elif graph_type == "Scatter Plot":
        ax.scatter(data[x_column], data[y_column])
    elif graph_type == "Pie Chart":
        ax.pie(data[x_column], labels=data[x_column], autopct="%1.1f%%")
    
    ax.set_title(title, fontsize=16)
    if graph_type != "Pie Chart":
        ax.set_xlabel(xlabel, fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12)
    
    st.pyplot(fig)

    # Download graph
    st.markdown("### Download Graph as Image")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    st.download_button(
        label="Download Graph as PNG",
        data=buf,
        file_name="graph.png",
        mime="image/png",
    )
