from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML table
with open('insert-html-table.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table
table = soup.find('table')

# Extract table headers and convert to lowercase
headers = [th.text.strip().lower() for th in table.find_all('th')]

# Extract table rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skip the header row
    cells = tr.find_all('td')
    row = []
    rows.append(row)

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to CSV
df.to_csv('your-output.csv', index=False, encoding='utf-8')
