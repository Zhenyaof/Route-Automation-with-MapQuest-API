# NetSec and Automation


## Introduction
Welcome to **Network Security and Automation**! This repository is dedicated to exploring **network automation, security, and enterprise networking solutions** using Python, APIs, and automation frameworks. The goal is to **simplify network operations**, enhance security, and automate repetitive tasks in IT environments.

Whether you're an IT professional, network engineer, or cybersecurity enthusiast, this repository will serve as a good resource for learning and implementing automation in networking.

## Projects
### **Project 1: Route Automation with MapQuest API**
#### **Overview**
The first project in this repository demonstrates how to use the **MapQuest Directions API** to automate route calculations between two locations. This can be useful for network engineers working on **logistics, network path analysis, or IoT tracking applications**.

#### **Prerequisite**
To use this project, you need to **obtain an API key** from the [MapQuest Developer Website](https://developer.mapquest.com/). Sign up for a free account, generate an API key, and use it in the script.

#### **Features**
- Fetches trip details like **duration, distance, and fuel usage**.
- Provides **step-by-step directions** for the route.
- Implements **error handling** for better API request management.

---

## **Code Implementation**

```python
import requests

def get_trip_info(api_key, origin, destination):
    """Fetches route details between two locations using the MapQuest API."""
    url = "https://www.mapquestapi.com/directions/v2/route"
    params = {
        "key": api_key,
        "from": origin,
        "to": destination
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raises an error for unsuccessful requests
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
    """Displays trip details like duration, distance, and directions."""
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
    """Handles user input and initiates API calls."""
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
```

---

## **Detailed Code Breakdown**
### **1. Importing Dependencies**
```python
import requests
```
- The `requests` module is used to send HTTP requests to the MapQuest API.

### **2. Fetching Trip Information (`get_trip_info`)**
```python
def get_trip_info(api_key, origin, destination):
```
- Defines a function that takes an **API key, origin, and destination** as parameters.
- This function makes a request to **MapQuest API** to retrieve trip details.

```python
url = "https://www.mapquestapi.com/directions/v2/route"
params = {
    "key": api_key,
    "from": origin,
    "to": destination
}
```
- Specifies the **API endpoint** and prepares **query parameters** to send in the request.

```python
response = requests.get(url, params=params, timeout=10)
```
- Sends a `GET` request with the **API key, origin, and destination**.
- Uses a **timeout of 10 seconds** to prevent indefinite waiting.

```python
response.raise_for_status()
```
- Checks for **HTTP errors** (like 404 Not Found, 500 Server Error).

```python
return response.json()
```
- Returns the **JSON response** from the API if successful.

### **3. Handling Errors**
```python
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
```
- Catches errors related to **HTTP responses**, such as 404 or 500.

```python
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error: {conn_err}")
```
- Handles issues like **network disconnections**.

```python
except requests.exceptions.Timeout as timeout_err:
    print(f"Request timed out: {timeout_err}")
```
- Handles **slow API responses**.

### **4. Displaying Trip Information (`display_trip_info`)**
```python
def display_trip_info(data):
```
- Extracts **trip duration, distance, fuel usage, and directions**.
- Handles cases where API returns an error.

```python
if data.get("info", {}).get("statuscode") == 0:
```
- Ensures that the API response is **valid**.

```python
for leg in route.get("legs", []):
    for maneuver in leg.get("maneuvers", []):
        print(maneuver.get("narrative", "No narrative provided."))
```
- Loops through **route legs** and **maneuvers** to print step-by-step directions.

### **5. User Interaction (`main`)**
```python
def main():
```
- Collects **user input** for **API key, origin, and destination**.
- Allows the user to **enter multiple locations** or type `quit` to exit.

### **6. Running the Script**
```python
if __name__ == "__main__":
    main()
```
- Ensures the script runs only when executed directly, not when imported as a module.

---

## **How to Use**
1. **Install dependencies** (if not installed):
   ```sh
   pip install requests
   ```
2. **Run the script**:
   ```sh
   python script.py
   ```
3. **Enter your MapQuest API Key**. 
5. **Provide Origin and Destination** to get trip details.

---

## **Future Enhancements**
- Add **Google Maps API** support.
- Implement **GUI with Tkinter or Flask API**.
- Include **real-time traffic conditions**

## **Output**
Here’s an example of what the output might look like when running the script:

```sh
Enter your MapQuest API Key: your-api-key
Enter the starting location (or type 'quit' to exit): New York, NY
Enter the destination (or type 'quit' to exit): Boston, MA
Trip Duration: 3 hours 45 minutes
Distance: 215.50 miles
Fuel Used: 8.23 gallons

Directions:
Start out going east on I-95 N.
Take exit 46 for Route 1.
...





