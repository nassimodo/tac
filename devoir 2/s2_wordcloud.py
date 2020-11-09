import subprocess

tmp_path = "./tmp/"
YEAR = 1855
# without filtering 
command = [
    'wordcloud_cli',
    '--text', f'{tmp_path}{YEAR}.txt',
    '--imagefile', f'{tmp_path}{YEAR}.png',
    '--width', '2000',
    '--height', '1000',
]
subprocess.run(command, capture_output=True)


command = [
    'wordcloud_cli',
    '--text', f'{tmp_path}{YEAR}_keywords.txt',
    '--imagefile', f'{tmp_path}{YEAR}_keywords.png',
    '--width', '2000',
    '--height', '1000',
]
subprocess.run(command, capture_output=True)