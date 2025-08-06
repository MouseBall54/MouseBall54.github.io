
import os
import re

def add_front_matter_to_posts(post_directory):
    en_dir = os.path.join(post_directory, 'en')
    ko_dir = os.path.join(post_directory, 'ko')

    if not os.path.isdir(en_dir) or not os.path.isdir(ko_dir):
        print("Error: 'en' or 'ko' directory not found in the specified path.")
        return

    en_posts = {os.path.splitext(f)[0]: os.path.join(en_dir, f) for f in os.listdir(en_dir) if f.endswith('.md')}
    ko_posts = {os.path.splitext(f)[0]: os.path.join(ko_dir, f) for f in os.listdir(ko_dir) if f.endswith('.md')}

    for name, en_path in en_posts.items():
        if name in ko_posts:
            ko_path = ko_posts[name]
            translation_id = name.split('-', 3)[-1] # Extract translation_id from filename

            # Process English post
            add_front_matter(en_path, 'en', translation_id)
            print(f"Updated English post: {en_path}")

            # Process Korean post
            add_front_matter(ko_path, 'ko', translation_id)
            print(f"Updated Korean post: {ko_path}")

def add_front_matter(filepath, lang, translation_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if fields already exist
    if re.search(r'^lang:\s*\w+\s*$', content, re.MULTILINE) and re.search(r'^translation_id:\s*[\w-]+\s*$', content, re.MULTILINE):
        print(f"Skipping {filepath}, front matter already exists.")
        return
    
    # Add lang and translation_id after the date line
    new_content = re.sub(r'(date: .*)', f'''\1
lang: {lang}
translation_id: {translation_id}''', content, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    posts_directory = '_posts'
    add_front_matter_to_posts(posts_directory)
    print("\nAll matching posts have been updated.")
