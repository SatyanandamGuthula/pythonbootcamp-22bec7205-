import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Brand': ['Tesla', 'Volkswagen', 'Polestar', 'BMW', 'Honda', 'Lucid', 'Volkswagen', 'Peugeot', 'Tesla', 'Audi'],
    'Model': ['Model 3 Long Range Dual Motor', 'ID.3 Pure', '2', 'iX3', 'e', 'Air', 'e-Golf', 'e-208', 'Model 3 Standard Range Plus', 'Q4 e-tron'],
    'AccelSec': [4.6, 10, 4.7, 6.8, 9.5, 2.8, 9.6, 8.1, 5.6, 6.3],
    'TopSpeed_KmH': [233, 160, 210, 180, 145, 250, 150, 150, 225, 180],
    'Range_Km': [450, 270, 400, 360, 170, 610, 190, 275, 310, 400],
    'Efficiency_WhKm': [161, 167, 181, 206, 168, 180, 168, 164, 153, 193],
    'FastCharge_KmH': [940, 250, 620, 560, 190, 620, 220, 420, 650, 540],
    'RapidCharge': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
    'PowerTrain': ['AWD', 'RWD', 'AWD', 'RWD', 'RWD', 'AWD', 'FWD', 'FWD', 'RWD', 'AWD'],
    'PlugType': ['Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS', 'Type 2 CCS'],
    'BodyStyle': ['Sedan', 'Hatchback', 'Liftback', 'SUV', 'Hatchback', 'Sedan', 'Hatchback', 'Hatchback', 'Sedan', 'SUV'],
    'Segment': ['D', 'C', 'D', 'D', 'B', 'F', 'C', 'B', 'D', 'D'],
    'Seats': [5, 5, 5, 5, 4, 5, 5, 5, 5, 5],
    'PriceEuro': [55480, 30000, 56440, 68040, 32997, 105000, 31900, 29682, 46380, 55000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df.head())

# Perform some pandas operations (you can customize based on your needs)
# For example, let's select specific columns
selected_columns = df[['Brand', 'Model', 'TopSpeed_KmH', 'Range_Km', 'PriceEuro']]
print("\nSelected Columns:")
print(selected_columns)

# Now, let's create a bar graph using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df['Model'], df['TopSpeed_KmH'], color='skyblue')
plt.xlabel('Model')
plt.ylabel('Top Speed (Km/H)')
plt.title('Top Speed of Electric Vehicle Models')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
