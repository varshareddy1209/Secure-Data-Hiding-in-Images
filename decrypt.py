import cv2
import numpy as np

def decrypt_message():
    img = cv2.imread("encryptedImage.png", cv2.IMREAD_UNCHANGED)  # Read image

    with open("key.txt", "r") as key_file:
        stored_password = key_file.readline().strip()
        message_length = int(key_file.readline().strip())  # Read stored message length

    entered_password = input("🔑 Enter password to decrypt: ")

    if entered_password != stored_password:
        print("\n❌ Invalid password!")
        return

    # Flatten the image to extract message
    flat_img = img.flatten()

    # Extract the first `message_length` values
    message_chars = [chr(value) for value in flat_img[:message_length]]

    decrypted_message = "".join(message_chars).strip()

    # Stop at the end marker
    if "<<<END>>>" in decrypted_message:
        decrypted_message = decrypted_message.replace("<<<END>>>", "")

    print("\n✅ Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    decrypt_message()
