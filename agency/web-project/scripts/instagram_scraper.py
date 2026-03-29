#!/usr/bin/env python3
"""
Instagram Scraper for @entradados_estudio78
Downloads photos to ~/AutonomousSystem/agency/web-project/images/instagram/

Usage:
    python3 instagram_scraper.py
"""

import os
import sys
import logging
from datetime import datetime

# Setup instaloader
import instaloader

# Configuration
USERNAME = "entramados_estudio78"
OUTPUT_DIR = os.path.expanduser("~/AutonomousSystem/agency/web-project/images/instagram")

# Setup logging
log_file = os.path.join(OUTPUT_DIR, "scraper_log.txt")
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def download_instagramPhotos():
    """Download all photos from Instagram profile"""
    
    logger.info(f"🚀 Starting Instagram scraper for @{USERNAME}")
    logger.info(f"📁 Output directory: {OUTPUT_DIR}")
    
    # Create instaloader instance
    L = instaloader.Instaloader(
        download_pictures=True,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
        quiet=False
    )
    
    try:
        # Load session if exists, otherwise try anonymous
        session_file = os.path.join(OUTPUT_DIR, "session")
        
        # Try to login (requires credentials)
        # For now, try to download profile pictures only (public)
        logger.info(f"📥 Downloading profile pictures and posts from @{USERNAME}...")
        
        # Get profile
        profile = instaloader.Profile.from_username(L.context, USERNAME)
        
        logger.info(f"👤 Profile: {profile.full_name}")
        logger.info(f"📊 Posts: {profile.mediacount}")
        logger.info(f"📝 Bio: {profile.biography}")
        
        # Count downloads
        downloaded = 0
        failed = 0
        
        # Download profile picture
        logger.info("📸 Downloading profile picture...")
        try:
            L.download_profilepic(profile)
            downloaded += 1
        except Exception as e:
            logger.error(f"❌ Failed to download profile pic: {e}")
        
        # Download posts
        logger.info(f"📥 Downloading {profile.mediacount} posts...")
        
        for i, post in enumerate(profile.get_posts()):
            try:
                post_shortcode = post.shortcode
                post_date = post.date_utc.strftime("%Y%m%d")
                existing_files = [f for f in os.listdir(OUTPUT_DIR) if post_shortcode in f]
                
                if existing_files:
                    logger.info(f"  ⏭️  Post {post_shortcode} already downloaded, skipping")
                    continue
                
                logger.info(f"  📥 [{i+1}/{profile.mediacount}] Downloading {post_shortcode}...")
                L.download_post(post, target=f"post_{post_shortcode}")
                downloaded += 1
                
            except Exception as e:
                logger.error(f"  ❌ Failed to download post: {e}")
                failed += 1
                continue
        
        # Summary
        logger.info("=" * 50)
        logger.info(f"✅ DOWNLOAD COMPLETE")
        logger.info(f"   Downloaded: {downloaded}")
        logger.info(f"   Failed: {failed}")
        logger.info(f"   Output: {OUTPUT_DIR}")
        logger.info("=" * 50)
        
        # List downloaded files
        files = [f for f in os.listdir(OUTPUT_DIR) if os.path.isfile(os.path.join(OUTPUT_DIR, f))]
        logger.info(f"📁 Total files in directory: {len(files)}")
        
        return True
        
    except instaloader.exceptions.InstaloaderException as e:
        logger.error(f"❌ Instaloader error: {e}")
        
        # Try alternative method - just download profile
        logger.info("🔄 Trying alternative method...")
        try:
            L = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(L.context, USERNAME)
            L.download_profilepic(profile)
            logger.info("✅ Profile picture downloaded")
            return True
        except Exception as e2:
            logger.error(f"❌ Alternative method also failed: {e2}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════╗
║     📸 Instagram Photo Scraper                     ║
║     Profile: @entramados_estudio78                 ║
╚════════════════════════════════════════════════════╝
    """)
    
    success = download_instagramPhotos()
    
    if success:
        print("\n✅ Scraping completed!")
    else:
        print("\n⚠️ Scraping completed with errors. Check log for details.")
    
    sys.exit(0 if success else 1)
