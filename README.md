# Callsign Data Scraper

This Python script scrapes data for callsigns from a website and stores it in a CSV file. The script generates callsigns based on a pattern and retrieves information for each callsign.

## Usage

1. Install the required libraries by running the following command:

   ```bash
   pip install requests beautifulsoup4
   ```

2. Define the parameters for the scraping process, such as the starting callsign pattern, and the character sets for generating callsigns.

3. Run the script by executing the following command in your terminal:

   ```bash
   python your_script_name.py
   ```

4. The script will generate callsigns based on the specified pattern and retrieve information for each callsign.

5. The collected data will be stored in a CSV file named 'data-iar.csv' with columns: 'callsign', 'nama', 'provinsi', 'masalaku', 'tingkat', and 'status'.

6. The script prints the retrieved data to the terminal as it progresses.

## Example

Suppose you want to scrape data for callsigns starting with the pattern 'y' followed by different combinations of letters and numbers. The script will generate callsigns, retrieve information for each callsign, and save the data to a CSV file.

## License

This script is provided under the [MIT License](LICENSE).
```

Replace `"your_script_name.py"` with the actual name of your script. Customize the README.md file further if needed to include additional information or usage examples for your project.
