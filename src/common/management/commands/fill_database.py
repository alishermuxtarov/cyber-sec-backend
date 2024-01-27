import re

import requests
from django.core.management.base import BaseCommand
from common.models import Keyword, KeywordCategory, Host
from utils.converters import convert_cyrillic_to_latin
from utils.enums import HostRiskLevel, HostCategory
from utils.text import clean_text, is_cyrillic


class Command(BaseCommand):
    help = "Parse data from given API and create Keyword objects"
    hosts = []
    keywords = []

    def handle(self, *args, **kwargs):
        self.clean_database()
        self.fill_extremists_lists()
        self.fill_rublacklist_hosts()
        self.prepare_keywords_to_flush()
        self.prepare_hosts_to_flush()
        self.flush_keywords_to_database()
        self.flush_hosts_to_database()

    @staticmethod
    def clean_database():
        Keyword.objects.all().delete()
        Host.objects.all().delete()

    def fill_extremists_lists(self, *args, **kwargs):
        url = "https://data.egov.uz/apiPartner/Partner/WebService"
        params = {
            "token": "65b39338be3bf9366e6d7784",
            "name": "1-014-0006",
            "offset": 0,
            "limit": 100000,
            "lang": "uz",
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "result" in data and "data" in data["result"]:
            keywords_data = data["result"]["data"]

            for keyword_entry in keywords_data:
                keyword: str = keyword_entry.get("Nomi", "")
                self.stdout.write(self.style.SUCCESS(f"processing keyword: {keyword}"))
                text_between_quotes_found = False

                if (
                    "ijtimoiy" not in keyword.lower()
                    and "00/08/08" not in keyword
                    and "minjust" not in keyword
                    and "qaroriga" not in keyword
                ):
                    keyword = keyword.replace("(", "")
                    keyword = keyword.replace(")", "")
                    keyword = keyword.replace("=>", " ")
                    keyword = keyword.replace("t/me", "t.me")
                    keyword = keyword.replace("tiktok/", "tiktok.com/")
                    keyword = keyword.replace("inst/", "instagram.com/")
                    keyword = keyword.replace("www.", "")
                    keyword = keyword.replace("http://", "")
                    keyword = keyword.replace("https://", "")
                    keyword = keyword.replace("t.me", "https://t.me")
                    keyword = keyword.replace("ok.ru", "https://ok.ru")
                    keyword = keyword.replace("youtube.com", "https://youtube.com")
                    keyword = keyword.replace("facebook.com", "https://facebook.com")
                    keyword = keyword.replace("tiktok.com", "https://tiktok.com")
                    keyword = keyword.replace("instagram.com", "https://instagram.com")
                    # keyword = keyword.replace("", "")

                    text_between_quotes = re.findall(r'[«"“](.*?)[»"”]', keyword)

                    for item in text_between_quotes:
                        self.keywords.append(Keyword(keyword=item, category=KeywordCategory.EXTREMIST))
                        text_between_quotes_found = True

                    keyword = keyword.replace('"', "")
                    keyword = keyword.replace('"', "")
                    keyword = keyword.replace("«", "")
                    keyword = keyword.replace("»", "")

                    url_regex = r"https?://\S+"

                    found_urls = re.findall(url_regex, keyword)
                    for url in found_urls:
                        self.hosts.append(
                            Host(url=url, category=HostCategory.EXTREMIST, risk_level=HostRiskLevel.BLACKLIST)
                        )
                        keyword = keyword.replace(url, "")

                    if not text_between_quotes_found:
                        self.keywords.append(Keyword(keyword=keyword, category=KeywordCategory.EXTREMIST))
        else:
            self.stdout.write(self.style.ERROR('No "data" field found in API response'))

    def fill_rublacklist_hosts(self):
        url = "https://reestr.rublacklist.net/api/v3/domains/"
        response = requests.get(url)

        for domain in response.json():
            self.hosts.append(Host(url=domain, category=HostCategory.OTHER, risk_level=HostRiskLevel.BLACKLIST))

    def prepare_keywords_to_flush(self):
        self.stdout.write(self.style.SUCCESS(f"Preparing keywords to flush"))
        cyrillic_keywords = []
        for keyword in self.keywords:
            if keyword.keyword:
                keyword.keyword = clean_text(keyword.keyword)
                keyword.keyword = keyword.keyword.strip()
                keyword.keyword = keyword.keyword.lower()

                if is_cyrillic(keyword.keyword):
                    cyrillic_keywords.append(
                        Keyword(
                            keyword=convert_cyrillic_to_latin(keyword.keyword),
                            category=keyword.category,
                            allowed_for_host=keyword.allowed_for_host,
                        )
                    )

        self.keywords.extend(cyrillic_keywords)

    def prepare_hosts_to_flush(self):
        self.stdout.write(self.style.SUCCESS(f"Preparing hosts to flush"))
        for host in self.hosts:
            host.url = host.url.lower()
            host.url = host.url.replace('"', "")
            host.url = host.url.replace("http://", "")
            host.url = host.url.replace("https://", "")

    def flush_keywords_to_database(self):
        self.stdout.write(self.style.SUCCESS(f"Flushing keywords to database"))
        Keyword.objects.bulk_create(self.keywords)
        self.stdout.write(self.style.SUCCESS(f"{len(self.keywords)} keywords successfully added"))

    def flush_hosts_to_database(self):
        self.stdout.write(self.style.SUCCESS(f"Flushing hosts to database"))
        Host.objects.bulk_create(self.hosts)
        self.stdout.write(self.style.SUCCESS(f"{len(self.hosts)} hosts successfully added"))
