import subprocess
import request
import creates3

def run_codeindex():
    """Run the codeindex.py script to fetch and save HTML content."""
    try:
        subprocess.run(['python', 'codeindex.py'], check=True)
        print("Successfully executed codeindex.py")
    except subprocess.CalledProcessError as e:
        print(f'Error running codeindex.py: {e}')

def run_final():
    """Run the final.py script to upload the HTML content to S3."""
    try:
        subprocess.run(['python', 'final.py'], check=True)
        print("Successfully executed final.py")
    except subprocess.CalledProcessError as e:
        print(f'Error running final.py: {e}')

if '_name_' == '_main_':
    run_codeindex()  # First, codeindex the HTML content
    run_final()   # Then, upload it to S3