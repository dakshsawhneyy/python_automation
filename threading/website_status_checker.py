urls = ["https://google.com", "https://github.com", "https://amazon.com"]

def check_status(url):
    result = subprocess.run(["curl", "-s", "--max-time", "5", url], text=True, capture_output=True)
    status_code = result.returncode
    print(f"{url} return status code {status_code}")
    
# Loop over urls and create threads
for url in urls:
    t = threading.Thread(target=check_status, args=(url,))
    
    t.start()
    t.join()
