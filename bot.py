import requests
from datetime import date

def fetch_weather_report(location="Thiruvananthapuram"):
    """Queries wttr.in to extract a clean weather text summary."""
    endpoint_url = f"https://wttr.in/{location}?format=3"
    try:
        api_response = requests.get(endpoint_url, timeout=12)
        api_response.raise_for_status()
        return api_response.text.strip()
    except Exception as error:
        return f"Weather data tracking offline: {error}"

def fetch_motivational_quote():
    """Pulls a randomized daily motivational quote from ZenQuotes."""
    endpoint_url = "https://zenquotes.io/api/random"
    try:
        api_response = requests.get(endpoint_url, timeout=12)
        api_response.raise_for_status()
        json_payload = api_response.json()
        quote_text = json_payload[0]['q']
        quote_author = json_payload[0]['a']
        return f'"{quote_text}" — {quote_author}'
    except Exception as error:
        return f"Inspirational content sync failed: {error}"

def compile_daily_feed():
    """Gathers parameters and formats them into the structured layout."""
    calendar_today = date.today().strftime("%A, %d %b %Y")
    current_weather = fetch_weather_report()
    selected_quote = fetch_motivational_quote()
    
    output_feed = (
        f"==================================================\n"
        f"PULSE ENGINE — CORE DAILY FEED\n"
        f"Generated on: {calendar_today}\n"
        f"==================================================\n\n"
        f"LOCAL METRICS:\n"
        f"↳ {current_weather}\n\n"
        f"TODAY'S INSPIRATION:\n"
        f"↳ {selected_quote}\n\n"
        f"--------------------------------------------------"
    )
    return output_feed

def main_execution_loop():
    """Primary routine handled by the GitHub actions environment."""
    compiled_data = compile_daily_feed()
    print(compiled_data)
    
    target_filename = "daily_summary.txt"
    with open(target_filename, "w", encoding="utf-8") as target_file:
        target_file.write(compiled_data)
    print(f"\n[Success] Manifest exported to {target_filename}.")

if __name__ == "__main__":
    main_execution_loop()
