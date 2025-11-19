from PyPDF2 import PdfReader, PdfWriter
import os


def encrypt_pdf():
    """
    Encrypts a PDF file with a password using PyPDF2 library.
    Creates a new encrypted PDF file while preserving the original.
    """
    print("\n=== PDF Encryption ===")

    # Get file path with validation
    while True:
        file_path = input("Enter the path to the PDF file to encrypt: ").strip()
        if not file_path:
            print("Error: File path cannot be empty. Please try again.")
            continue
        if not os.path.exists(file_path):
            print("Error: File not found. Please check the path and try again.")
            continue
        if not file_path.lower().endswith('.pdf'):
            print("Error: Please provide a PDF file (.pdf extension).")
            continue
        break

    # Get password with validation
    while True:
        password = input("Enter encryption password: ").strip()
        if not password:
            print("Error: Password cannot be empty. Please try again.")
            continue
        if len(password) < 3:
            print("Error: Password must be at least 3 characters long.")
            continue
        break

    # Get output filename with validation
    while True:
        encrypted_file_name = input("Enter name for the encrypted file (without extension): ").strip()
        if not encrypted_file_name:
            print("Error: File name cannot be empty. Please try again.")
            continue
        # Ensure the filename has .pdf extension
        if not encrypted_file_name.lower().endswith('.pdf'):
            encrypted_file_name += '.pdf'
        break

    # Initialize PDF writer
    pdf_writer = PdfWriter()

    try:
        # Read the original PDF file
        pdf_reader = PdfReader(file_path)

        # Add all pages from original PDF to the writer
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Encrypt the PDF with the provided password
        pdf_writer.encrypt(password)

        # Save the encrypted PDF
        with open(encrypted_file_name, "wb") as output_file:
            pdf_writer.write(output_file)

        print(f"\n✅ Success! Encrypted file '{encrypted_file_name}' created with password protection.")

    except Exception as e:
        print(f"\n❌ Error during encryption: {e}")


def decrypt_pdf():
    """
    Decrypts a password-protected PDF file using PyPDF2 library.
    Creates a new decrypted PDF file without password protection.
    """
    print("\n=== PDF Decryption ===")

    # Get file path with validation
    while True:
        file_path = input("Enter the path to the encrypted PDF file: ").strip()
        if not file_path:
            print("Error: File path cannot be empty. Please try again.")
            continue
        if not os.path.exists(file_path):
            print("Error: File not found. Please check the path and try again.")
            continue
        break

    # Get password
    password = input("Enter the decryption password: ").strip()

    # Get output filename with validation
    while True:
        decrypted_file_name = input("Enter name for the decrypted file (without extension): ").strip()
        if not decrypted_file_name:
            print("Error: File name cannot be empty. Please try again.")
            continue
        # Ensure the filename has .pdf extension
        if not decrypted_file_name.lower().endswith('.pdf'):
            decrypted_file_name += '.pdf'

        # Warn if file already exists
        if os.path.exists(decrypted_file_name):
            overwrite = input(f"Warning: '{decrypted_file_name}' already exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != 'y':
                continue
        break

    # Initialize PDF writer
    pdf_writer = PdfWriter()

    try:
        # Read the encrypted PDF file
        pdf_reader = PdfReader(file_path)

        # Check if file is encrypted
        if pdf_reader.is_encrypted:
            # Attempt to decrypt with provided password
            decrypt_success = pdf_reader.decrypt(password)
            if not decrypt_success:
                print("\n❌ Error: Incorrect password or unable to decrypt the file.")
                return

        # Add all pages to the writer
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Save the decrypted PDF
        with open(decrypted_file_name, "wb") as output_file:
            pdf_writer.write(output_file)

        print(f"\n✅ Success! File decrypted and saved as '{decrypted_file_name}'")

    except Exception as e:
        print(f"\n❌ Error during decryption: {e}")


def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n" + "=" * 50)
    print("          PDF ENCRYPTION/DECRYPTION TOOL")
    print("=" * 50)
    print("1. Encrypt PDF (Add password protection)")
    print("2. Decrypt PDF (Remove password protection)")
    print("3. Exit")
    print("=" * 50)


def main():
    """
    Main function that runs the PDF encryption/decryption tool.
    Provides a user-friendly menu interface for operations.
    """
    print("Welcome to the PDF Security Tool!")

    while True:
        display_menu()

        choice = input("\nPlease choose an option (1-3): ").strip()

        if choice == '1':
            encrypt_pdf()
        elif choice == '2':
            decrypt_pdf()
        elif choice == '3':
            print("\nThank you for using the PDF Security Tool. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")

        # Ask if user wants to continue
        if choice in ['1', '2']:
            continue_choice = input("\nWould you like to perform another operation? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("\nThank you for using the PDF Security Tool. Goodbye!")
                break


if __name__ == "__main__":
    main()