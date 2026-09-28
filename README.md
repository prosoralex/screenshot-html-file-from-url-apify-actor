# Screenshot & HTML file from Url — Apify Actor usage guide

[![Run for free on Apify](https://img.shields.io/badge/Apify-Run%20it%20free%20%E2%80%94%20%245%2Fmo%20credit-24C1E0)](https://console.apify.com/sign-up?fpr=aupara)

From 1$/1000 results. Capture website screenshots &/or full-page HTML in one run, from $1/1000 URLs. PNG, JPEG & PDF — full-page, custom viewport, lazy-load scroll, cookie-banner hiding, batch mode. HTML files open correctly in any browser. REST API ready. No watermark.

> **This repository does not contain the Actor's source code.** The Actor
> itself is closed-source and runs on Apify's infrastructure — this repo is
> just documentation and example client code showing how to call it via the
> Apify API/SDK with your own Apify API token. Think of it as a "cookbook"
> repo, not the product itself.

**Run it on Apify →** [https://apify.com/leadsbrary/screenshot-html-file-from-url?fpr=aupara](https://apify.com/leadsbrary/screenshot-html-file-from-url?fpr=aupara)

## What it does

Capture full-page visual and HTML archives of webpages by loading each URL in a real browser and saving a screenshot (PNG, JPEG) or PDF together with an optional complete HTML source. The Actor performs automated navigation and rendering, supports full-page or viewport-only captures, adjustable viewport dimensions and image quality, PDF output, and automatic resolution of relative links in the saved HTML so the archive renders offline. It can trigger lazy-loaded content by scrolling, hide DOM elements via CSS selectors, wait for different load conditions, apply configurable delays, retry failed navigations, run parallel captures, and use proxies. Outputs are per-URL metadata that indicate success, final URL, page title and HTTP status, timing/duration, and links to the generated screenshot/PDF and the archived HTML file.…

## Pricing

Pay-per-event pricing — you only pay for what the Actor actually delivers:

- **Actor Start** — $0.00005 (one-time, per run). Charged when the Actor starts running. Number of events charged depends on Actor memory (one event per GB, minimum one event).
- **result** — $0.002–$0.001 depending on your Apify usage tier. Single result in the default dataset.

*(Apify may also charge a small amount for the platform compute the Actor
uses while running — see the [pricing tab](https://apify.com/leadsbrary/screenshot-html-file-from-url?fpr=aupara) on the Actor page
for exact current numbers.)*

## Quick start

You need an Apify account and API token (`console.apify.com` → Settings →
Integrations). Don't have one yet? See the signup section below — new
accounts get **$5 of free usage credit every month**.

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/leadsbrary~screenshot-html-file-from-url/runs?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "urls": [
    {
      "url": "https://www.apify.com/"
    }
  ],
  "format": "png",
  "fullPage": true,
  "saveHtml": false,
  "viewportWidth": 1280,
  "viewportHeight": 720,
  "jpegQuality": 90,
  "waitUntil": "load",
  "delayBeforeScreenshotMs": 0,
  "scrollToBottom": false,
  "delayAfterScrollMs": 1000,
  "navigationTimeoutSecs": 60,
  "maxRequestRetries": 1,
  "maxConcurrency": 1,
  "proxyConfiguration": {
    "useApifyProxy": false
  }
}'
```

### Python (`apify-client`)

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

run_input = {
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

run = client.actor("leadsbrary/screenshot-html-file-from-url").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });

const runInput = {
  "urls": [
    {
      "url": "https://www.apify.com/"
    }
  ],
  "format": "png",
  "fullPage": true,
  "saveHtml": false,
  "viewportWidth": 1280,
  "viewportHeight": 720,
  "jpegQuality": 90,
  "waitUntil": "load",
  "delayBeforeScreenshotMs": 0,
  "scrollToBottom": false,
  "delayAfterScrollMs": 1000,
  "navigationTimeoutSecs": 60,
  "maxRequestRetries": 1,
  "maxConcurrency": 1,
  "proxyConfiguration": {
    "useApifyProxy": false
  }
};

const run = await client.actor('leadsbrary/screenshot-html-file-from-url').call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

See [`example.py`](./example.py) in this repo for a complete runnable script.

## Don't have an Apify account yet?

[Sign up here](https://console.apify.com/sign-up?fpr=aupara) — new accounts get **$5 of free platform credit
every month**, enough to try most Actors without paying anything upfront.
Browsing for other tools? The full [Apify Store](https://apify.com/store?fpr=aupara) has thousands
of ready-made Actors.

## Links

- Actor page (run it, see live pricing/reviews): [https://apify.com/leadsbrary/screenshot-html-file-from-url?fpr=aupara](https://apify.com/leadsbrary/screenshot-html-file-from-url?fpr=aupara)
- All Actors from this developer: [https://apify.com/leadsbrary?fpr=aupara](https://apify.com/leadsbrary?fpr=aupara)
- Apify API docs: [https://docs.apify.com/api/v2](https://docs.apify.com/api/v2)

## License

The example code in this repository (README snippets, `example.py`) is
released under the MIT License — see [LICENSE](./LICENSE). This does not
cover the Actor itself, which remains closed-source and is operated by its
developer on the Apify platform.
