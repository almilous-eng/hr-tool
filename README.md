# 🧑‍💼 HR Analytics Dashboard

An interactive HR analytics dashboard built with **Streamlit**, **Plotly**, and **Pandas** to explore workforce characteristics, employee metrics, and synthetic compensation data.

The application demonstrates how HR data can be transformed into actionable insights through interactive visualizations and business intelligence techniques.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hr-tool-p2h3tknotccksp9qdh8ald.streamlit.app/)

---

## 🚀 Features

### 📊 Executive Dashboard

* Employee headcount KPIs
* Average salary and workload metrics
* Average tenure analysis
* Department overview
* Salary distribution visualization

### 👥 Workforce Analysis

* Age distribution analysis
* Residence breakdown
* Workload distribution by department
* Correlation heatmap of HR metrics

### 💰 Compensation & Seniority

* Synthetic salary generation based on seniority
* Salary distribution by seniority level
* Workload vs salary relationships
* Compensation analytics

### 🔎 Employee Explorer

* Employee search functionality
* Individual employee profiles
* Tenure and vacation metrics
* HR risk flagging system

### 📈 Deep HR Insights

Advanced visualizations including:

* Box plots of age by residence
* Distribution histograms
* Vacation usage analytics
* Stacked workload charts
* Department vs seniority heatmaps
* Workload and vacation composition analyses

---

## 🧠 Synthetic Features

Since the original dataset does not contain compensation information, the application generates realistic synthetic metrics:

* **Annual net salary (€)** based on seniority level
* **Tenure (years)** computed from hire date
* **Vacation usage ratio**
* **Overworked employee flag**
* **At-risk employee heuristic**

These synthetic features are intended solely for demonstration and portfolio purposes.

---

## 📂 Project Structure

```text
hr-tool/
│
├── app.py
├── data/
│   └── hr_dataset_nrw.csv
│
├── requirements.txt
└── README.md
```

---

## 🗂 Dataset

The dataset contains mocked HR data for employees residing in **North Rhine-Westphalia (NRW), Germany**.

Available columns:

* First name
* Name
* Residence
* Age
* Department
* Seniority Level
* Workload (%)
* Vacation days total
* Vacation days taken
* Hire date

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/hr-tool.git
cd hr-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The application is designed for deployment on **Streamlit Community Cloud**.

1. Push the repository to GitHub.
2. Connect the repository to Streamlit Cloud.
3. Select `app.py` as the entry point.
4. Deploy.

---

## 📸 Dashboard Preview

*Add screenshots or GIFs of the dashboard here.*

Examples:

* Overview page
* Workforce analysis page
* Employee explorer
* Deep HR insights dashboard

---

## 🎯 Learning Objectives

This project demonstrates:

* Interactive dashboard development
* HR analytics and workforce insights
* Feature engineering
* Synthetic data generation
* Business intelligence visualization
* Cloud deployment with Streamlit

---

## ⚠️ Disclaimer

This project uses **synthetic and mocked HR data** for educational and portfolio purposes only. No real employee information is included.

---

## 👤 Author

**Alexandros Milousis**

Feel free to connect or provide feedback regarding the project.
