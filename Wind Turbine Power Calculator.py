# Wind Turbine Power Calculator
# EEE Mini Project - Python

class WindTurbinePowerCalculator:

    def __init__(self, air_density, efficiency):
        self.air_density = air_density
        self.efficiency = efficiency

    def calculate_power(self, swept_area, wind_speed):
        # Wind Power = 0.5 × rho × A × V^3 × efficiency
        power = (
            0.5
            * self.air_density
            * swept_area
            * (wind_speed ** 3)
            * self.efficiency
        )

        return power

    def display_result(self, power, wind_speed):
        print("\n====================================")
        print("     WIND TURBINE POWER CALCULATOR")
        print("====================================")

        print(f"Wind Speed    : {wind_speed:.2f} m/s")
        print(f"Power Output  : {power:.2f} W")
        print(f"Power Output  : {power / 1000:.2f} kW")

        print("------------------------------------")

        if wind_speed < 3:
            print("Status        : LOW WIND SPEED")
        elif wind_speed < 12:
            print("Status        : POWER GENERATING")
        elif wind_speed <= 25:
            print("Status        : HIGH WIND SPEED")
        else:
            print("Status        : TURBINE SHUTDOWN")

        print("====================================")


# Main Program
print("WIND TURBINE POWER CALCULATOR")

swept_area = float(
    input("Enter turbine swept area (m²): ")
)

wind_speed = float(
    input("Enter wind speed (m/s): ")
)

# Typical simplified values
air_density = 1.225
efficiency = 0.35

# Input validation
if swept_area <= 0:
    print("Invalid swept area.")

elif wind_speed < 0:
    print("Wind speed cannot be negative.")

else:
    turbine = WindTurbinePowerCalculator(
        air_density,
        efficiency
    )

    power = turbine.calculate_power(
        swept_area,
        wind_speed
    )

    turbine.display_result(
        power,
        wind_speed
    )
