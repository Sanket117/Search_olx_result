import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_olx_car_covers(url):
    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Send GET request to the OLX search page
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all listing items
        listings = soup.find_all('li', class_='_4m2w7')
        
        # Prepare results
        results = []
        
        # Extract details from each listing
        for listing in listings:
            # Try to extract title
            title_elem = listing.find('div', class_='_1mko3')
            title = title_elem.text.strip() if title_elem else 'N/A'
            
            # Try to extract price
            price_elem = listing.find('div', class_='_1iTqv')
            price = price_elem.text.strip() if price_elem else 'N/A'
            
            # Try to extract location
            location_elem = listing.find('div', class_='_1JNK3')
            location = location_elem.text.strip() if location_elem else 'N/A'
            
            # Try to extract listing link
            link_elem = listing.find('a', class_='_2JC5U')
            link = link_elem['href'] if link_elem and link_elem.has_attr('href') else 'N/A'
            
            # Add to results
            results.append({
                'Title': title,
                'Price': price,
                'Location': location,
                'Link': link
            })
        
        # Create a timestamp for the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'olx_car_covers_{timestamp}.csv'
        
        # Write results to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            if results:
                fieldnames = results[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Write headers
                writer.writeheader()
                
                # Write data
                for result in results:
                    writer.writerow(result)
        
        print(f"Successfully scraped {len(results)} listings. Saved to {filename}")
        return filename
    
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# URL for OLX car cover search
url = 'https://www.olx.in/items/q-car-cover'

# Run the scraper
scrape_olx_car_covers(url)
