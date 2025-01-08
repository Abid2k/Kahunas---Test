import random
import numpy as np
import pandas as pd

# Step 1: Simulate health data for 100 users with realistic distributions
def simulate_health_data(num_users=100):
    data = []
    for user_id in range(1, num_users + 1):
        # Simulate daily steps (normal distribution, clipped to valid range)
        daily_steps = int(np.clip(np.random.normal(6000, 2000), 0, 20000))
        
        # Simulate heart rate (normal distribution, clipped to valid range)
        heart_rate = int(np.clip(np.random.normal(72, 10), 40, 100))
        
        # Simulate sleep quality (normal distribution, clipped to range 1–10)
        sleep_quality = int(np.clip(np.random.normal(7, 1.5), 1, 10))
        
        data.append({
            "User_ID": user_id,
            "Daily_Steps": daily_steps,
            "Heart_Rate": heart_rate,
            "Sleep_Quality": sleep_quality
        })
    return pd.DataFrame(data)

# Step 2: Analyze trends and correlations
def analyze_data(df):
    # Calculate average performance metrics grouped by sleep quality
    avg_steps_by_sleep = df.groupby("Sleep_Quality")["Daily_Steps"].mean()
    avg_heart_rate_by_sleep = df.groupby("Sleep_Quality")["Heart_Rate"].mean()
    
    # Correlation between sleep quality and performance metrics
    correlation_steps_sleep = df["Daily_Steps"].corr(df["Sleep_Quality"])
    correlation_hr_sleep = df["Heart_Rate"].corr(df["Sleep_Quality"])
    print(f"Correlation Steps-Sleep: {correlation_steps_sleep}")
    print(f"Correlation HR-Sleep: {correlation_hr_sleep}")  
    
    analysis = {
        "Average_Steps_By_Sleep": avg_steps_by_sleep.to_dict(),
        "Average_Heart_Rate_By_Sleep": avg_heart_rate_by_sleep.to_dict(),
        "Correlation_Steps_Sleep": correlation_steps_sleep,
        "Correlation_HR_Sleep": correlation_hr_sleep
    }
    return analysis

# Step 3: Generate actionable insights
def generate_insights(df):
    insights = []
    for _, row in df.iterrows():
        user_id = row["User_ID"]
        sleep_quality = row["Sleep_Quality"]
        daily_steps = row["Daily_Steps"]
        heart_rate = row["Heart_Rate"]

        advice = []
        if sleep_quality < 5:
            advice.append("Consider improving sleep habits for better performance.")
        if daily_steps < 5000:
            advice.append("Try increasing daily steps to at least 7,000 for better health.")
        if heart_rate > 90:
            advice.append("Maintain a balanced routine to lower resting heart rate.")

        insights.append({
            "User_ID": user_id,
            "Sleep_Quality": sleep_quality,
            "Daily_Steps": daily_steps,
            "Heart_Rate": heart_rate,
            "Advice": advice
        })
    return insights

# Step 4: Main function to tie everything together
def main():
    # Generate health data
    health_data = simulate_health_data()

    # Analyze data
    analysis = analyze_data(health_data)

    # Generate insights
    insights = generate_insights(health_data)

    # Display results
    print("\n--- Data Analysis Results ---")
    print(f"Correlation between Sleep Quality and Daily Steps: {analysis['Correlation_Steps_Sleep']:.2f}")
    print(f"Correlation between Sleep Quality and Heart Rate: {analysis['Correlation_HR_Sleep']:.2f}")
    print("\n--- Sample Insights ---")
    for insight in insights[:5]:  # Display insights for first 5 users
        print(f"User {insight['User_ID']}:")
        print(f"  Sleep Quality: {insight['Sleep_Quality']}")
        print(f"  Daily Steps: {insight['Daily_Steps']}")
        print(f"  Heart Rate: {insight['Heart_Rate']}")
        print(f"  Advice: {' '.join(insight['Advice'])}")
        print()

# Run the script
if __name__ == "__main__":
    main()

