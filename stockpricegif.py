import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# Set a non-interactive backend for matplotlib
import matplotlib
matplotlib.use('Agg')

# Define the ticker and the period
ticker = 'TSLA'  # Tesla Inc
period = '10y'   

# Fetch data from Yahoo Finance
data = yf.download(ticker, period=period, interval='1d')  # Use daily data

# Check if data is available
if data is None or data.empty:
    raise ValueError("No data fetched from Yahoo Finance. Please check the ticker symbol and period.")

# Print the first few rows of data to verify
print(data.head())

# Extract dates and closing prices
dates = data.index
prices = data['Close']

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Function to update the plot
def update(frame):
    if frame > len(dates):
        return
    ax.clear()  # Clear previous content
    
    print(f"Plotting frame {frame} with data length: {len(dates[:frame])}")  # Debug print
    ax.plot(dates[:frame], prices[:frame], color='blue')  # Plot up to the current frame
    ax.set_title(f'{ticker} Stock Price Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    
    # Set x and y limits
    ax.set_xlim([dates.min(), dates.max()])
    ax.set_ylim([prices.min(), prices.max()])
    
    ax.grid(True)

    # Save the current frame
    file_name = f'{frame_dir}/frame_{frame:03d}.png'
    plt.savefig(file_name, bbox_inches='tight')  # Save with tight bounding box
    print(f"Saved frame {frame} as {file_name}")  # Debug print

# Create directory to store frames
frame_dir = r'C:\Users\navab\OneDrive\Desktop\Bhargav\project\frames'
if not os.path.exists(frame_dir):
    os.makedirs(frame_dir)
    print(f"Created directory: {frame_dir}")
else:
    print(f"Directory already exists: {frame_dir}")

# Save each frame as an image
for i in range(1, len(dates) + 1):  # Ensure we include the last frame
    update(i)  # Update the plot for the frame

# Verify if frames are created
frame_files = [f'{frame_dir}/frame_{i:03d}.png' for i in range(1, len(dates) + 1)]
print(f"Frame files to be used: {frame_files}")

# Check if frames actually exist
for frame_file in frame_files:
    if not os.path.exists(frame_file):
        print(f"Frame file does not exist: {frame_file}")

# Load all frame images and save as a GIF in the specified directory
gif_path = r'C:\Users\navab\OneDrive\Desktop\Bhargav\project\stock_prices.gif'

try:
    images = [Image.open(frame_file) for frame_file in frame_files if os.path.exists(frame_file)]
    if images:
        images[0].save(gif_path, save_all=True, append_images=images[1:], duration=100, loop=0)
        print(f"GIF saved to: {gif_path}")
    else:
        print("No images were loaded. Please check the frame files.")
except Exception as e:
    print(f"Error while creating GIF: {e}")

# Clean up temporary frame files
for frame_file in frame_files:
    if os.path.exists(frame_file):
        os.remove(frame_file)
