import requests
import sys
URL = "https://alko.fi"
ALKO_SUBDIRECTORIES = ["punaviinit","roseviinit","valkoviinit","viinijuomat"]

def webpage_exists(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

def main():

	if len(sys.argv) < 2:
		exit(1)
		
	if sys.argv[1] != "alko":
		print("There is no wine at "+ URL)
		exit(1)

	print("Pinging "+ URL)
	
	
	
	nr_successes = 0
	
	for subdirectory in ALKO_SUBDIRECTORIES:
		if webpage_exists(URL + "/" + subdirectory):
			print("Reply from alko/tuotteet/"+subdirectory)
			nr_successes = nr_successes + 1
		else:
			print("Subdirectory "+subdirectory+" not found.")

	if nr_successes == 0:
		print("There is no wine in alko.")
	else:
		print("There is wine in alko.")
	
if __name__ == '__main__':
	main()