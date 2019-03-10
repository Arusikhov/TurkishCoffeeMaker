#this is ment to run in parallel with the Regular window and update the dictionary
import time


while True:
    #write to the data files from gpio pins
    print("Enter Weight Sensor Data: ")
    WeightSensor = input()
    f = open("Data_Sensor_Weight.txt", "w")
    f.write(WeightSensor)
    f.close()

    print("Temperature: ")
    Temp = input()
    f = open("Data_Temperature.txt", "w")
    f.write(Temp)
    f.close()

    print("Vibration Sensor: ")
    Vib = input()
    f = open("Data_Vibration_Sensor.txt", "w")
    f.write(Vib)
    f.close()

    time.sleep(1)






