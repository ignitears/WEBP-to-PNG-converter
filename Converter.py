import os
import sys
import subprocess

# Try importing Pillow; install automatically if missing
try:
    from PIL import Image
except ImportError:
    print("Installing Pillow (image library)...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image

def convert_webp_to_png():
    folder = os.path.dirname(os.path.abspath(sys.argv[0]))
    output_folder = os.path.join(folder, "converted_pngs")
    os.makedirs(output_folder, exist_ok=True)

    webp_files = [f for f in os.listdir(folder) if f.lower().endswith(".webp")]

    if not webp_files:
        print("No .webp files found in this folder.")
        input("Press Enter to exit...")
        return

    for file_name in webp_files:
        src = os.path.join(folder, file_name)
        dst = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".png")
        try:
            with Image.open(src) as img:
                img.save(dst, "PNG")
            print(f" {file_name} → {os.path.basename(dst)}")
        except Exception as e:
            print(f" Error converting {file_name}: {e}")

    print(f"\nAll done! PNG files saved in: {output_folder}")
    input("Press Enter to close...")

if __name__ == "__main__":
    convert_webp_to_png()
