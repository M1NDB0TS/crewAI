import os

# Assuming the Markdown content is stored in a variable named `markdown_content`
markdown_content = """
# Venues in Roseburg, Oregon

## Venue 1:
- Name: The Event Center at Umpqua Valley
- Address: 3452 E Evans Creek Rd, Roseburg, OR 97471
- Contact: (541) 672-0800
- Website: http://www.theeventcenteroregon.com/

## Venue 2:
- Name: Roseburg National Guard Armory
- Address: 3215 W Gardner St, Roseburg, OR 97471
- Contact: (541) 672-4870
- Website: https://www.ornga.org/

## Venue 3:
- Name: The Venue at the Ranch
- Address: 3554 W Gardner St, Roseburg, OR 97471
- Contact: (541) 608-2284
- Website: https://www.facebook.com/TheVenueAtTheRanch/
"""

# Specify the path where the Markdown file should be saved
output_dir = "Z:\\GIT\\crewAI\\out"  # Ensure this directory exists
output_file_path = os.path.join(output_dir, "venues_in_roseburg.md")

# Write the Markdown content to the file
try:
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    logger.info(f"Markdown file successfully generated at: {output_file_path}")
except Exception as e:
    logger.error(f"An error occurred during Markdown file generation: {e}")
