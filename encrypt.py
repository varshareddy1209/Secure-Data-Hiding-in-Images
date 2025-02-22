import cv2
import numpy as np

def encrypt_message(message, password, output_path="encryptedImage.png"):
    img = cv2.imread("mypic.jpg", cv2.IMREAD_UNCHANGED)  # Read the image
    rows, cols, _ = img.shape  # Get image dimensions

    # Ensure the message fits in the image
    if len(message) + 7 > rows * cols:  # +7 for <<<END>>>
        print("\n❌ Error: Message too long for the image size!")
        return

    message += "<<<END>>>"  # Add an end marker to detect message end

    ascii_values = np.array([ord(char) for char in message], dtype=np.uint8)  # Convert to ASCII values

    # Flatten the image array
    flat_img = img.flatten()
    
    # Store message in first N pixels
    flat_img[:len(ascii_values)] = ascii_values

    # Reshape back to original image shape
    img = flat_img.reshape(rows, cols, -1)

    cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save without compression

    # Save password and message length
    with open("key.txt", "w") as key_file:
        key_file.write(f"{password}\n{len(ascii_values)}")

    print("\n✅ Message Encrypted Successfully!")

if __name__ == "__main__":
    msg = input("\n📝 Enter the secret message: ")
    pwd = input("🔑 Enter a password: ")

    encrypt_message(msg, pwd)
