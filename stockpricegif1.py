import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Define the ticker and the period
ticker = 'TSLA'  # Tesla Inc
period = '10y'

# Fetch data from Yahoo Finance
data = yf.download(ticker, period=period, interval='1d')  # Use daily data

# Check if data is available
if data is None or data.empty:
    raise ValueError("No data fetched from Yahoo Finance. Please check the ticker symbol and period.")

# Extract dates and closing prices
dates = data.index
prices = data['Close']

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Define the update function
def update(frame):
    ax.clear()  # Clear previous content
    
    # Determine the range for the current frame
    start_index = max(0, frame - 252)  # Approx 252 trading days in a year
    end_index = min(frame, len(dates))  # Ensure we don't go out of bounds

    # Check for valid frame
    if start_index >= end_index:
        return  # Skip frames where there's no valid data

    # Print debug information
    print(f"Frame: {frame}, Start index: {start_index}, End index: {end_index}")

    # Get the current segment of data
    current_dates = dates[start_index:end_index]
    current_prices = prices[start_index:end_index]

    # Plot current frame
    ax.plot(current_dates, current_prices, color='blue')
    ax.set_title(f'{ticker} Stock Price Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    
    # Set x and y limits
    ax.set_xlim([current_dates.min(), current_dates.max()])
    ax.set_ylim([min(current_prices), max(current_prices)])
    
    ax.grid(True)

# Create and save the animation as a GIF
anim = FuncAnimation(fig, update, frames=len(dates), interval=100, repeat=False)

# Set up the path for the GIF
gif_path = r'C:\Users\navab\OneDrive\Desktop\Bhargav\project\stock_new_price.gif'

# Use PillowWriter to save the animation
writer = PillowWriter(fps=10)
try:
    anim.save(gif_path, writer=writer)
    print(f"GIF saved to: {gif_path}")
except Exception as e:
    print(f"Error while saving GIF: {e}")
