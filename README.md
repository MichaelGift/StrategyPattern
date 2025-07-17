# Design Patterns in Python

This repository demonstrates the implementation of various design patterns in Python. Each pattern is implemented in its own directory with clear examples and explanations to help you understand and apply these patterns in real-world scenarios.

## Project Structure

```
Design-Patterns/
├── Observer-Pattern/       # Implementation of the Observer Pattern
│   ├── client.py           # Entry point for the Observer Pattern example
│   ├── README.md           # Documentation for the Observer Pattern
│   ├── legacy/             # Legacy implementation for comparison
│   └── observer/           # Core implementation of the Observer Pattern
├── Strategy-Pattern/       # Implementation of the Strategy Pattern
│   ├── client.py           # Entry point for the Strategy Pattern example
│   ├── README.md           # Documentation for the Strategy Pattern
│   ├── legacy/             # Legacy implementation for comparison
│   └── strategy/           # Core implementation of the Strategy Pattern
├── LICENSE                 # License for the repository
└── CODE_OF_CONDUCT.md      # Code of Conduct for contributors
```

## Patterns Included

### 1. Observer Pattern
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. This is demonstrated using a weather station example.

- **Directory**: `Observer-Pattern/`
- **Key Features**:
  - Decoupled design using subjects and observers.
  - Real-world example of a weather station.
  - Legacy implementation for comparison.

### 2. Strategy Pattern
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern lets the algorithm vary independently from clients that use it.

- **Directory**: `Strategy-Pattern/`
- **Key Features**:
  - Encapsulation of algorithms.
  - Real-world example of a processing strategy.
  - Legacy implementation for comparison.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/design-patterns.git
   ```
2. Navigate to the desired pattern directory (e.g., `Observer-Pattern` or `Strategy-Pattern`).
3. Follow the instructions in the respective `README.md` file to run the examples.

## Requirements
- Python 3.7+

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or additional patterns.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing to this project.