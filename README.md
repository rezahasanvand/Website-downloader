🌐 Website Downloader
<div align="center">
https://img.shields.io/badge/python-3.7+-blue.svg
https://img.shields.io/badge/license-MIT-green.svg
https://img.shields.io/badge/requests-2.28+-orange.svg
https://img.shields.io/badge/beautifulsoup4-4.11+-yellow.svg
https://img.shields.io/badge/lxml-4.9+-red.svg

Download entire websites with one click!

Features • Installation • Usage • Examples • Contributing

</div>
📖 Table of Contents
Features

Prerequisites

Installation

Usage

Output Structure

Examples

Important Notes

Troubleshooting

Contributing

License

Author

🚀 Features
Website Downloader is a powerful and simple tool for downloading entire websites. By entering a website URL, it downloads all resources including HTML, CSS, JavaScript, and images, and saves them in a structured format with separate folders.

✨ Key Features
✅ Complete Website Download - Downloads all HTML, CSS, JS, and image files

✅ Organized Structure - Files saved in separate folders (css, js, images)

✅ Automatic Path Management - Converts relative paths to absolute and updates them

✅ Multiple File Support - Supports PNG, JPG, GIF, SVG, WebP images, fonts, and more

✅ Simple Interface - Just enter the website URL and go!

✅ High Security - Browser simulation with proper User-Agent headers

✅ Error Handling - Displays download errors and continues the process

✅ Detailed Statistics - Shows count of downloaded files by type

✅ Timeout Management - Prevents hanging on slow connections

✅ UTF-8 Encoding - Proper character encoding for international websites

🎯 What Can You Download?
HTML Files - Main pages and subpages

CSS Stylesheets - All external and internal styles

JavaScript Files - All external scripts

Images - PNG, JPG, JPEG, GIF, SVG, WebP, BMP, ICO

Fonts - WOFF, WOFF2, TTF, OTF

Other Resources - JSON, XML, and other linked resources

📋 Prerequisites
Before you begin, ensure you have the following installed:

Python 3.7 or higher

pip (Python package manager)

Internet connection (to download websites)

Check Python Version
bash
python --version
# or
python3 --version
🔧 Installation
1. Clone the Repository
bash
git clone https://github.com/RezaHasanvand/website-downloader.git
cd website-downloader
2. Install Dependencies
Using requirements.txt:

bash
pip install -r requirements.txt
Or manually install:

bash
pip install requests beautifulsoup4 lxml
3. Verify Installation
bash
python -c "import requests, bs4, lxml; print('✅ All dependencies installed successfully!')"
💻 Usage
Method 1: Command Line Interface (CLI)
The simplest way to use Website Downloader:

bash
python website_downloader.py
Then follow the interactive prompts:

text
🔗 Please enter the website URL (e.g., https://example.com): https://example.com
📁 Output folder name (default: downloaded_site): my_website
Method 2: Python Script
Create a Python script and import the WebsiteDownloader class:

python
from website_downloader import WebsiteDownloader

# Download a website with custom settings
downloader = WebsiteDownloader(
    url="https://example.com",
    output_dir="my_website"
)
downloader.download_website()
Method 3: Advanced Configuration
python
from website_downloader import WebsiteDownloader

# Custom configuration
downloader = WebsiteDownloader(
    url="https://www.example.com",
    output_dir="downloaded_site"
)

# Override session settings if needed
downloader.session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# Start download
downloader.download_website()
📁 Output Structure
After successful download, the following structure is created:

text
my_website/                    # Root directory
├── index.html                 # Main HTML file
├── css/                       # All CSS files
│   ├── style.css
│   ├── main.css
│   └── responsive.css
├── js/                        # All JavaScript files
│   ├── script.js
│   ├── app.js
│   └── vendor.js
├── images/                    # All images
│   ├── logo.png
│   ├── banner.jpg
│   ├── icon.svg
│   └── background.webp
└── fonts/                     # Font files (if any)
    ├── font.woff2
    └── font.ttf
File Organization Details
Folder	Description	File Types
css/	Stylesheet files	.css, .scss, .less
js/	JavaScript files	.js, .mjs, .cjs
images/	Image files	.png, .jpg, .jpeg, .gif, .svg, .webp, .ico, .bmp
fonts/	Font files	.woff, .woff2, .ttf, .otf, .eot
🎯 Examples
Example 1: Download a Simple Website
bash
python website_downloader.py
Input:

text
🔗 URL: https://example.com
📁 Output folder: example_site
Output:

text
✅ Download complete!
📄 HTML file: index.html
📁 Folder: example_site
📊 Download Statistics:
   📄 HTML files: 1
   🎨 CSS files: 2
   📜 JS files: 3
   🖼️ Images: 5
   📁 Total files: 11
Example 2: Download a Documentation Site
python
from website_downloader import WebsiteDownloader

downloader = WebsiteDownloader(
    url="https://docs.python.org/3/",
    output_dir="python_docs"
)
downloader.download_website()
Example 3: Bulk Download Multiple Sites
python
from website_downloader import WebsiteDownloader

sites = [
    "https://example1.com",
    "https://example2.com",
    "https://example3.com"
]

for i, site in enumerate(sites):
    print(f"\n📥 Downloading site {i+1}/{len(sites)}: {site}")
    downloader = WebsiteDownloader(site, f"site_{i+1}")
    downloader.download_website()
Example 4: Custom User-Agent
python
from website_downloader import WebsiteDownloader

downloader = WebsiteDownloader("https://example.com", "custom_site")
downloader.session.headers.update({
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
})
downloader.download_website()
⚠️ Important Notes
🔒 Legal & Ethical Considerations
Copyright: Only use this tool for websites you have permission to download. Respect copyright laws and terms of service.

Robots.txt: Always check the website's robots.txt file to ensure you're allowed to crawl the site.

Rate Limiting: Don't send too many requests too quickly. Be respectful of the website's resources.

Personal Use: This tool is intended for personal, educational, or archival purposes only.

🚫 Limitations
Dynamic Websites: This tool is designed for static websites. For SPAs (React, Vue, Angular), you'll need more advanced tools like:

Puppeteer/Playwright (for JavaScript rendering)

HTTrack (for complex sites)

Custom scrapers

Login-Protected Sites: This tool cannot download sites that require authentication.

Large Websites: For very large websites (1000+ pages), the process may be slow and resource-intensive.

Modern Web Technologies: Some advanced features (WebGL, WebAssembly, etc.) might not be fully supported.

💡 Best Practices
Start Small: Test with simple websites first

Check Size: Some websites are very large (GBs) - be mindful of storage

Respect Resources: Use delay between requests if downloading many pages

Monitor Progress: Keep an eye on the download process

🔧 Troubleshooting
Common Issues and Solutions
Issue	Solution
Connection Error	Check your internet connection and try again
403 Forbidden	The website may be blocking automated requests. Try using a different User-Agent
Timeout Error	Increase the timeout value in the code
SSL Certificate Error	Add verify=False to the request or update your SSL certificates
Empty HTML	The website might be using JavaScript. Try using a different tool
Missing Resources	Some resources might use relative paths incorrectly. Check the source code
Debug Mode
To enable debug logging, modify the code:

python
import logging
logging.basicConfig(level=logging.DEBUG)
Increase Timeout
python
response = self.session.get(full_url, timeout=30)  # 30 seconds instead of 10
Custom Headers
python
downloader.session.headers.update({
    'User-Agent': 'Your Custom User-Agent',
    'Referer': 'https://example.com',
    'Accept-Language': 'en-US,en;q=0.9'
})
🤝 Contributing
Contributions are welcome! Here's how you can help:

🐛 Report Bugs
If you find a bug, please create an issue with:

Description of the problem

Steps to reproduce

Expected vs actual behavior

Screenshots if applicable

💡 Suggest Features
Have an idea for improvement? Open an issue with:

Clear description of the feature

Why it would be useful

How it should work

📝 Submit Code
Fork the repository

Create a feature branch:

bash
git checkout -b feature/amazing-feature
Commit your changes:

bash
git commit -m 'Add amazing feature'
Push to the branch:

bash
git push origin feature/amazing-feature
Open a Pull Request

📚 Improve Documentation
Fix typos or grammar issues

Add more examples

Improve explanations

Translate documentation

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

MIT License Summary
✅ Commercial use: You can use this code in commercial projects

✅ Modification: You can modify the code

✅ Distribution: You can distribute the code

✅ Private use: You can use it privately

⚠️ No warranty: The software is provided "as is" without warranty

👨‍💻 Author
Reza Hasanvand (رضا حسنوند)

Connect with Me
🌐 GitHub: github.com/RezaHasanvand

📧 Email: rezahasanvand75@gmail.com

💼 LinkedIn: linkedin.com/in/rezahasanvand

🐦 Twitter: @RezaHasanvand

Support My Work
If you find this tool useful, consider:

⭐ Starring the repository

🐛 Reporting issues

📝 Contributing to the code

🔗 Sharing with others

🙏 Acknowledgments
Special thanks to these amazing open-source projects:

Project	Description
Requests	Elegant HTTP library for Python
BeautifulSoup	HTML/XML parsing library
lxml	Fast HTML/XML processing
Python	The programming language
📊 Project Statistics
<div align="center">
Metric	Value
Language	Python 100%
Lines of Code	~300
Dependencies	3
File Types Supported	15+
Time to Download	Varies by site size
</div>
🔄 Changelog
v1.0.0 (Current)
✅ Initial release

✅ Full website download capability

✅ CSS, JS, and image extraction

✅ Automatic path management

✅ Organized output structure

Planned Features (v2.0.0)
🔄 Recursive subpage downloading

🔄 Multi-threading for faster downloads

🔄 Support for SPA websites

🔄 GUI interface

🔄 Download progress bar

🔄 Session persistence

<div align="center">
⭐ If you like this project, please give it a star!

Made with ❤️ by Reza Hasanvand

⬆ Back to Top

</div>
