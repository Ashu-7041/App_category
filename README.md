📱 App Category Scraper
This repository provides a script to automatically extract app details from Google Play Store and Apple App Store using a list of app IDs or URLs. It compiles the results into a structured CSV format for analysis or downstream use.

🚀 Features
Scrapes app metadata like name, description, developer, rating, version, price, category, etc.

Supports both Google Play Store and Apple App Store.

Reads input app identifiers from a CSV file.

Outputs structured data into a timestamped CSV file.

Simple and extensible code structure for enhancements.

🗂️ Folder Structure
yaml
Copy
Edit
APP_CATEGORY/
│
├── services/                         # Core logic for scraping
│   └── app_scraper/
│       └── playstore_appstore_scraper.py
│
├── 2025-05-07_output.csv             # Sample output file
├── sample_input.csv                  # Sample input file
├── logger.py                         # Logging configuration
├── task.py                           # Entrypoint to run the scraper
├── Makefile                          # (Optional) Task automation
├── pyproject.toml                    # Build configuration
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
├── setup.cfg                         # Linting and setup config
📦 Installation
Clone the repository:

git clone https://github.com/yourusername/app-category-scraper.git
cd app-category-scraper
Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
📄 Usage
Prepare a CSV file with one column containing app identifiers (IDs or URLs).

For Play Store, use app package names like com.whatsapp.

For App Store, use numeric IDs like 333903271.

Update the file_name variable in task.py to point to your CSV file.

file_name = "/path/to/your_input.csv"
Run the script:

python task.py
Output: A CSV file named like 2025-05-07_output.csv will be created with all scraped data.

🔧 Configuration
Logging is managed via logger.py using structlog.

The scraper is initialized and executed in task.py.

📚 Dependencies
Dependencies are listed in requirements.txt, including:
pandas
google-play-scraper
requests
structlog

📝 License
This project is licensed under the MIT License.

Let me know if you'd like to add usage examples or Docker support.