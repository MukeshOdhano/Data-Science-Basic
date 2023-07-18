from requests import get

def get_data(url):
  try:
    response = get(url)
    if response.status_code == 200:
      data = response.json()
      return (data['content'])
    else:
      print("Error")
      return None
    
  except get.exceptions.RequestException as e:
    print(f"error: {e}")
    return None
    
data = get_data("https://api.quotable.io/random")
print(data)