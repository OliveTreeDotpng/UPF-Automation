import time

SLEEP_TIME = 2

def generate_report():
    print("Generating...")
    time.sleep(SLEEP_TIME)
    print("Generated!")

def send_email():
    print("Sending...")
    time.sleep(SLEEP_TIME)
    print("Sent!")

def backup_files():
    print("Loading...")
    time.sleep(SLEEP_TIME)
    print("Backupp Complete!")

def full_workflow():
    backup_files()
    data = fetch_data()
    process_data(data)
    generate_report()
    send_email()


if __name__=="__main__":
    full_workflow()
