from gpiozero import CPUTemperature

def main():
    cpu = CPUTemperature()
    print(cpu.temperature)
    formatted_value = format(cpu.temperature, '.2f')
    print(formatted_value)

if __name__ == "__main__":
    main()
