import subprocess

def sign_pdf(pdf_file, private_key_file, output_sig):
    cmd = [
        "gpg", "--output", output_sig, "--detach-sign",
        "--default-key", private_key_file, pdf_file
    ]
    subprocess.run(cmd)
