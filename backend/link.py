import requests

access_token = 'EAAkeKJ4W0MUBOZCUlvEDolTfNX6jywTvW3ZCuS4kh28dm061PfTl9HnKcuvzitrT13ZCqZCkBYCodZA1EF1sPx1gGYQUwJ9mofcokkK9it2toDCMZB6hnCuqEBiQlRW6odEKsca0dGEsdLMTZCAZCzWbAZCbKJCUaZAchQGqsWZAWAfQJniJVixX7uOz16nKyQpxiSWgZAfZA8mgGACqCSHKkjIt6jkdRjHRnibZAquZCgSLjhu'
url = f"https://graph.facebook.com/v14.0/me?access_token={access_token}"

response = requests.get(url)
data = response.json()

print(data)
