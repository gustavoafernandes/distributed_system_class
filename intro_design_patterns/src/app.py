from flask import Flask, jsonify

app = Flask(__name__)


# Vehicle factory (Factory Pattern)
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type, name):
        if vehicle_type == "car":
            return Car(name)
        elif vehicle_type == "bike":
            return Bike(name)
        raise ValueError("Vehicle type not supported")

# Vehicle classes
class Vehicle:
    def info(self):
        raise NotImplementedError

class Car(Vehicle):
    def __init__(self, name):
        self.name = name

    def info(self):
        return {"type": "Car", "name": self.name}

class Bike(Vehicle):
    def __init__(self, name):
        self.name = name

    def info(self):
        return {"type": "Bike", "name": self.name}

# Decorator for logging (also an Adapter)
def log_route(func):
    def wrapper(*args, **kwargs):
        print(f"Accessing route: {func.__name__}")
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__  # Necessary for Flask routing
    return wrapper

# Route to demonstrate Factory and Adapter Patterns
@app.route('/vehicle/<vehicle_type>/<name>')
@log_route
def get_vehicle_info(vehicle_type, name):
    try:
        vehicle = VehicleFactory.get_vehicle(vehicle_type, name)
        return jsonify(vehicle.info())
    except ValueError as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
