# HoldFast Landing Page Deployment

## Setup

### Netlify Deployment (Recommended)

1. Install Go dependencies:
```bash
go mod tidy
```

2. Get your Netlify credentials:
   - **Access Token**: Create at https://app.netlify.com/user/applications#personal-access-tokens
   - **Site ID** (Optional): Use existing site ID, or
   - **Site Name** (Optional): Create new site with this name

## Deployment Options

### Option 1: Environment Variables (Recommended)
```bash
export NETLIFY_ACCESS_TOKEN="your_access_token"
export NETLIFY_SITE_NAME="holdfast-landing"  # For new site
# OR
export NETLIFY_SITE_ID="existing_site_id"    # For existing site

go run deploy.go
```

### Option 2: Deploy from Different Directory
```bash
# Deploy specific directory:
go run deploy.go /path/to/website/files
```

### Option 3: Build Go Binary (Optional)
```bash
# Build once, use anywhere:
go build -o deploy deploy.go
./deploy

# Or for different directory:
./deploy /path/to/website/files
```

## What Gets Deployed

The script automatically includes:
- `.html` files (your main pages)
- `.css` files (stylesheets)
- `.js` files (JavaScript)
- Image files (`.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`)
- `.ico` files (favicons)
- `.txt` files (robots.txt, etc.)
- `.json` and `.xml` files

## Netlify Setup

### First Time Setup

1. **Get Access Token**:
   - Go to [Netlify Personal Access Tokens](https://app.netlify.com/user/applications#personal-access-tokens)
   - Click "New access token"
   - Give it a name like "HoldFast Deploy"
   - Copy the token

2. **Deploy Options**:
   - **New Site**: Set `NETLIFY_SITE_NAME` to create a new site
   - **Existing Site**: Set `NETLIFY_SITE_ID` to deploy to existing site

### Features

- **Automatic Site Creation**: Creates site if it doesn't exist
- **Zip-based Deployment**: Efficiently uploads all files as a zip archive
- **Deployment Status Tracking**: Waits for deployment to complete
- **Live URL Output**: Shows both live and preview URLs
- **Error Handling**: Comprehensive error reporting

### Deployment Flow

1. **Site Verification**: Creates site or verifies existing site exists
2. **Archive Creation**: Zips all web files from source directory
3. **Upload**: Deploys zip archive to Netlify
4. **Status Monitoring**: Waits for deployment to complete
5. **URL Display**: Shows live site URL when ready

Your site will be available at: `https://site-name.netlify.app`

---

## Legacy Python Deployment (Cloudflare Pages)

<details>
<summary>Click to expand Python/Cloudflare deployment instructions</summary>

### Python Setup
```bash
pip install -r requirements.txt
```

### Cloudflare Credentials
- **Account ID**: Found in Cloudflare dashboard sidebar
- **API Token**: Create at https://dash.cloudflare.com/profile/api-tokens
  - Use "Custom token" with permissions:
    - `Cloudflare Pages:Edit`
    - `Account:Read`
- **Project Name**: Your Cloudflare Pages project name

### Usage
```bash
export CLOUDFLARE_ACCOUNT_ID="your_account_id"
export CLOUDFLARE_API_TOKEN="your_api_token"
export CLOUDFLARE_PROJECT_NAME="holdfast-landing"

python deploy_to_cloudflare.py
```

</details>