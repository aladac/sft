---
source: https://developer.civitai.com/docs/api/public-rest
additional_sources:
  - https://github.com/civitai/civitai/wiki/REST-API-Reference
  - https://education.civitai.com/civitais-guide-to-downloading-via-api/
fetched: 2026-01-19
---

# CivitAI REST API Reference

The Civitai REST API provides programmatic access to models, images, creators, and tags. The API is still in active development.

## Base URL

```
https://civitai.com/api/v1
```

## Authorization

Generate an API Key from [User Account Settings](https://civitai.com/user/account).

### Authorization Header

```http
GET https://civitai.com/api/v1/models
Content-Type: application/json
Authorization: Bearer {api_key}
```

### Query String

```http
GET https://civitai.com/api/v1/models?token={api_key}
```

## Endpoints

### GET /api/v1/creators

List creators/users.

**Query Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `limit` | number | Results per page (0-200, default 20). 0 returns all |
| `page` | number | Page number |
| `query` | string | Filter by username |

**Response:**

```json
{
  "items": [
    {
      "username": "Civitai",
      "modelCount": 848,
      "link": "https://civitai.com/api/v1/models?username=Civitai"
    }
  ],
  "metadata": {
    "totalItems": 46,
    "currentPage": 1,
    "pageSize": 20,
    "totalPages": 3,
    "nextPage": "https://civitai.com/api/v1/creators?page=2"
  }
}
```

---

### GET /api/v1/images

List images with generation metadata.

**Query Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `limit` | number | Results per page (0-200, default 100) |
| `postId` | number | Filter by post ID |
| `modelId` | number | Filter by model ID (gallery) |
| `modelVersionId` | number | Filter by model version |
| `username` | string | Filter by creator |
| `nsfw` | boolean/enum | `None`, `Soft`, `Mature`, `X` |
| `sort` | enum | `Most Reactions`, `Most Comments`, `Newest` |
| `period` | enum | `AllTime`, `Year`, `Month`, `Week`, `Day` |
| `page` | number | Page number |

**Response:**

```json
{
  "items": [
    {
      "id": 469632,
      "url": "https://imagecache.civitai.com/.../image.jpeg",
      "hash": "UKHU@6H?_ND*...",
      "width": 1024,
      "height": 1536,
      "nsfw": false,
      "nsfwLevel": "None",
      "createdAt": "2023-04-11T15:33:12.500Z",
      "postId": 138779,
      "stats": {
        "cryCount": 0,
        "laughCount": 0,
        "likeCount": 0,
        "heartCount": 0,
        "commentCount": 0
      },
      "meta": {
        "seed": 234871805,
        "Model": "Meina",
        "steps": 35,
        "prompt": "...",
        "sampler": "DPM++ SDE Karras",
        "cfgScale": 7,
        "negativePrompt": "..."
      },
      "username": "Cooler_Rider"
    }
  ],
  "metadata": {
    "nextCursor": 101,
    "nextPage": "https://civitai.com/api/v1/images?page=2"
  }
}
```

> Note: Uses cursor-based pagination since July 2023.

---

### GET /api/v1/models

List models (checkpoints, LoRAs, etc.).

**Query Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `limit` | number | Results per page (1-100, default 100) |
| `page` | number | Page number |
| `query` | string | Search by name |
| `tag` | string | Filter by tag |
| `username` | string | Filter by creator |
| `types` | enum[] | `Checkpoint`, `TextualInversion`, `Hypernetwork`, `AestheticGradient`, `LORA`, `Controlnet`, `Poses` |
| `sort` | enum | `Highest Rated`, `Most Downloaded`, `Newest` |
| `period` | enum | `AllTime`, `Year`, `Month`, `Week`, `Day` |
| `favorites` | boolean | Filter to user favorites (auth required) |
| `hidden` | boolean | Filter to hidden models (auth required) |
| `primaryFileOnly` | boolean | Only include primary file |
| `allowNoCredit` | boolean | Filter by credit requirements |
| `allowDerivatives` | boolean | Filter by derivative permissions |
| `allowCommercialUse` | enum | `None`, `Image`, `Rent`, `Sell` |
| `nsfw` | boolean | Filter NSFW content |
| `supportsGeneration` | boolean | Filter by generation support |

**Response:**

```json
{
  "items": [
    {
      "id": 1234,
      "name": "Model Name",
      "description": "<p>HTML description</p>",
      "type": "Checkpoint",
      "nsfw": false,
      "tags": ["anime", "realistic"],
      "mode": null,
      "creator": {
        "username": "creator",
        "image": "https://..."
      },
      "stats": {
        "downloadCount": 50000,
        "favoriteCount": 1000,
        "commentCount": 50,
        "ratingCount": 200,
        "rating": 4.8
      },
      "modelVersions": [
        {
          "id": 5678,
          "name": "v1.0",
          "description": "Changelog...",
          "createdAt": "2023-01-01T00:00:00.000Z",
          "downloadUrl": "https://civitai.com/api/download/models/5678",
          "trainedWords": ["trigger_word"],
          "files": [
            {
              "name": "model.safetensors",
              "sizeKB": 2048000,
              "type": "Model",
              "primary": true,
              "metadata": {
                "fp": "fp16",
                "size": "pruned",
                "format": "SafeTensor"
              },
              "pickleScanResult": "Success",
              "virusScanResult": "Success",
              "scannedAt": "2023-01-01T00:00:00.000Z",
              "hashes": {
                "SHA256": "abc123...",
                "AutoV2": "def456..."
              },
              "downloadUrl": "https://civitai.com/api/download/models/5678"
            }
          ],
          "images": [
            {
              "id": "img123",
              "url": "https://...",
              "nsfw": "None",
              "width": 512,
              "height": 768,
              "meta": { "prompt": "..." }
            }
          ]
        }
      ]
    }
  ],
  "metadata": {
    "totalItems": 1000,
    "currentPage": 1,
    "pageSize": 100,
    "totalPages": 10,
    "nextPage": "https://civitai.com/api/v1/models?page=2"
  }
}
```

---

### GET /api/v1/models/:modelId

Get a single model by ID.

**Response:** Same as single item from `/api/v1/models`

---

### GET /api/v1/model-versions/:modelVersionId

Get a specific model version.

**Response:**

```json
{
  "id": 5678,
  "modelId": 1234,
  "name": "v1.0",
  "createdAt": "2023-01-01T00:00:00.000Z",
  "downloadUrl": "https://civitai.com/api/download/models/5678",
  "trainedWords": ["trigger_word"],
  "files": [...],
  "images": [...]
}
```

---

### GET /api/v1/model-versions/by-hash/:hash

Get model version by file hash (SHA256 or AutoV2).

**Response:** Same as `/api/v1/model-versions/:modelVersionId`

---

### GET /api/v1/tags

List available tags.

**Query Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `limit` | number | Results per page (0-200, default 20). 0 returns all |
| `page` | number | Page number |
| `query` | string | Search tags by name |

**Response:**

```json
{
  "items": [
    {
      "name": "anime",
      "modelCount": 5000,
      "link": "https://civitai.com/api/v1/models?tag=anime"
    }
  ],
  "metadata": {
    "totalItems": 100,
    "currentPage": 1,
    "pageSize": 20,
    "totalPages": 5
  }
}
```

---

## Downloading Models

### Download URL

```
https://civitai.com/api/download/models/{modelVersionId}
```

Or with token for restricted models:

```
https://civitai.com/api/download/models/{modelVersionId}?token={api_key}
```

### Using wget

```bash
wget https://civitai.com/api/download/models/12345 --content-disposition
```

The `--content-disposition` flag ensures the correct filename is used.

### Using curl

```bash
curl -L -o model.safetensors \
  "https://civitai.com/api/download/models/12345?token=${CIVITAI_API_KEY}"
```

---

## Python Examples

### Search and Download

```python
import httpx
import os

API_KEY = os.environ.get("CIVITAI_API_KEY")
BASE_URL = "https://civitai.com/api/v1"

headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}

# Search for models
response = httpx.get(
    f"{BASE_URL}/models",
    params={
        "query": "illustrious",
        "types": "Checkpoint",
        "sort": "Most Downloaded",
        "limit": 5,
    },
    headers=headers,
)
models = response.json()

for model in models["items"]:
    print(f"{model['name']} - {model['stats']['downloadCount']} downloads")

    # Get download URL for latest version
    latest = model["modelVersions"][0]
    primary_file = next(f for f in latest["files"] if f.get("primary"))
    print(f"  Download: {primary_file['downloadUrl']}")
```

### Download with Resume

```python
import httpx
from pathlib import Path

def download_model(version_id: int, dest: Path, api_key: str | None = None):
    url = f"https://civitai.com/api/download/models/{version_id}"
    params = {"token": api_key} if api_key else {}
    headers = {}
    mode = "wb"
    initial = 0

    if dest.exists():
        initial = dest.stat().st_size
        headers["Range"] = f"bytes={initial}-"
        mode = "ab"

    with httpx.stream("GET", url, params=params, headers=headers, follow_redirects=True) as r:
        total = int(r.headers.get("content-length", 0)) + initial

        with open(dest, mode) as f:
            for chunk in r.iter_bytes(1024 * 1024):
                f.write(chunk)
                downloaded = f.tell()
                print(f"\r{downloaded / 1e6:.1f} / {total / 1e6:.1f} MB", end="")

    print("\nDone!")

# Usage
download_model(12345, Path("model.safetensors"), os.environ.get("CIVITAI_API_KEY"))
```

---

## Model Types

| Type | Description |
|------|-------------|
| `Checkpoint` | Full model weights (SD 1.5, SDXL, etc.) |
| `LORA` | Low-rank adaptation weights |
| `TextualInversion` | Textual inversion embeddings |
| `Hypernetwork` | Hypernetwork weights |
| `AestheticGradient` | Aesthetic gradient files |
| `Controlnet` | ControlNet models |
| `Poses` | Pose reference files |

## File Metadata

| Field | Values |
|-------|--------|
| `fp` | `fp16`, `fp32` |
| `size` | `full`, `pruned` |
| `format` | `SafeTensor`, `PickleTensor`, `Other` |

## Rate Limits

The API has rate limits in place. If you receive a 429 response, implement exponential backoff.
