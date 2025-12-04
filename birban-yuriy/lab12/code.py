class MediaPlayer:
    def play(self, audio):
        return f"Граю аудіо: {audio}"

class VideoPlayer:
    def play_video(self, video):
        return f"Граю відео: {video}"

class VideoAdapter(MediaPlayer):
    def __init__(self, video_player):
        self.video_player = video_player

    def play(self, video):
        return self.video_player.play_video(video)

player = VideoAdapter(VideoPlayer())
print(player.play("film.mp4"))