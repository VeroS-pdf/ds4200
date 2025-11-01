import pandas as pd
df = pd.read_csv("socialMedia.csv")
df['Likes'] = pd.to_numeric(df['Likes'], errors='coerce')

# Clean the data for bar charts

# Calculate average likes by Platform and PostType
avg_likes_df = df.groupby(['Platform', 'PostType'], as_index=False)['Likes'].mean()
avg_likes_df.rename(columns={'Likes': 'AvgLikes'}, inplace=True)

# Save to CSV
avg_likes_df.to_csv("socialMediaAvg.csv", index=False)

# Clean the data for the line plot
df = pd.read_csv("socialMedia.csv")
df['Likes'] = pd.to_numeric(df['Likes'], errors='coerce')

df['Date'] = df['Date'].apply(lambda x: x.split('(')[0].strip() if pd.notnull(x) else x)

avg_likes_date_df = df.groupby('Date', as_index=False)['Likes'].mean()
avg_likes_date_df.rename(columns={'Likes': 'AvgLikes'}, inplace=True)

# Sort by Date
avg_likes_date_df['Date'] = pd.to_datetime(avg_likes_date_df['Date'], errors='coerce')
avg_likes_date_df = avg_likes_date_df.dropna(subset=['Date']).sort_values(by='Date')

# Save to csv
avg_likes_date_df.to_csv("socialMediaTime.csv", index=False)
print("it worked!")