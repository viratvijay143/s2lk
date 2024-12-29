from youtubesearchpython.__future__ import VideosSearch
from config import YOUTUBE_IMG_URL

# Assuming HTML code for rendering the UI (HTML part)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Thumbnail with Video Details</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
        }}

        /* Background image and blur */
        .background {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('{0}'); /* Replace with actual image URL */
            background-size: cover;
            background-position: center;
            filter: blur(8px); /* Background blur effect */
            z-index: -1;
        }}

        /* Box styling */
        .box {{
            position: absolute;
            width: 45%;
            height: 200px;
            top: 50%;
            transform: translateY(-50%);
            border-radius: 10px;
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black background */
            color: white;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}

        .box-left {{
            left: 5%;
        }}

        .box-right {{
            right: 5%;
        }}

        /* Styling for the video details */
        .video-details {{
            text-align: center;
        }}

        .video-title {{
            font-size: 20px;
            font-weight: bold;
        }}

        .video-description {{
            font-size: 14px;
            margin-top: 10px;
        }}

    </style>
</head>
<body>

<div class="background"></div>

<!-- Left Box -->
<div class="box box-left">
    <div class="video-details">
        <div class="video-title">{1}</div>
        <div class="video-description">{2}</div>
    </div>
</div>

<!-- Right Box -->
<div class="box box-right">
    <div class="video-details">
        <div class="video-title">{1}</div>
        <div class="video-description">{2}</div>
    </div>
</div>

</body>
</html>
"""

async def gen_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            title = result["title"]
            description = result["descriptionSnippet"]
            return generate_html(thumbnail, title, description)
    except Exception as e:
        return generate_html(YOUTUBE_IMG_URL, "Video Not Found", "No description available.")

async def gen_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            title = result["title"]
            description = result["descriptionSnippet"]
            return generate_html(thumbnail, title, description)
    except Exception as e:
        return generate_html(YOUTUBE_IMG_URL, "Video Not Found", "No description available.")

def generate_html(thumbnail, title, description):
    # Generating HTML with video details and background
    return html_template.format(thumbnail, title, description)
