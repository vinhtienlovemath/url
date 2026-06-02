import json
import os
import shutil

DATA_FILE = 'links.json'
TEMPLATE_FILE = 'template.html'
ADMIN_FILE = 'admin.html' 
OUTPUT_DIR = 'public'

def main():
    # 1. Dọn dẹp thư mục cũ
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # 2. Đọc dữ liệu
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        links = json.load(f)
    
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    # 3. Tạo trang chủ
    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write("<h1>Hệ thống Rút gọn URL</h1><p>Liên hệ Admin.</p>")

    if os.path.exists(ADMIN_FILE):
        shutil.copy(ADMIN_FILE, os.path.join(OUTPUT_DIR, ADMIN_FILE))
        print(f"Đã copy {ADMIN_FILE} sang {OUTPUT_DIR}/")

    # 4. Tạo từng folder link
    print(f"Đang xử lý {len(links)} liên kết...")
    for slug, url in links.items():
        safe_slug = "".join([c for c in slug if c.isalnum() or c in "-_"])
        link_dir = os.path.join(OUTPUT_DIR, safe_slug)
        os.makedirs(link_dir, exist_ok=True)
        html_content = template.replace('{{TARGET_URL}}', url)
        
        with open(os.path.join(link_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
            
    print("Build thành công!")

if __name__ == "__main__":
    main()