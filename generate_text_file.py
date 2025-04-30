import os

def main():
    with open("rsud20k-val.txt", "w") as f:
        for file in os.listdir(r"/home/michael/Dev/Python/TransWeather/data/test/rsud20k-val/input"):
            f.write(f"./rsud20k-val/input/{file}\n")

if __name__ == "__main__":
    main()