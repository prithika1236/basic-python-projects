import time

def countdown_timer(seconds):
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r", flush=True)
            time.sleep(1)
            seconds -= 1
        print("00:00")
        print("Time's up!")
    except KeyboardInterrupt:
        print("\nCountdown stopped by user.")

def parse_time_input(time_str):
    parts = time_str.split(":")
    if len(parts) != 2:
        raise ValueError("Input must be in the format mm:ss")
    mins, secs = parts
    mins = int(mins)
    secs = int(secs)
    if mins < 0 or secs < 0 or secs >= 60:
        raise ValueError("Minutes must be >= 0, seconds must be between 0 and 59")
    return mins * 60 + secs

def main():
    print("Real-time Countdown Timer")
    time_input = input("Enter countdown time (mm:ss): ")
    try:
        total_seconds = parse_time_input(time_input)
        countdown_timer(total_seconds)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()



