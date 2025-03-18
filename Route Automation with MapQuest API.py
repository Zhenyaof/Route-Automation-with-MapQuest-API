import requests

def get_trip_info(api_key, origin, destination):
    url = "https://www.mapquestapi.com/directions/v2/route"
    params = {
        "key": api_key,
        "from": origin,
        "to": destination
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Request timed out: {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return None

def display_trip_info(data):
    if data is None:
        print("No data received from API. Check your API key and internet connection.")
        return
    
    if data.get("info", {}).get("statuscode") == 0:
        route = data["route"]
        print(f"Trip Duration: {route.get('formattedTime', 'N/A')}")
        print(f"Distance: {route.get('distance', 0):.2f} miles")
        print(f"Fuel Used: {route.get('fuelUsed', 0):.2f} gallons")

        print("\nDirections:")
        for leg in route.get("legs", []):
            for maneuver in leg.get("maneuvers", []):
                print(maneuver.get("narrative", "No narrative provided."))
    else:
        print("Error: Invalid input or route not found.")
        print(f"Detailed error info: {data}")

def main():
    api_key = input("Enter your MapQuest API Key: ").strip()

    while True:
        origin = input("Enter the starting location (or type 'quit' to exit): ").strip()
        if origin.lower() == 'quit':
            break
        
        destination = input("Enter the destination (or type 'quit' to exit): ").strip()
        if destination.lower() == 'quit':
            break
        
        data = get_trip_info(api_key, origin, destination)
        display_trip_info(data)

if __name__ == "__main__":
    main()