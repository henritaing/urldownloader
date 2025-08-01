import re

def clean_filename(title, author):
    """Sanitize the filename to 'Title - Author.mp3' without illegal characters."""
    def sanitize(s):
        return re.sub(r'[\\/*?:"<>|]', "", s)
    
    return sanitize(f"{title} - {author}.mp3")
