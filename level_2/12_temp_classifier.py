# Challenge: Using if-else logic create a temperature classifier (cold, warm, hot)
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

def classify_temp(temp):
    if temp > 100 or temp < 10:
        print("those are extreme temperatures!")
    elif temp >= 90:
        print("temperature is hot!")
    elif temp < 90 and temp > 30:
        print("temperature is warm")
    elif temp < 30:
        print("temperature is cold")
    else:
        print("Perhaps an invalid temperature value?")

classify_temp(92)
classify_temp(29)
classify_temp(67)
classify_temp(115)
classify_temp(5)
