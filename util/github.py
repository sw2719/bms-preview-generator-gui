from typing import TypedDict

import requests
import json

from requests import HTTPError

API_URL = "https://api.github.com/repos/MikiraSora/BmsPreviewAudioGenerator/releases/latest"


class Release(TypedDict):
    version: str
    asset_url: str
    asset_name: str


def get_latest_release() -> Release:
    with requests.get(API_URL) as response:
        if response.status_code == 403 or response.status_code == 429:
            raise requests.HTTPError("GitHub API rate limit exceeded")

        response.raise_for_status()
        data = response.json()

        return Release(version=data["tag_name"],
                       asset_url=data["assets"][0]["browser_download_url"],
                       asset_name=data["assets"][0]["name"])
