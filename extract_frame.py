import cv2

def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Frame counter
    frame_count = 0
    
    # Loop through all frames
    while True:
        # Read a frame
        ret, frame = cap.read()
        
        # If frame reading was unsuccessful, break the loop
        if not ret:
            break
        
        # Save every 10th frame
        if frame_count % 10 == 0:
            output_path = f"{output_folder}/frame_{frame_count}.jpg"
            cv2.imwrite(output_path, frame)
        
        # Increment frame count
        frame_count += 1
    
    # Release the video capture object
    cap.release()

# Main function
def main():
    # Video file path
    video_path = "video\change_line.mp4"
    # Output folder path
    output_folder = "video2frames"
    
    # Extract frames from the video
    extract_frames(video_path, output_folder)

if __name__ == "__main__":
    main()
