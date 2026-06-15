import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")

# =========================================================
# DATA LOADING (CACHED)
# =========================================================
import os

@st.cache_data
def load_data():
    path = os.path.join("data", "hr_dataset_nrw.csv")
    df = pd.read_csv(path)

    df["Hire date"] = pd.to_datetime(df["Hire date"])
    return df

# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/hr_dataset_nrw.csv")

#     # Parse dates
#     df["Hire date"] = pd.to_datetime(df["Hire date"])

#     return df

df = load_data()

# =========================================================
# FEATURE ENGINEERING
# =========================================================
def generate_salary(row):
    base = {
        "Junior": (28000, 45000),
        "Mid": (45000, 70000),
        "Senior": (70000, 110000),
        "Lead": (90000, 140000),
        "Manager": (90000, 150000),
    }

    low, high = base.get(row["Seniority Level"], (40000, 80000))
    salary = np.random.uniform(low, high)

    # small noise for realism
    salary *= np.random.uniform(0.9, 1.1)

    return round(salary, 2)


# Apply salary
np.random.seed(42)
df["Salary (€)"] = df.apply(generate_salary, axis=1)

# Tenure
df["Tenure (Years)"] = (
    (datetime.today() - df["Hire date"]).dt.days / 365
).round(1)

# Vacation usage
df["Vacation Usage"] = df["Vacation days taken"] / df["Vacation days total"]

# Overworked flag
df["Overworked"] = df["Workload (%)"] > 85

# Risk flag (simple heuristic)
df["At Risk"] = (df["Overworked"]) & (df["Vacation Usage"] < 0.6)

# =========================================================
# SIDEBAR FILTERS
# =========================================================
st.sidebar.title("Filters")

departments = st.sidebar.multiselect(
    "Department",
    sorted(df["Department"].unique()),
    default=sorted(df["Department"].unique())
)

seniority = st.sidebar.multiselect(
    "Seniority Level",
    sorted(df["Seniority Level"].unique()),
    default=sorted(df["Seniority Level"].unique())
)

age_range = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (int(df["Age"].min()), int(df["Age"].max()))
)

workload_range = st.sidebar.slider(
    "Workload (%)",
    int(df["Workload (%)"].min()),
    int(df["Workload (%)"].max()),
    (int(df["Workload (%)"].min()), int(df["Workload (%)"].max()))
)

# Apply filters
df_filtered = df[
    (df["Department"].isin(departments)) &
    (df["Seniority Level"].isin(seniority)) &
    (df["Age"].between(age_range[0], age_range[1])) &
    (df["Workload (%)"].between(workload_range[0], workload_range[1]))
]

# =========================================================
# PAGE NAVIGATION
# =========================================================
page = st.sidebar.selectbox(
    "Navigation",
    ["Overview", "Workforce Analysis", "Compensation & Seniority", "Employee Explorer"]
)

st.title("🧑‍💼 HR Analytics Dashboard")

# =========================================================
# OVERVIEW PAGE
# =========================================================
if page == "Overview":

    st.subheader("Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Employees", len(df_filtered))
    col2.metric("Avg Salary (€)", int(df_filtered["Salary (€)"].mean()))
    col3.metric("Avg Workload (%)", round(df_filtered["Workload (%)"].mean(), 1))
    col4.metric("Avg Tenure (Years)", round(df_filtered["Tenure (Years)"].mean(), 1))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            df_filtered,
            x="Department",
            color="Department",
            title="Employees by Department"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            df_filtered,
            x="Salary (€)",
            nbins=30,
            title="Salary Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# WORKFORCE ANALYSIS
# =========================================================
elif page == "Workforce Analysis":

    st.subheader("Workforce Insights")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            df_filtered,
            x="Age",
            nbins=20,
            title="Age Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(
            df_filtered["Residence"].value_counts().head(10).reset_index(),
            x="index",
            y="Residence",
            title="Top Residences"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    fig = px.box(
        df_filtered,
        x="Department",
        y="Workload (%)",
        title="Workload by Department"
    )
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# COMPENSATION & SENIORITY
# =========================================================
elif page == "Compensation & Seniority":

    st.subheader("Salary & HR Structure")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.box(
            df_filtered,
            x="Seniority Level",
            y="Salary (€)",
            title="Salary by Seniority Level"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(
            df_filtered,
            x="Workload (%)",
            y="Salary (€)",
            color="Seniority Level",
            title="Workload vs Salary"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    fig = px.histogram(
        df_filtered,
        x="Salary (€)",
        nbins=30,
        title="Salary Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# EMPLOYEE EXPLORER
# =========================================================
elif page == "Employee Explorer":

    st.subheader("Employee Search & Profile")

    search = st.text_input("Search employee by name")

    if search:
        result = df_filtered[
            df_filtered["Name"].str.contains(search, case=False, na=False)
            | df_filtered["First name"].str.contains(search, case=False, na=False)
        ]

        st.write(f"Found {len(result)} employees")

        if len(result) > 0:
            selected = st.selectbox(
                "Select Employee",
                result["Name"] + " " + result["First name"]
            )

            emp = result[
                (result["Name"] + " " + result["First name"]) == selected
            ].iloc[0]

            st.divider()

            col1, col2, col3 = st.columns(3)

            col1.metric("Age", emp["Age"])
            col2.metric("Department", emp["Department"])
            col3.metric("Seniority", emp["Seniority Level"])

            col1, col2, col3 = st.columns(3)

            col1.metric("Workload (%)", emp["Workload (%)"])
            col2.metric("Salary (€)", emp["Salary (€)"])
            col3.metric("Tenure (Years)", emp["Tenure (Years)"])

            st.write("Vacation Usage:", round(emp["Vacation Usage"] * 100, 1), "%")

            if emp["At Risk"]:
                st.error("⚠️ Employee is flagged as AT RISK (workload + low vacation usage)")
            elif emp["Overworked"]:
                st.warning("⚠️ Employee is overworked")
            else:
                st.success("Healthy profile")