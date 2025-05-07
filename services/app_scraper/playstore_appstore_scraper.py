import structlog
import sys
import os
from datetime import datetime
from google_play_scraper import app
import requests
import csv
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from logger import configure_logging
configure_logging()
logger = structlog.get_logger(__name__)


class AppScraper:

    class AppScraperException(Exception):
        pass

    def __init__(self):
        pass

    def _fetch_playstore_data(self, app_id):
        try:
            result = app(
                app_id,
                lang='en',
                country='us'
            )
            return result
        except Exception as e:
            logger.error(f"Error in fetching playstore data: {e}", app_id=app_id)

    def _fetch_appstore_data(self, app_id):
        try:
            response = requests.get(f"https://itunes.apple.com/lookup?id={app_id}")
            data = response.json()
            return data
        except Exception as e:
            logger.error(f"Error in fetching appstore data: {e}", app_id=app_id)

    def _format_playstore_data(self, data, app_id):
        playstore_details = {
            "app_id": app_id,
            "app_name": "",
            "description": "",
            "categories": "",
            "developer": "",
            "price": "",
            "primary_category": "",
            "version": "",
            "rating": "",
            "installs": "",
            "url": "",
            "developer_url": "",
        }

        if data:
            playstore_details = {
                "app_id": app_id,
                "app_name": data.get("title", ""),
                "description": data.get("description", ""),
                "categories": [category['name'] for category in data['categories']],
                "developer": data.get("developer", ""),
                "price": data.get("price", ""),
                "primary_category": data.get("genre", ""),
                "version": data.get("version", ""),
                "rating": data.get("score", ""),
                "installs": str(data.get("realInstalls", "")),
                "url": data.get("url", ""),
                "developer_url": data.get("developerWebsite", ""),
            }
            return playstore_details
        return playstore_details

    def _format_appstore_data(self, data, app_id):
        appstore_details = {
            "app_id": app_id,
            "app_name": "",
            "description": "",
            "categories": "",
            "developer": "",
            "price": "",
            "primary_category": "",
            "version": "",
            "rating": "",
            "installs": "",
            "url": "",
            "developer_url": "",
        }
        if data["resultCount"] > 0:
            app_data = data["results"][0]
            appstore_details = {
                "app_id": app_id,
                "app_name": app_data.get("trackName", ""),
                "description": app_data.get("description", ""),
                "categories": app_data.get("genres", []),
                "developer": app_data.get("sellerName", ""),
                "price": app_data.get("formattedPrice", ""),
                "primary_category": app_data.get("primaryGenreName", ""),
                "version": app_data.get("version", ""),
                "rating": app_data.get("averageUserRating", ""),
                "installs": "",
                "url": app_data.get("trackViewUrl", ""),
                "developer_url": data.get("artistViewUrl", ""),
            }
            return appstore_details
        return appstore_details

    def _read_and_return_urls(self, csv_path):
        df = pd.read_csv(csv_path)
        if not df.empty:
            first_column = df.iloc[:, 0]
            return first_column.tolist()
        return []

    def _separate_app_ids(self, app_url):
        try:
            if app_url.isdigit():
                return "app_store"
            else:
                return "playstore"
        except Exception as e:
            logger.error(f"Error in separating app ids: {e}")
            return None

    def _save_app_data_to_csv(self, data, output_csv):
        fieldnames = [
            "app_id", "app_name", "description", "categories", "developer", "price",
            "primary_category", "version", "rating", "installs", "url", "developer_url"
        ]

        file_exists = os.path.isfile(output_csv)

        with open(output_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            if isinstance(data.get('screenshots'), list):
                data['screenshots'] = ', '.join(data['screenshots'])

            writer.writerow(data)

    def app_data_scraper(self, csv_file):
        all_apps = self._read_and_return_urls(csv_file)
        for apps in all_apps:
            logger.info("Scrapping details for - {app}".format(app=app))
            try:
                if self._separate_app_ids(apps) == "app_store":
                    data = self._fetch_appstore_data(apps)
                    formatted_data = self._format_appstore_data(data, apps)
                else:
                    data = self._fetch_playstore_data(apps)
                    formatted_data = self._format_playstore_data(data, apps)
                self._save_app_data_to_csv(formatted_data, f"{datetime.today().date()}_output.csv")
            except Exception as e:
                logger.error(f"Error in fetching app data: {e}")
                continue
