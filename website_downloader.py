# ============================================================
# website_downloader.py
# Download full website and save files seperetly
# ============================================================

import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import os
import re
from pathlib import Path
import time

class WebsiteDownloader:
    """
   class for full download of website
    """
    
    def __init__(self, url, output_dir="downloaded_site"):
        """
       class creator
        
        Args:
            url (str): Your website address
            output_dir (str): Output folder name
        """
        self.base_url = url
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Create output folder
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        
        # Seperate folder for files
        self.css_dir = os.path.join(output_dir, "css")
        self.js_dir = os.path.join(output_dir, "js")
        self.images_dir = os.path.join(output_dir, "images")
        
        Path(self.css_dir).mkdir(parents=True, exist_ok=True)
        Path(self.js_dir).mkdir(parents=True, exist_ok=True)
        Path(self.images_dir).mkdir(parents=True, exist_ok=True)
        
        # Saving contents
        self.html_content = ""
        self.css_files = {}
        self.js_files = {}
        self.image_files = {}
        self.other_files = {}
        
        print(f"🌐 Ready for download: {self.base_url}")
        print(f"📁 Output folder: {self.output_dir}")
        print("=" * 60)
    
    def download_file(self, url, file_type="other"):
        """
       Downloading files from address
        
        Args:
            url (str): File address
            file_type (str): File type (css, js, image, other)
            
        Returns:
            tuple: (success, content, filename)
        """
        try:
            # Converting relative addresses to absolute addresses
            full_url = urljoin(self.base_url, url)
            
            # Retrieve content
            response = self.session.get(full_url, timeout=10)
            response.raise_for_status()
            
            # Extracting the file name
            parsed_url = urlparse(full_url)
            filename = os.path.basename(parsed_url.path)
            
            if not filename:
                filename = f"{file_type}_{int(time.time())}.{file_type}"
            
            # If the file does not have an extension, add it by type.
            if '.' not in filename:
                if file_type == "css":
                    filename += ".css"
                elif file_type == "js":
                    filename += ".js"
                elif file_type == "image":
                    # Type detection from content
                    content_type = response.headers.get('content-type', '')
                    if 'png' in content_type:
                        filename += ".png"
                    elif 'jpeg' in content_type or 'jpg' in content_type:
                        filename += ".jpg"
                    elif 'gif' in content_type:
                        filename += ".gif"
                    elif 'svg' in content_type:
                        filename += ".svg"
                    else:
                        filename += ".bin"
            
            # File name sanitization
            filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
            
            return True, response.content, filename
            
        except Exception as e:
            print(f"⚠️ Download Failed{url}: {str(e)[:50]}")
            return False, None, None
    
    def download_css(self, css_url):
        """
       Download CSS file
        
        Args:
            css_url (str): Download CSS file
            
        Returns:
            str: Saved file name or None
        """
        success, content, filename = self.download_file(css_url, "css")
        
        if success and content:
            filepath = os.path.join(self.css_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(content)
            
            self.css_files[css_url] = filename
            print(f"✅ Download CSS: {filename}")
            return filename
        
        return None
    
    def download_js(self, js_url):
        """
       Download JavaScript file
        
        Args:
            js_url (str): JS file path
            
        Returns:
            str: Saved file name or None
        """
        success, content, filename = self.download_file(js_url, "js")
        
        if success and content:
            filepath = os.path.join(self.js_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(content)
            
            self.js_files[js_url] = filename
            print(f"✅ Download JS: {filename}")
            return filename
        
        return None
    
    def download_image(self, img_url):
        """
       Download image file
        
        Args:
            img_url (str): Image URL
            
        Returns:
            str: Saved file name or None
        """
        success, content, filename = self.download_file(img_url, "image")
        
        if success and content:
            filepath = os.path.join(self.images_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(content)
            
            self.image_files[img_url] = filename
            print(f"✅ Download image: {filename}")
            return filename
        
        return None
    
    def process_html(self, html_content):
        """
       HTML Processing and Resource Extraction
        
        Args:
            html_content (str): HTML Content
            
        Returns:
            str: Modified HTML with local paths
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # ==========CSS Processing ==========
        # لینک‌های CSS
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                filename = self.download_css(href)
                if filename:
                    link['href'] = f"css/{filename}"
        
        # Inline styles (for subsequent extraction)
        
        # ========== JavaScript Processing ==========
        # External scripts
        for script in soup.find_all('script', src=True):
            src = script.get('src')
            if src:
                # If the script is external
                if not src.startswith('data:') and not src.startswith('blob:'):
                    filename = self.download_js(src)
                    if filename:
                        script['src'] = f"js/{filename}"
        
        # ========== Image Processing==========
        # Images in the img tag
        for img in soup.find_all('img', src=True):
            src = img.get('src')
            if src and not src.startswith('data:'):
                filename = self.download_image(src)
                if filename:
                    img['src'] = f"images/{filename}"
        
        # Images in CSS background (for subsequent processing)
        
        # ========== Font processing==========
        # Google Fonts and other services
        for link in soup.find_all('link', href=True):
            href = link.get('href')
            if 'fonts.googleapis.com' in href or 'fonts.gstatic.com' in href:
                # It is usually not possible to download the fonts.
                # But we can keep the link.
                pass
        
        return str(soup)
    
    def download_website(self):
        """
       Download the entire site
        """
        print("🔄 Download started...")
        print("-" * 60)
        
        try:
            # Download Home Page
            response = self.session.get(self.base_url, timeout=10)
            response.raise_for_status()
            
            # Encoding detection
            if response.encoding:
                html_content = response.text
            else:
                html_content = response.content.decode('utf-8', errors='ignore')
            
            # HTML Processing
            processed_html = self.process_html(html_content)
            
            # Save the original HTML file
            html_file = os.path.join(self.output_dir, "index.html")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(processed_html)
            
            print("-" * 60)
            print("✅ Download complete!")
            print(f"📄 HTML file: index.html")
            print(f"📁 Folder: {self.output_dir}")
            print("=" * 60)
            
            # Show statistics
            print("\n📊 Download statistics:")
            print(f"   📄 HTML files: 1")
            print(f"   🎨 CSS files: {len(self.css_files)}")
            print(f"   📜 JS files: {len(self.js_files)}")
            print(f"   🖼️  Images: {len(self.image_files)}")
            print(f"   📁 Total files: {1 + len(self.css_files) + len(self.js_files) + len(self.image_files)}")
            
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Download error: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False


def main():
    """
   Main function
    """
    print("=" * 60)
    print("🌐 Website Downloader - Download the entire site")
    print("Created BY Reza Hasanvand")
    print("=" * 60)
    
    # Get address from the user
    url = input("\n🔗 Please enter the website address (example: https://example.com): ").strip()
    
    if not url:
        print("❌ Address not entered!")
        return
    
    # If the address does not start with http, add it.
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Get output folder name
    output_dir = input("📁 Output folder name (default: downloaded_site): ").strip()
    if not output_dir:
        output_dir = "downloaded_site"
    
    print("\n" + "=" * 60)
    
    # Download
    downloader = WebsiteDownloader(url, output_dir)
    success = downloader.download_website()
    
    if success:
        print("\n🎉 Download completed successfully!")
        print(f"📂 Files in the folder: {output_dir}")
        print("\n💡To view the site, open the index.html file in your browser.")
    else:
        print("\n❌ The download failed. Please check the address.")


if __name__ == "__main__":
    main()