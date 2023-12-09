""" Generate image links for README.md. """

import os


def generate_image_links(img_directory):
    image_files = [f for f in os.listdir(img_directory) if f.endswith(".png")]
    image_links = [
        f"![{os.path.splitext(f)[0]}]({os.path.join('img', f)})" for f in image_files]
    return image_links


def update_readme(readme_path, image_links):
    with open(readme_path, 'r', encoding='utf-8') as readme_file:
        readme_content = readme_file.read()
    insert_position = readme_content.find(
        "## Imágenes generadas a partir de PDFs")
    updated_readme_content = (
        readme_content[:insert_position] +
        '\n'.join(image_links) +
        readme_content[insert_position:]
    )
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(updated_readme_content)


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    img_directory = os.path.join(script_directory, "img")
    readme_path = os.path.join(script_directory, "README.md")
    image_links = generate_image_links(img_directory)
    update_readme(readme_path, image_links)
