import requests

ALKO_URL = "https://www.alko.fi"
SUBDIRECTORIES = ["punaviinit","roseviinit","valkoviinit","viinijuomat"]

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
	print("Pinging "+ALKO_URL)
	
	nr_successes = 0
	
	for subdirectory in SUBDIRECTORIES:
		if webpage_exists(ALKO_URL + "/" + subdirectory):
			print("Reply from alko/tuotteet/"+subdirectory)
			nr_successes = nr_successes + 1
		else:
			print("Subdirectory "+subdirectory+" not found.")

	if nr_successes == 0:
		print("There is no wine.")
	
if __name__ == '__main__':
	main()
