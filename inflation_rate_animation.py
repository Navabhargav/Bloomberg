import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

file_path = "C:/Users/navab/Downloads/imf-dm-export-20240723 (2).xlsx"  # Update this to the path of your .xlsx file
data = pd.read_excel(file_path, sheet_name='PCPIEPCH')

Country='Inflation rate, end of period consumer prices (Annual percent change)'

countries = data[Country].unique()
print("Available countries:")
for country in countries:
    print(country)

# Input from user
selected_country = input("Enter the name of the country to plot the inflation rate: ")

# Check if the country is in the list
if selected_country not in countries:
    print("Country not found in the list.")
else:
    # Extract data for the selected country if 'Country' column exists
    if Country in data.columns:
        years = data.columns[1:]  # Assuming the first column is the country name
        inflation_rates = data[data[Country] == selected_country].iloc[0, 1:]

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(years, inflation_rates, marker='o')
        plt.title(f'Inflation Rate Over Time for {selected_country}')
        plt.xlabel('Year')
        plt.ylabel('Inflation Rate (%)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Data does not contain a 'Country' column.")

# Check if the country is in the list
if selected_country not in countries:
    print("Country not found in the list.")
else:
    # Check if the column exists
    if Country in data.columns:
        years = data.columns[1:]  # Assuming the first column is the country name
        inflation_rates = data[data[Country] == selected_country].iloc[0, 1:]

        # Update function for animation
        def update(frame):
            x = years[:frame+1]
            y = inflation_rates[:frame+1]
            line.set_data(range(len(x)), y)
            ax.set_xticks(range(len(x)))
            ax.set_xticklabels(x, rotation=45)
            return line,

        # Create animation
        ani = FuncAnimation(fig, update, frames=len(years), blit=True, repeat=False)


        # Save as GIF to the specified directory
        save_path = "C:/Users/navab/OneDrive/Desktop/Bhargav/project/demo/inflation_rate_animation.gif"
        ani.save(save_path, writer='pillow')
        print(f"Animation saved as GIF at: {save_path}")
    else:
        print("Data does not contain a 'Country' column.")
