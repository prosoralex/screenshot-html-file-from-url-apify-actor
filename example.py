"""
Minimal working example: run the "Screenshot & HTML file from Url" Apify Actor
and print its results.

Setup:
    pip install apify-client
    export APIFY_TOKEN=your_apify_token_here   # console.apify.com > Settings > Integrations

This repo is just usage documentation for the Actor — the Actor's own source
code is not included here (it runs on Apify's infrastructure).
"""
import os
import sys

from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
ACTOR_ID = "leadsbrary/screenshot-html-file-from-url"

RUN_INPUT = {
    "urls": [
        {
            "url": "https://www.apify.com/"
        }
    ],
    "format": "png",
    "fullPage": True,
    "saveHtml": False,
    "viewportWidth": 1280,
    "viewportHeight": 720,
    "jpegQuality": 90,
    "waitUntil": "load",
    "delayBeforeScreenshotMs": 0,
    "scrollToBottom": False,
    "delayAfterScrollMs": 1000,
    "navigationTimeoutSecs": 60,
    "maxRequestRetries": 1,
    "maxConcurrency": 1,
    "proxyConfiguration": {
        "useApifyProxy": False
    }
}


def main() -> None:
    if not APIFY_TOKEN:
        sys.exit("Set the APIFY_TOKEN environment variable first (get one at console.apify.com).")

    client = ApifyClient(APIFY_TOKEN)

    print(f"Starting {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    print(f"Run finished with status: {run['status']}")

    print("Results:")
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)


if __name__ == "__main__":
    main()
