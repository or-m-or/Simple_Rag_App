import os
from datetime import datetime

def get_files(root_path: str = os.path.join(os.getcwd(), "documents")) -> list:
    ''' /documents 폴더 안에 있는 파일 리스트를 반환하는 함수 '''
    return ["(선택)"] + os.listdir(root_path)

