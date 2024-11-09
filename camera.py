import cv2
from get_gpt_request import interpret_image

def capture_image():
    # Initialize the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    image_path='captured_image.jpg'
    # Check if the camera is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
    else:
        print("Press 's' to capture a photo and 'q' to quit.")
        
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If frame is read correctly, ret is True
            if not ret:
                print("Error: Failed to capture image.")
                break

            # Display the resulting frame
            cv2.imshow('Press s to save image, q to quit', frame)

            # Wait for user input to save or quit
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('s'):  # Press 's' to save the image
                cv2.imwrite('captured_image.jpg', frame)
                print("Image saved as 'captured_image.jpg'.")
                interpret_image(image_path)

            elif key == ord('q'):  # Press 'q' to quit
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

        return image_path

capture_image()