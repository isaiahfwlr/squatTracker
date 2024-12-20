import cv2

Load the video
video_path = 'MASON.mp4'  # Corrected file path
cap = cv2.VideoCapture(video_path)

Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file. Please check the path.")
    exit()

Play the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:  # Stop if the video ends
        print("Video playback finished.")
        break

    cv2.imshow('MASON.mp4', frame)  # Show the video frame
    if cv2.waitKey(10) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
