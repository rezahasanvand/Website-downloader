<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website Downloader - README</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #f6f8fa;
            color: #24292e;
            line-height: 1.6;
            padding: 40px 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px 50px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }

        /* Headers */
        h1 {
            font-size: 32px;
            font-weight: 700;
            color: #24292e;
            border-bottom: 1px solid #e1e4e8;
            padding-bottom: 12px;
            margin-bottom: 24px;
        }

        h2 {
            font-size: 24px;
            font-weight: 600;
            margin-top: 32px;
            margin-bottom: 16px;
            color: #24292e;
        }

        h3 {
            font-size: 18px;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 12px;
            color: #24292e;
        }

        h4 {
            font-size: 16px;
            font-weight: 600;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #24292e;
        }

        /* Badges */
        .badges {
            text-align: center;
            margin: 20px 0 30px 0;
        }

        .badge {
            display: inline-block;
            background: #f1f8ff;
            color: #0366d6;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            margin: 4px 6px;
            border: 1px solid #0366d6;
        }

        .badge.green {
            background: #dcffe4;
            color: #22863a;
            border-color: #22863a;
        }

        .badge.orange {
            background: #ffd8b5;
            color: #b45a1c;
            border-color: #b45a1c;
        }

        .badge.yellow {
            background: #fff5b1;
            color: #735c0f;
            border-color: #735c0f;
        }

        .badge.red {
            background: #ffe1e1;
            color: #b31d28;
            border-color: #b31d28;
        }

        /* Text */
        p {
            margin-bottom: 16px;
        }

        a {
            color: #0366d6;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Lists */
        ul, ol {
            margin: 12px 0 20px 24px;
        }

        li {
            margin-bottom: 6px;
        }

        /* Code */
        code {
            background: #f6f8fa;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 14px;
            color: #24292e;
        }

        pre {
            background: #f6f8fa;
            padding: 16px 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 16px 0;
            border: 1px solid #e1e4e8;
        }

        pre code {
            background: transparent;
            padding: 0;
            border-radius: 0;
            color: #24292e;
            font-size: 14px;
            line-height: 1.5;
        }

        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0 24px 0;
        }

        table th {
            background: #f6f8fa;
            padding: 10px 16px;
            text-align: left;
            font-weight: 600;
            border: 1px solid #e1e4e8;
        }

        table td {
            padding: 10px 16px;
            border: 1px solid #e1e4e8;
        }

        /* Divider */
        hr {
            border: none;
            border-top: 1px solid #e1e4e8;
            margin: 32px 0;
        }

        /* Center */
        .text-center {
            text-align: center;
        }

        /* Author section */
        .author-section {
            background: #f6f8fa;
            padding: 24px;
            border-radius: 6px;
            margin: 24px 0;
            border: 1px solid #e1e4e8;
        }

        .author-section h3 {
            margin-top: 0;
        }

        .author-section ul {
            list-style: none;
            padding-left: 0;
            margin: 8px 0 0 0;
        }

        .author-section ul li {
            margin-bottom: 4px;
        }

        .author-section ul li a {
            color: #0366d6;
        }

        .author-section ul li a:hover {
            text-decoration: underline;
        }

        /* Feature grid */
        .feature-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 16px 0 24px 0;
        }

        .feature-item {
            background: #f8f9fa;
            padding: 12px 16px;
            border-radius: 6px;
            border: 1px solid #e1e4e8;
        }

        .feature-item strong {
            color: #24292e;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .container {
                padding: 24px 20px;
            }

            h1 {
                font-size: 26px;
            }

            h2 {
                font-size: 20px;
            }

            .feature-grid {
                grid-template-columns: 1fr;
            }

            table {
                font-size: 14px;
            }

            table th, table td {
                padding: 6px 10px;
            }
        }

        @media (max-width: 480px) {
            body {
                padding: 16px 10px;
            }

            .container {
                padding: 16px 14px;
            }

            .badge {
                font-size: 12px;
                padding: 2px 10px;
                margin: 2px 4px;
            }

            pre {
                padding: 10px 12px;
                font-size: 12px;
            }

            code {
                font-size: 12px;
            }
        }

        /* Print */
        @media print {
            body {
                background: white;
                padding: 20px;
            }

            .container {
                box-shadow: none;
                padding: 20px;
            }

            .badge {
                border: 1px solid #ccc;
            }

            .author-section {
                border: 1px solid #ccc;
            }
        }
    </style>
</head>
<body>

    <div class="container">

        <!-- Header -->
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="border-bottom: none; padding-bottom: 0; margin-bottom: 0;">🌐 Website Downloader</h1>
        </div>

        <!-- Badges -->
        <div class="badges">
            <span class="badge green">Python 3.7+</span>
            <span class="badge">MIT License</span>
            <span class="badge orange">Requests 2.28+</span>
            <span class="badge yellow">BeautifulSoup 4.11+</span>
            <span class="badge red">LXML 4.9+</span>
        </div>

        <p style="text-align: center; font-size: 18px; margin-bottom: 24px;">
            <strong>Download entire websites with one click!</strong>
        </p>

        <hr>

        <!-- Table of Contents -->
        <h2>📖 Table of Contents</h2>
        <ul>
            <li><a href="#features">Features</a></li>
            <li><a href="#prerequisites">Prerequisites</a></li>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#output-structure">Output Structure</a></li>
            <li><a href="#examples">Examples</a></li>
            <li><a href="#important-notes">Important Notes</a></li>
            <li><a href="#troubleshooting">Troubleshooting</a></li>
            <li><a href="#contributing">Contributing</a></li>
            <li><a href="#license">License</a></li>
            <li><a href="#author">Author</a></li>
        </ul>

        <hr>

        <!-- Features -->
        <h2 id="features">🚀 Features</h2>
        <p>
            <strong>Website Downloader</strong> is a powerful and simple tool for downloading entire websites.
            By entering a website URL, it downloads all resources including HTML, CSS, JavaScript, and images,
            and saves them in a structured format with separate folders.
        </p>

        <h3>✨ Key Features</h3>
        <div class="feature-grid">
            <div class="feature-item"><strong>✅ Complete Website Download</strong> — Downloads all HTML, CSS, JS, and image files</div>
            <div class="feature-item"><strong>📁 Organized Structure</strong> — Files saved in separate folders (css, js, images)</div>
            <div class="feature-item"><strong>🔄 Automatic Path Management</strong> — Converts relative paths to absolute and updates them</div>
            <div class="feature-item"><strong>📄 Multiple File Support</strong> — Supports PNG, JPG, GIF, SVG, WebP images, fonts, and more</div>
            <div class="feature-item"><strong>🎯 Simple Interface</strong> — Just enter the website URL and go!</div>
            <div class="feature-item"><strong>🛡️ High Security</strong> — Browser simulation with proper User-Agent headers</div>
            <div class="feature-item"><strong>⚠️ Error Handling</strong> — Displays download errors and continues the process</div>
            <div class="feature-item"><strong>📊 Detailed Statistics</strong> — Shows count of downloaded files by type</div>
        </div>

        <h3>🎯 What Can You Download?</h3>
        <ul>
            <li><strong>HTML Files</strong> — Main pages and subpages</li>
            <li><strong>CSS Stylesheets</strong> — All external and internal styles</li>
            <li><strong>JavaScript Files</strong> — All external scripts</li>
            <li><strong>Images</strong> — PNG, JPG, JPEG, GIF, SVG, WebP, BMP, ICO</li>
            <li><strong>Fonts</strong> — WOFF, WOFF2, TTF, OTF</li>
            <li><strong>Other Resources</strong> — JSON, XML, and other linked resources</li>
        </ul>

        <hr>

        <!-- Prerequisites -->
        <h2 id="prerequisites">📋 Prerequisites</h2>
        <p>Before you begin, ensure you have the following installed:</p>
        <ul>
            <li><strong>Python 3.7</strong> or higher</li>
            <li><strong>pip</strong> (Python package manager)</li>
            <li><strong>Internet connection</strong> (to download websites)</li>
        </ul>

        <h3>Check Python Version</h3>
        <pre><code>python --version
# or
python3 --version</code></pre>

        <hr>

        <!-- Installation -->
        <h2 id="installation">🔧 Installation</h2>

        <h3>1. Clone the Repository</h3>
        <pre><code>git clone https://github.com/RezaHasanvand/website-downloader.git
cd website-downloader</code></pre>

        <h3>2. Install Dependencies</h3>
        <p>Using <code>requirements.txt</code>:</p>
        <pre><code>pip install -r requirements.txt</code></pre>
        <p>Or manually install:</p>
        <pre><code>pip install requests beautifulsoup4 lxml</code></pre>

        <h3>3. Verify Installation</h3>
        <pre><code>python -c "import requests, bs4, lxml; print('✅ All dependencies installed successfully!')"</code></pre>

        <hr>

        <!-- Usage -->
        <h2 id="usage">💻 Usage</h2>

        <h3>Method 1: Command Line Interface (CLI)</h3>
        <p>The simplest way to use Website Downloader:</p>
        <pre><code>python website_downloader.py</code></pre>
        <p>Then follow the interactive prompts:</p>
        <pre><code>🔗 Please enter the website URL (e.g., https://example.com): https://example.com
📁 Output folder name (default: downloaded_site): my_website</code></pre>

        <h3>Method 2: Python Script</h3>
        <p>Create a Python script and import the <code>WebsiteDownloader</code> class:</p>
        <pre><code>from website_downloader import WebsiteDownloader

# Download a website with custom settings
downloader = WebsiteDownloader(
    url="https://example.com",
    output_dir="my_website"
)
downloader.download_website()</code></pre>

        <h3>Method 3: Advanced Configuration</h3>
        <pre><code>from website_downloader import WebsiteDownloader

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
downloader.download_website()</code></pre>

        <hr>

        <!-- Output Structure -->
        <h2 id="output-structure">📁 Output Structure</h2>
        <p>After successful download, the following structure is created:</p>
        <pre><code>my_website/                    # Root directory
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
    └── font.ttf</code></pre>

        <h3>File Organization Details</h3>
        <table>
            <thead>
                <tr>
                    <th>Folder</th>
                    <th>Description</th>
                    <th>File Types</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>css/</code></td>
                    <td>Stylesheet files</td>
                    <td>.css, .scss, .less</td>
                </tr>
                <tr>
                    <td><code>js/</code></td>
                    <td>JavaScript files</td>
                    <td>.js, .mjs, .cjs</td>
                </tr>
                <tr>
                    <td><code>images/</code></td>
                    <td>Image files</td>
                    <td>.png, .jpg, .jpeg, .gif, .svg, .webp, .ico, .bmp</td>
                </tr>
                <tr>
                    <td><code>fonts/</code></td>
                    <td>Font files</td>
                    <td>.woff, .woff2, .ttf, .otf, .eot</td>
                </tr>
            </tbody>
        </table>

        <hr>

        <!-- Examples -->
        <h2 id="examples">🎯 Examples</h2>

        <h3>Example 1: Download a Simple Website</h3>
        <pre><code>python website_downloader.py</code></pre>
        <p>Input:</p>
        <pre><code>🔗 URL: https://example.com
📁 Output folder: example_site</code></pre>
        <p>Output:</p>
        <pre><code>✅ Download complete!
📄 HTML file: index.html
📁 Folder: example_site
📊 Download Statistics:
   📄 HTML files: 1
   🎨 CSS files: 2
   📜 JS files: 3
   🖼️ Images: 5
   📁 Total files: 11</code></pre>

        <h3>Example 2: Download a Documentation Site</h3>
        <pre><code>from website_downloader import WebsiteDownloader

downloader = WebsiteDownloader(
    url="https://docs.python.org/3/",
    output_dir="python_docs"
)
downloader.download_website()</code></pre>

        <h3>Example 3: Bulk Download Multiple Sites</h3>
        <pre><code>from website_downloader import WebsiteDownloader

sites = [
    "https://example1.com",
    "https://example2.com",
    "https://example3.com"
]

for i, site in enumerate(sites):
    print(f"\n📥 Downloading site {i+1}/{len(sites)}: {site}")
    downloader = WebsiteDownloader(site, f"site_{i+1}")
    downloader.download_website()</code></pre>

        <h3>Example 4: Custom User-Agent</h3>
        <pre><code>from website_downloader import WebsiteDownloader

downloader = WebsiteDownloader("https://example.com", "custom_site")
downloader.session.headers.update({
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
})
downloader.download_website()</code></pre>

        <hr>

        <!-- Important Notes -->
        <h2 id="important-notes">⚠️ Important Notes</h2>

        <h3>🔒 Legal & Ethical Considerations</h3>
        <ol>
            <li><strong>Copyright</strong>: Only use this tool for websites you have permission to download. Respect copyright laws and terms of service.</li>
            <li><strong>Robots.txt</strong>: Always check the website's <code>robots.txt</code> file to ensure you're allowed to crawl the site.</li>
            <li><strong>Rate Limiting</strong>: Don't send too many requests too quickly. Be respectful of the website's resources.</li>
            <li><strong>Personal Use</strong>: This tool is intended for personal, educational, or archival purposes only.</li>
        </ol>

        <h3>🚫 Limitations</h3>
        <ol>
            <li><strong>Dynamic Websites</strong>: This tool is designed for static websites. For SPAs (React, Vue, Angular), you'll need more advanced tools like Puppeteer/Playwright, HTTrack, or custom scrapers.</li>
            <li><strong>Login-Protected Sites</strong>: This tool cannot download sites that require authentication.</li>
            <li><strong>Large Websites</strong>: For very large websites (1000+ pages), the process may be slow and resource-intensive.</li>
            <li><strong>Modern Web Technologies</strong>: Some advanced features (WebGL, WebAssembly, etc.) might not be fully supported.</li>
        </ol>

        <h3>💡 Best Practices</h3>
        <ul>
            <li><strong>Start Small</strong>: Test with simple websites first</li>
            <li><strong>Check Size</strong>: Some websites are very large (GBs) - be mindful of storage</li>
            <li><strong>Respect Resources</strong>: Use delay between requests if downloading many pages</li>
            <li><strong>Monitor Progress</strong>: Keep an eye on the download process</li>
        </ul>

        <hr>

        <!-- Troubleshooting -->
        <h2 id="troubleshooting">🔧 Troubleshooting</h2>

        <h3>Common Issues and Solutions</h3>
        <table>
            <thead>
                <tr>
                    <th>Issue</th>
                    <th>Solution</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Connection Error</strong></td>
                    <td>Check your internet connection and try again</td>
                </tr>
                <tr>
                    <td><strong>403 Forbidden</strong></td>
                    <td>The website may be blocking automated requests. Try using a different User-Agent</td>
                </tr>
                <tr>
                    <td><strong>Timeout Error</strong></td>
                    <td>Increase the timeout value in the code</td>
                </tr>
                <tr>
                    <td><strong>SSL Certificate Error</strong></td>
                    <td>Add <code>verify=False</code> to the request or update your SSL certificates</td>
                </tr>
                <tr>
                    <td><strong>Empty HTML</strong></td>
                    <td>The website might be using JavaScript. Try using a different tool</td>
                </tr>
                <tr>
                    <td><strong>Missing Resources</strong></td>
                    <td>Some resources might use relative paths incorrectly. Check the source code</td>
                </tr>
            </tbody>
        </table>

        <h3>Debug Mode</h3>
        <p>To enable debug logging, modify the code:</p>
        <pre><code>import logging
logging.basicConfig(level=logging.DEBUG)</code></pre>

        <h3>Increase Timeout</h3>
        <pre><code>response = self.session.get(full_url, timeout=30)  # 30 seconds instead of 10</code></pre>

        <h3>Custom Headers</h3>
        <pre><code>downloader.session.headers.update({
    'User-Agent': 'Your Custom User-Agent',
    'Referer': 'https://example.com',
    'Accept-Language': 'en-US,en;q=0.9'
})</code></pre>

        <hr>

        <!-- Contributing -->
        <h2 id="contributing">🤝 Contributing</h2>
        <p>Contributions are welcome! Here's how you can help:</p>

        <h3>🐛 Report Bugs</h3>
        <p>If you find a bug, please create an issue with:</p>
        <ul>
            <li>Description of the problem</li>
            <li>Steps to reproduce</li>
            <li>Expected vs actual behavior</li>
            <li>Screenshots if applicable</li>
        </ul>

        <h3>💡 Suggest Features</h3>
        <p>Have an idea for improvement? Open an issue with:</p>
        <ul>
            <li>Clear description of the feature</li>
            <li>Why it would be useful</li>
            <li>How it should work</li>
        </ul>

        <h3>📝 Submit Code</h3>
        <ol>
            <li>Fork the repository</li>
            <li>Create a feature branch:
                <pre><code>git checkout -b feature/amazing-feature</code></pre>
            </li>
            <li>Commit your changes:
                <pre><code>git commit -m 'Add amazing feature'</code></pre>
            </li>
            <li>Push to the branch:
                <pre><code>git push origin feature/amazing-feature</code></pre>
            </li>
            <li>Open a Pull Request</li>
        </ol>

        <h3>📚 Improve Documentation</h3>
        <ul>
            <li>Fix typos or grammar issues</li>
            <li>Add more examples</li>
            <li>Improve explanations</li>
            <li>Translate documentation</li>
        </ul>

        <hr>

        <!-- License -->
        <h2 id="license">📄 License</h2>
        <p>This project is licensed under the <strong>MIT License</strong>.</p>

        <h3>MIT License Summary</h3>
        <ul>
            <li>✅ <strong>Commercial use</strong>: You can use this code in commercial projects</li>
            <li>✅ <strong>Modification</strong>: You can modify the code</li>
            <li>✅ <strong>Distribution</strong>: You can distribute the code</li>
            <li>✅ <strong>Private use</strong>: You can use it privately</li>
            <li>⚠️ <strong>No warranty</strong>: The software is provided "as is" without warranty</li>
        </ul>

        <hr>

        <!-- Author -->
        <h2 id="author">👨‍💻 Author</h2>
        <div class="author-section">
            <h3>Reza Hasanvand (رضا حسنوند)</h3>
            <h4>Connect with Me</h4>
            <ul>
                <li>🌐 <strong>GitHub</strong>: <a href="https://github.com/RezaHasanvand" target="_blank">github.com/RezaHasanvand</a></li>
                <li>📧 <strong>Email</strong>: <a href="mailto:rezahasanvand75@gmail.com">rezahasanvand75@gmail.com</a></li>
                <li>💼 <strong>LinkedIn</strong>: <a href="https://linkedin.com/in/rezahasanvand" target="_blank">linkedin.com/in/rezahasanvand</a></li>
            </ul>
            <h4>Support My Work</h4>
            <p>If you find this tool useful, consider:</p>
            <ul>
                <li>⭐ Starring the repository</li>
                <li>🐛 Reporting issues</li>
                <li>📝 Contributing to the code</li>
                <li>🔗 Sharing with others</li>
            </ul>
        </div>

        <hr>

        <!-- Acknowledgments -->
        <h2 id="acknowledgments">🙏 Acknowledgments</h2>
        <p>Special thanks to these amazing open-source projects:</p>
        <table>
            <thead>
                <tr>
                    <th>Project</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><a href="https://docs.python-requests.org/" target="_blank">Requests</a></td>
                    <td>Elegant HTTP library for Python</td>
                </tr>
                <tr>
                    <td><a href="https://www.crummy.com/software/BeautifulSoup/" target="_blank">BeautifulSoup</a></td>
                    <td>HTML/XML parsing library</td>
                </tr>
                <tr>
                    <td><a href="https://lxml.de/" target="_blank">lxml</a></td>
                    <td>Fast HTML/XML processing</td>
                </tr>
                <tr>
                    <td><a href="https://www.python.org/" target="_blank">Python</a></td>
                    <td>The programming language</td>
                </tr>
            </tbody>
        </table>

        <hr>

        <!-- Project Statistics -->
        <h2 id="statistics">📊 Project Statistics</h2>
        <table>
            <thead>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Language</strong></td>
                    <td>Python 100%</td>
                </tr>
                <tr>
                    <td><strong>Lines of Code</strong></td>
                    <td>~300</td>
                </tr>
                <tr>
                    <td><strong>Dependencies</strong></td>
                    <td>3</td>
                </tr>
                <tr>
                    <td><strong>File Types Supported</strong></td>
                    <td>15+</td>
                </tr>
                <tr>
                    <td><strong>Time to Download</strong></td>
                    <td>Varies by site size</td>
                </tr>
            </tbody>
        </table>

        <hr>

        <!-- Changelog -->
        <h2 id="changelog">🔄 Changelog</h2>

        <h3>v1.0.0 (Current)</h3>
        <ul>
            <li>✅ Initial release</li>
            <li>✅ Full website download capability</li>
            <li>✅ CSS, JS, and image extraction</li>
            <li>✅ Automatic path management</li>
            <li>✅ Organized output structure</li>
        </ul>

        <h3>Planned Features (v2.0.0)</h3>
        <ul>
            <li>🔄 Recursive subpage downloading</li>
            <li>🔄 Multi-threading for faster downloads</li>
            <li>🔄 Support for SPA websites</li>
            <li>🔄 GUI interface</li>
            <li>🔄 Download progress bar</li>
            <li>🔄 Session persistence</li>
        </ul>

        <hr>

        <!-- Footer -->
        <div class="text-center" style="padding-top: 20px;">
            <p style="font-size: 16px;">
                <strong>⭐ If you like this project, please give it a star!</strong>
            </p>
            <p style="font-size: 14px; color: #586069;">
                Made with ❤️ by <strong>Reza Hasanvand</strong>
            </p>
            <p style="font-size: 12px; color: #586069; margin-top: 8px;">
                <a href="#top">⬆ Back to Top</a>
            </p>
        </div>

    </div>

</body>
</html>
