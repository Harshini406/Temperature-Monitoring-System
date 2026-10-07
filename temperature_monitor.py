import tkinter as tk


# -----------------------------
# CHECK TEMPERATURE
# -----------------------------
def check_temperature():

    value = temperature_input.get().strip()

    # Empty input
    if value == "":
        status_indicator.config(text="INVALID INPUT", bg="gray")
        fan_status.config(text="Fan: OFF")
        buzzer_status.config(text="Buzzer: OFF")
        message.config(text="Please enter a temperature.")
        return

    # Convert input to number
    try:
        temperature = float(value)
    except ValueError:
        status_indicator.config(text="INVALID INPUT", bg="gray")
        fan_status.config(text="Fan: OFF")
        buzzer_status.config(text="Buzzer: OFF")
        message.config(text="Please enter a valid number.")
        return

    # Check valid range
    if temperature < -50 or temperature > 150:
        status_indicator.config(text="INVALID RANGE", bg="gray")
        fan_status.config(text="Fan: OFF")
        buzzer_status.config(text="Buzzer: OFF")
        message.config(text="Enter a temperature between -50°C and 150°C.")
        return

    # -----------------------------
    # TEMPERATURE CONTROL LOGIC
    # -----------------------------

    if temperature < 30:

        status = "NORMAL"
        fan = "OFF"
        buzzer = "OFF"
        status_color = "green"
        message_text = "Temperature is within normal range."

    elif temperature <= 40:

        status = "WARNING"
        fan = "ON"
        buzzer = "OFF"
        status_color = "orange"
        message_text = "Temperature is high. Cooling activated."

    else:

        status = "CRITICAL"
        fan = "ON"
        buzzer = "ON"
        status_color = "red"
        message_text = "Critical temperature! Immediate attention required."

    # Update display
    status_indicator.config(
        text=status,
        bg=status_color
    )

    fan_status.config(
        text="Fan: " + fan
    )

    buzzer_status.config(
        text="Buzzer: " + buzzer
    )

    message.config(
        text=message_text
    )


# -----------------------------
# RESET
# -----------------------------
def reset_system():

    temperature_input.delete(0, tk.END)

    status_indicator.config(
        text="WAITING",
        bg="gray"
    )

    fan_status.config(
        text="Fan: OFF"
    )

    buzzer_status.config(
        text="Buzzer: OFF"
    )

    message.config(
        text="Enter a temperature to begin monitoring."
    )


# -----------------------------
# MAIN WINDOW
# -----------------------------
window = tk.Tk()

window.title("Temperature Monitoring System")

window.geometry("600x650")

window.resizable(False, False)


# -----------------------------
# TITLE
# -----------------------------
title = tk.Label(
    window,
    text="Temperature Monitoring System",
    font=("Arial", 24, "bold")
)

title.pack(pady=25)


# -----------------------------
# DESCRIPTION
# -----------------------------
description = tk.Label(
    window,
    text="Embedded Sensor Monitoring & Automatic Control",
    font=("Arial", 11)
)

description.pack(pady=5)


# -----------------------------
# TEMPERATURE INPUT
# -----------------------------
label = tk.Label(
    window,
    text="Enter Temperature (°C):",
    font=("Arial", 15, "bold")
)

label.pack(pady=(25, 8))


temperature_input = tk.Entry(
    window,
    font=("Arial", 16),
    justify="center",
    width=15
)

temperature_input.pack()


# -----------------------------
# BUTTONS
# -----------------------------
button_frame = tk.Frame(window)

button_frame.pack(pady=20)


check_button = tk.Button(
    button_frame,
    text="CHECK TEMPERATURE",
    font=("Arial", 12, "bold"),
    command=check_temperature,
    width=20
)

check_button.grid(row=0, column=0, padx=5)


reset_button = tk.Button(
    button_frame,
    text="RESET",
    font=("Arial", 12, "bold"),
    command=reset_system,
    width=10
)

reset_button.grid(row=0, column=1, padx=5)


# -----------------------------
# STATUS
# -----------------------------
status_label = tk.Label(
    window,
    text="SYSTEM STATUS",
    font=("Arial", 12, "bold")
)

status_label.pack(pady=(10, 5))


status_indicator = tk.Label(
    window,
    text="WAITING",
    font=("Arial", 22, "bold"),
    bg="gray",
    fg="white",
    width=18,
    height=2
)

status_indicator.pack(pady=5)


# -----------------------------
# FAN
# -----------------------------
fan_status = tk.Label(
    window,
    text="Fan: OFF",
    font=("Arial", 16)
)

fan_status.pack(pady=8)


# -----------------------------
# BUZZER
# -----------------------------
buzzer_status = tk.Label(
    window,
    text="Buzzer: OFF",
    font=("Arial", 16)
)

buzzer_status.pack(pady=8)


# -----------------------------
# MESSAGE
# -----------------------------
message = tk.Label(
    window,
    text="Enter a temperature to begin monitoring.",
    font=("Arial", 11),
    wraplength=500
)

message.pack(pady=20)


# -----------------------------
# THRESHOLDS
# -----------------------------
thresholds = tk.Label(
    window,
    text="Normal: <30°C    |    Warning: 30–40°C    |    Critical: >40°C",
    font=("Arial", 10)
)

thresholds.pack(pady=10)


# -----------------------------
# START PROGRAM
# -----------------------------
window.mainloop()
