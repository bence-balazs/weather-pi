from gpiozero import CPUTemperature

def main():
    cpu = CPUTemperature()
    formatted_value = format(cpu.temperature, '.1f')
    

if __name__ == "__main__":
    main()
