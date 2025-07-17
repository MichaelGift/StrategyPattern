# Weather Station System

This project demonstrates the Observer Pattern using a weather station scenario. The Observer Pattern allows an object (the Subject) to maintain a list of dependents (Observers) and notify them of any state changes, promoting a decoupled design.

## Project Structure

```
Observer-Pattern/
├── __init__.py
├── client.py              # Entry point for the application
├── README.md
├── legacy/
│   ├── __init__.py
│   └── weather-station.py  # Non pattern implementation
└── observer/
    ├── __init__.py
    ├── interface.py
    ├── observers.py
    ├── subject.py
    └── __pycache__/
```

## Features
- Implements the Observer Pattern to demonstrate decoupled design.
- Includes a weather station example to showcase real-world usage.
- Provides a legacy implementation for comparison.

## How it Works
1. The `Subject` maintains a list of observers and notifies them of state changes.
2. Observers implement an interface to define their update behavior.
3. The `client.py` file demonstrates the interaction between the subject and observers.

## Usage
1. Clone the repository.
2. Navigate to the `Observer-Pattern` directory.
3. Run the `client.py` file to see the Observer Pattern in action:

   ```bash
   python client.py
   ```

## Example Output
When you run the `client.py` file, you will see output similar to the following:

```
Temperature: 25°C
Humidity: 60%
Pressure: 1013 hPa
```

## Adding a New Observer
1. Create a new class that implements the `Observer` interface.
2. Define the `update` method to handle state changes.
3. Register the new observer with the subject using the `add_observer` method.

## Requirements
- Python 3.7+

## Design Principles Used
- **Encapsulation**: The subject encapsulates the logic for managing observers.
- **Open/Closed Principle**: New observers can be added without modifying existing code.
- **Loose Coupling**: Observers and subjects are loosely coupled, promoting flexibility.