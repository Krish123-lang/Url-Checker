import requests

def main(url):
  print("Checking connectivity...")
  r = requests.get(url) # Getting the url
  print("Connected to ", url, "successfully") # printing success message
  print("The Status code is ", r.status_code)  # printing status code

inpUrl = input("Enter the url link: ") # enter the url link

main(inpUrl) # calling function with parameter
