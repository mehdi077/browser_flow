import undetected_chromedriver as uc
import os
from selenium.webdriver.support import expected_conditions as EC
import psutil
import importlib

import data


def kill_relevant_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_info = proc.info
            if process_info['name'] in ['chrome', 'chromedriver']:
                os.kill(process_info['pid'], 9)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
kill_relevant_processes()


# ---------------------------------------------
def start_browser():
    options = uc.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Define the path for the profile
    user_data_dir = os.path.join(os.getcwd(), "chrome_profiles")

    # -------------------------- profiles here ---------------------------------
    profile_dir = "profile_name_1" 
    # profile_dir = "profile_name_2" 
    # profile_dir = "profile_name_3" 
    # profile_dir = "profile_name_4" 
    # profile_dir = "profile_name_5" 
    # profile_dir = "profile_name_6" 
    # --------------------------------------------------------------------------

    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument(f'--profile-directory={profile_dir}')

    # Create the user data directory if it doesn't exist
    if not os.path.exists(user_data_dir):
        os.makedirs(user_data_dir)
    driver = uc.Chrome(options=options)
    return driver

def control_browser(driver):
    driver.get("https://www.google.com") 
    print(driver.title)  
    # type exit to exit >> testing code <<
    while True:
        cmd = input("run! (type 'exit' to exit) > ")
        if cmd == "exit":
            break
        elif cmd == "":
            # load a txt file 
            try:
                # with open('code.txt', 'r') as file:
                #     code = file.read()
                # exec(code)  # <<<< testing code
                importlib.reload(data)
                data.main(driver)
            except Exception as e:
                print(f"Error executing code from file: {e}")
                continue
        else:
            print("Invalid command")


if __name__ == "__main__":
    driver = start_browser()
    try:
        control_browser(driver)
    finally:
        driver.quit()

