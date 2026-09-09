<h3>Website Downloader</h3>
Download entire websites with all resources (HTML, CSS, JavaScript, images, fonts) organized in a clean folder structure.
<h3>Features</h3>
Website Downloader is a powerful and simple tool for downloading entire websites. By entering a website URL, it downloads all resources, including HTML, CSS, JavaScript, and images, and saves them in a structured format with separate folders.

<h3>Key Features</h3>
<ul>
<li>✅ Complete Website Download - Downloads all HTML, CSS, JS, and image files</li>
<li>✅ Organized Structure - Files saved in separate folders (css, js, images)</li>
<li>✅ Automatic Path Management - Converts relative paths to absolute and updates them</li>
<li>✅ Multiple File Support - Supports PNG, JPG, GIF, SVG, WebP images, fonts, and more</li>
<li>✅ Simple Interface - Just enter the website URL and go!</li>
<li>✅ High Security - Browser simulation with proper User-Agent headers</li>
<li>✅ Error Handling - Displays download errors and continues the process</li>
<li>✅ Detailed Statistics - Shows count of downloaded files by type</li>
<li>✅ Timeout Management - Prevents hanging on slow connections</li>
<li>✅ UTF-8 Encoding - Proper character encoding for international websites</li>
</ul>
<h3>🔧 Installation</h3>
<h4>1. Clone the Repository</h4>
<code>git clone https://github.com/RezaHasanvand/website-downloader.git
cd website-downloader</code>
<h4>2. Install Dependencies</h4>
Using requirements.txt:
<code>pip install -r requirements.txt</code>
Or manually install:
<code>pip install requests beautifulsoup4 lxml</code>
<h4>3. Verify Installation</h4>
<h3>💻 Usage</h3>
<h4>Method 1: Command Line Interface (CLI)</h4>
The simplest way to use Website Downloader:
<code>python website_downloader.py</code>
Then follow the interactive prompts:
<code>🔗 Please enter the website URL (e.g., https://example.com): https://example.com
📁 Output folder name (default: downloaded_site): my_website</code>
<h4>Method 2: Python Script</h4>
Create a Python script and import the WebsiteDownloader class:
<code>from website_downloader import WebsiteDownloader

# Download a website with custom settings
downloader = WebsiteDownloader(
    url="https://example.com",
    output_dir="my_website"
)
downloader.download_website()</code>
<h4>Method 3: Advanced Configuration</h4>
<code>from website_downloader import WebsiteDownloader

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
downloader.download_website()</code>

<h2>👨‍💻 Author</h2>
Reza Hasanvand (رضا حسنوند)
<h3>Connect with Me</h3>
<ul>
<li>🌐 GitHub: github.com/rezahasanvand</li>
<li>📧 Email: hasanvand.reza72@gmail.com</li>
<li>💼 LinkedIn: linkedin.com/in/rezahasanvand</li>
</ul>
