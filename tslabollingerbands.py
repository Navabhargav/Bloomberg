import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker and the period
ticker = 'TSLA'  # Tesla Inc
period = '10y'

# Fetch data from Yahoo Finance
data = yf.download(ticker, period=period, interval='1d')  # Use daily data

# Check if data is available
if data is None or data.empty:
    raise ValueError("No data fetched from Yahoo Finance. Please check the ticker symbol and period.")

# Calculate Bollinger Bands
window = 20  # Window for moving average
data['SMA'] = data['Close'].rolling(window=window).mean()
data['STD'] = data['Close'].rolling(window=window).std()
data['Upper Band'] = data['SMA'] + (data['STD'] * 2)
data['Lower Band'] = data['SMA'] - (data['STD'] * 2)

# Plot Bollinger Bands
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Close'], label='Close Price', color='blue')
plt.plot(data.index, data['SMA'], label='20-Day SMA', color='orange')
plt.plot(data.index, data['Upper Band'], label='Upper Band', color='red', linestyle='--')
plt.plot(data.index, data['Lower Band'], label='Lower Band', color='green', linestyle='--')

# Fill the area between the upper and lower bands
plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='lightgray', alpha=0.5)

# Customize the plot
plt.title(f'{ticker} Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)

# Save the plot to a file
output_path = r'C:\Users\navab\OneDrive\Desktop\Bhargav\project\bollinger_bands.png'
plt.tight_layout()
plt.savefig(output_path, dpi=300)
print(f"Plot saved to {output_path}")

# Uncomment the line below if you're in an interactive environment and want to display the plot
# plt.show()
