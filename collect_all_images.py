import os
import face_recognition
import shutil 


# Example usage
#image_folder = ""
#reference_image = ""
#output_folder = ""

TOLERANCE = 0.6


def find_matching_faces(image_folder, reference_image_path, output_folder):
    """
    Iterates through images in a folder, compares each face to a reference image, 
    and copies matching images to a new folder.
    
    Args:
        image_folder (str): Path to the folder containing images to check.
        reference_image_path (str): Path to the reference image for comparison.
        output_folder (str): Path to the folder where matching images will be copied. 
    """
    
    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)[0]
    # Count for each image processed
    image_count = 0

    for filename in os.listdir(image_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            # Increment the image count
            image_count += 1
            print(f"{filename} is the {image_count} file")
            # Load the image
            image_path = os.path.join(image_folder, filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)
            # Check if any faces are found
            if face_encodings:
                for encoding in face_encodings:
                    match = face_recognition.compare_faces([reference_encoding], encoding, tolerance=TOLERANCE)
                    # If a match is found, copy the image to the output folder
                    if match[0]: 
                        new_path = os.path.join(output_folder, filename)
                        shutil.copy(image_path, new_path)
                        print(f"Copied: {filename} to {output_folder}")
                        break
            


#find_matching_faces(image_folder, reference_image, output_folder)