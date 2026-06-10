from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):

    api = YouTubeTranscriptApi()

    languages = [
        "en",
        "hi",
        "en-US",
        "en-GB"
    ]

    transcript = api.fetch(
        video_id,
        languages=languages
    )

    return " ".join(
        snippet.text
        for snippet in transcript
    )