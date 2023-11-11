from gpiozero import CPUTemperature

def main():
    cpu = CPUTemperature()
    print(cpu.temperature)

if __name__ == "__main__":
    main()
