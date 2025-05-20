import markdown
import os
import webbrowser
import time

def show_title():
    print("="*60)
    print("📝  MARKDOWN TO HTML CONVERTER TOOL")
    print("="*60)
    print("📄 Description:")
    print("    This tool converts your Markdown (.md) files into clean,")
    print("    browser-viewable HTML (.html) files with one simple step.")
    print("\n📌 Instructions:")
    print("    - Enter a full file name like 'sample.md' or full path.")
    print("    - You can also convert ALL markdown files in a folder.")
    print("    - The converted HTML file will open automatically.\n")

def convert_markdown_to_html(md_path):
    try:
        print(f"\n🔄 Converting: {md_path}")
        time.sleep(1)  # Simulate loading
        with open(md_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])

        full_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Converted Markdown</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                code {{ background-color: #f4f4f4; padding: 2px 4px; }}
                pre {{ background-color: #f4f4f4; padding: 10px; overflow-x: auto; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        html_path = os.path.splitext(md_path)[0] + ".html"
        with open(html_path, 'w', encoding='utf-8') as html_file:
            html_file.write(full_html)

        time.sleep(1)  # Brief pause before confirming
        print(f"✅ Conversion successful! HTML saved as: {html_path}")
        print("🌐 Opening in your browser...")
        time.sleep(1)
        webbrowser.open('file://' + os.path.realpath(html_path))

    except Exception as e:
        print(f"❌ Failed to convert {md_path}: {str(e)}")

def convert_single_file():
    file_path = input("Enter the Markdown file name (e.g., `sample.md`): ").strip()
    if not file_path.endswith(".md"):
        print("⚠️  Only `.md` files are supported.")
        return
    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return
    convert_markdown_to_html(file_path)

def convert_multiple_files():
    file_list = input("Enter Markdown file names separated by commas: ").split(',')
    file_list = [file.strip() for file in file_list if file.strip().endswith('.md')]

    if not file_list:
        print("⚠️  No valid `.md` files provided.")
        return

    for file_path in file_list:
        if os.path.exists(file_path):
            convert_markdown_to_html(file_path)
        else:
            print(f"❌ File not found: {file_path}")

def convert_folder():
    folder_path = input("Enter the folder path containing Markdown files: ").strip()
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
        return

    md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]

    if not md_files:
        print("⚠️  No Markdown files found in this folder.")
        return

    for md_file in md_files:
        full_path = os.path.join(folder_path, md_file)
        convert_markdown_to_html(full_path)

def main():
    show_title()
    print("Select Mode:")
    print("1. Convert a single Markdown file")
    print("2. Convert multiple Markdown files (comma-separated)")
    print("3. Convert all `.md` files in a folder")
    
    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        convert_single_file()
    elif choice == "2":
        convert_multiple_files()
    elif choice == "3":
        convert_folder()
    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
