import ffmpeg
import os

def extract_frames_ffmpeg():
    video_path = r"F:\ai_vedio_dataset\real_2500"
    output_folder = r"F:\ai_video_frames\real_2500"
    fps = 16

    os.makedirs(output_folder, exist_ok=True)
    output_pattern = os.path.join(output_folder, "frame_%04d.jpg")

    (
        ffmpeg
        .input(video_path)
        .output(output_pattern, r=fps, loglevel="quiet")
        .run()
    )

    print(f"[✓] Extracted frames to: {output_folder}")
