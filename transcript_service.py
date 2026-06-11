from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):
    print("FETCHING:", video_id)

    try:
        transcript = YouTubeTranscriptApi().fetch(
            video_id,
            languages=["hi", "en"]
        )

        text = " ".join(
            snippet.text
            for snippet in transcript
        )

        print("TRANSCRIPT FOUND:", len(text))

        return text

    except Exception as e:
        print("TRANSCRIPT ERROR:", e)
        return None