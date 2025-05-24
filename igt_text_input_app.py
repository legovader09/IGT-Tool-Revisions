
import streamlit as st
import pandas as pd

# Function to calculate net score
def calculate_net_score(decisions):
    freq_1_2 = decisions.count(1) + decisions.count(2)
    freq_3_4 = decisions.count(3) + decisions.count(4)
    return freq_3_4 - freq_1_2

# Function to calculate Z-score
def calculate_z_score(net_score, mean, std_dev):
    return (net_score - mean) / std_dev

# Function to classify Z-score
def classify_z_score(z_score):
    if z_score >= 3.33:
        return "Exceptionally High Score"
    elif z_score >= 3.27:
        return "Exceptionally High Score"
    elif z_score >= 3.2:
        return "Exceptionally High Score"
    elif z_score >= 3.13:
        return "Exceptionally High Score"
    elif z_score >= 3.07:
        return "Exceptionally High Score"
    elif z_score >= 3:
        return "Exceptionally High Score"
    elif z_score >= 2.93:
        return "Exceptionally High Score"
    elif z_score >= 2.87:
        return "Exceptionally High Score"
    elif z_score >= 2.8:
        return "Exceptionally High Score"
    elif z_score >= 2.73:
        return "Exceptionally High Score"
    elif z_score >= 2.67:
        return "Exceptionally High Score"
    elif z_score >= 2.6:
        return "Exceptionally High Score"
    elif z_score >= 2.53:
        return "Exceptionally High Score"
    elif z_score >= 2.47:
        return "Exceptionally High Score"
    elif z_score >= 2.4:
        return "Exceptionally High Score"
    elif z_score >= 2.33:
        return "Exceptionally High Score"
    elif z_score >= 2.27:
        return "Exceptionally High Score"
    elif z_score >= 2.2:
        return "Exceptionally High Score"
    elif z_score >= 2.13:
        return "Exceptionally High Score"
    elif z_score >= 2.07:
        return "Exceptionally High Score"
    elif z_score >= 2:
        return "Exceptionally High Score"
    elif z_score >= 1.93:
        return "Above Average Score"
    elif z_score >= 1.87:
        return "Above Average Score"
    elif z_score >= 1.8:
        return "Above Average Score"
    elif z_score >= 1.73:
        return "Above Average Score"
    elif z_score >= 1.67:
        return "Above Average Score"
    elif z_score >= 1.6:
        return "Above Average Score"
    elif z_score >= 1.53:
        return "Above Average Score"
    elif z_score >= 1.47:
        return "Above Average Score"
    elif z_score >= 1.4:
        return "Above Average Score"
    elif z_score >= 1.33:
        return "Above Average Score"
    elif z_score >= 1.27:
        return "High Average Score"
    elif z_score >= 1.2:
        return "High Average Score"
    elif z_score >= 1.13:
        return "High Average Score"
    elif z_score >= 1.07:
        return "High Average Score"
    elif z_score >= 1:
        return "High Average Score"
    elif z_score >= 0.93:
        return "High Average Score"
    elif z_score >= 0.87:
        return "High Average Score"
    elif z_score >= 0.8:
        return "High Average Score"
    elif z_score >= 0.73:
        return "High Average Score"
    elif z_score >= 0.67:
        return "High Average Score"
    elif z_score >= 0.6:
        return "Average Score"
    elif z_score >= 0.53:
        return "Average Score"
    elif z_score >= 0.47:
        return "Average Score"
    elif z_score >= 0.4:
        return "Average Score"
    elif z_score >= 0.33:
        return "Average Score"
    elif z_score >= 0.27:
        return "Average Score"
    elif z_score >= 0.2:
        return "Average Score"
    elif z_score >= 0.13:
        return "Average Score"
    elif z_score >= 0.07:
        return "Average Score"
    elif z_score >= 0:
        return "Average Score"
    elif z_score >= -0.07:
        return "Average Score"
    elif z_score >= -0.13:
        return "Average Score"
    elif z_score >= -0.2:
        return "Average Score"
    elif z_score >= -0.27:
        return "Average Score"
    elif z_score >= -0.33:
        return "Average Score"
    elif z_score >= -0.4:
        return "Average Score"
    elif z_score >= -0.47:
        return "Average Score"
    elif z_score >= -0.53:
        return "Average Score"
    elif z_score >= -0.6:
        return "Average Score"
    elif z_score >= -0.67:
        return "Average Score"
    elif z_score >= -0.73:
        return "Low Average Score"
    elif z_score >= -0.8:
        return "Low Average Score"
    elif z_score >= -0.87:
        return "Low Average Score"
    elif z_score >= -0.93:
        return "Low Average Score"
    elif z_score >= -1:
        return "Low Average Score"
    elif z_score >= -1.07:
        return "Low Average Score"
    elif z_score >= -1.13:
        return "Low Average Score"
    elif z_score >= -1.2:
        return "Low Average Score"
    elif z_score >= -1.27:
        return "Low Average Score"
    elif z_score >= -1.33:
        return "Low Average Score"
    elif z_score >= -1.4:
        return "Below Average Score"
    elif z_score >= -1.47:
        return "Below Average Score"
    elif z_score >= -1.53:
        return "Below Average Score"
    elif z_score >= -1.6:
        return "Below Average Score"
    elif z_score >= -1.67:
        return "Below Average Score"
    elif z_score >= -1.73:
        return "Below Average Score"
    elif z_score >= -1.8:
        return "Below Average Score"
    elif z_score >= -1.87:
        return "Below Average Score"
    elif z_score >= -1.93:
        return "Below Average Score"
    elif z_score >= -2:
        return "Below Average Score"
    elif z_score >= -2.07:
        return "Exceptionally Low Score"
    elif z_score >= -2.13:
        return "Exceptionally Low Score"
    elif z_score >= -2.2:
        return "Exceptionally Low Score"
    elif z_score >= -2.27:
        return "Exceptionally Low Score"
    elif z_score >= -2.33:
        return "Exceptionally Low Score"
    elif z_score >= -2.4:
        return "Exceptionally Low Score"
    elif z_score >= -2.47:
        return "Exceptionally Low Score"
    elif z_score >= -2.53:
        return "Exceptionally Low Score"
    elif z_score >= -2.6:
        return "Exceptionally Low Score"
    elif z_score >= -2.67:
        return "Exceptionally Low Score"
    elif z_score >= -2.73:
        return "Exceptionally Low Score"
    elif z_score >= -2.8:
        return "Exceptionally Low Score"
    elif z_score >= -2.87:
        return "Exceptionally Low Score"
    elif z_score >= -2.93:
        return "Exceptionally Low Score"
    elif z_score >= -3:
        return "Exceptionally Low Score"
    elif z_score >= -3.07:
        return "Exceptionally Low Score"
    elif z_score >= -3.13:
        return "Exceptionally Low Score"
    elif z_score >= -3.2:
        return "Exceptionally Low Score"
    else:
        return "Score Out of Range"

# Streamlit app
st.title("IGT Net Score Analyzer")

st.write("Paste your raw IGT data (tab-separated) below:")

# Text area for raw data input
raw_data = st.text_area("Raw Data", height=300)

if st.button("Analyze"):
    if raw_data:
        # Parse the raw data
        data = [line.split("\t") for line in raw_data.strip().split("\n")]
        df = pd.DataFrame(data, columns=["RT", "Decision", "Fee", "Before", "After", "Reward", "Penalty"])

        # Convert Decision column to integers
        df["Decision"] = df["Decision"].astype(int)

        # Calculate net score
        net_score = calculate_net_score(df["Decision"].tolist())

        # Norms
        norms = {
            "IGT1": {"mean": 15.31, "std_dev": 17.44},
            "IGT2 Male": {"mean": 20.26, "std_dev": 15.67},
            "IGT2 Female": {"mean": 10.35, "std_dev": 17.87}
        }

        # Calculate Z-scores and descriptors
        results = []
        for group, norm in norms.items():
            z_score = calculate_z_score(net_score, norm["mean"], norm["std_dev"])
            descriptor = classify_z_score(z_score)
            results.append({"Group": group, "Net Score": net_score, "Z-Score": z_score, "Descriptor": descriptor})

        results_df = pd.DataFrame(results)

        # Display results
        st.write("### Results")
        st.dataframe(results_df)
    else:
        st.error("Please paste your raw data.")
