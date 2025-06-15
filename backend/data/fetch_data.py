print("🧪 Script started...")

from pybaseball import statcast
import pandas as pd

def fetch_statcast_data(start_date: str, end_date: str, save_csv=True):
    print(f"📊 Fetching Statcast data from {start_date} to {end_date}...")
    try:
        data = statcast(start_dt=start_date, end_dt=end_date)
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return None

    if save_csv:
        filename = f"statcast_{start_date}_to_{end_date}.csv"
        try:
            data.to_csv(filename, index=False)
            print(f"✅ Data saved to {filename}.")
        except Exception as e:
            print(f"❌ Error saving CSV: {e}")
    else:
        print(data.head())

    return data

if __name__ == "__main__":
    print("🚀 Running main...")
    fetch_statcast_data("2024-04-01", "2024-04-07")
