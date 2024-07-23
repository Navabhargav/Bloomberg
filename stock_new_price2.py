import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.dates as mdates

# Define the ticker and the period
ticker = 'TSLA'  # Tesla Inc
period = '10y'    # Use 1 year of daily data

# Fetch data from Yahoo Finance
data = yf.download(ticker, period=period, interval='1d')  # Use daily data

# Check if data is available
if data is None or data.empty:
    raise ValueError("No data fetched from Yahoo Finance. Please check the ticker symbol and period.")

# Extract dates and the required price variables
dates = data.index
open_prices = data['Open']
high_prices = data['High']
low_prices = data['Low']
close_prices = data['Close']

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 7))

# Define the update function for the animation
def update(frame):
    ax.clear()  # Clear previous content

    # Determine the range for the current frame
    start_index = max(0, frame - 30)  # Show the past 30 days
    end_index = min(frame + 1, len(dates))  # Ensure we don't go out of bounds

    # Check for valid frame
    if start_index >= end_index:
        return  # Skip frames where there's no valid data

    # Get the current segment of data
    current_dates = dates[start_index:end_index]
    current_open = open_prices[start_index:end_index]
    current_high = high_prices[start_index:end_index]
    current_low = low_prices[start_index:end_index]
    current_close = close_prices[start_index:end_index]

    # Plot the lines for each price type
    ax.plot(current_dates, current_open, label='Open', color='blue', linestyle='-', marker='o')
    ax.plot(current_dates, current_high, label='High', color='green', linestyle='-', marker='o')
    ax.plot(current_dates, current_low, label='Low', color='red', linestyle='-', marker='o')
    ax.plot(current_dates, current_close, label='Close', color='purple', linestyle='-', marker='o')

    # Format the x-axis to show dates
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Update title, labels, and date
    current_date = current_dates[-1].strftime('%Y-%m-%d')
    ax.set_title(f'{ticker} Stock Prices (Date: {current_date})')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.legend()
    ax.grid(True)

# Create and save the animation as a GIF
frames = len(dates)
anim = FuncAnimation(fig, update, frames=frames, interval=200, repeat=False)

# Set up the path for the GIF
gif_path = r'C:\Users\navab\OneDrive\Desktop\Bhargav\project\stock_new_price2.gif'

# Use PillowWriter to save the animation
writer = PillowWriter(fps=10)
try:
    anim.save(gif_path, writer=writer)
    print(f"GIF saved to: {gif_path}")
except Exception as e:
    print(f"Error while saving GIF: {e}")
