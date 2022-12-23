import requests
import xml.etree.ElementTree as ET

# Replace YOUR_SITEMAP_URL with the URL of your sitemap
sitemap_url = "YOUR_SITEMAP_URL"

# Replace YOUR_SEARCH_CONSOLE_API_KEY with your Google Search Console API key
api_key = "YOUR_SEARCH_CONSOLE_API_KEY"

# Fetch the sitemap XML from the URL
response = requests.get(sitemap_url)

# Parse the sitemap XML
root = ET.fromstring(response.text)

# Find all the <loc> elements in the sitemap
loc_elements = root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")

# Extract the URLs from the <loc> elements
urls = [loc.text for loc in loc_elements]

# Iterate over the URLs and submit them to Google Search Console
for url in urls:
  # Send a POST request to the Google Search Console API to request indexing of the URL
  requests.post(
    "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run",
    params={"key": api_key},
    json={"url": url}
  )

print("All URLs submitted to Google Search Console for indexing!")


