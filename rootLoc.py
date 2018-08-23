#用於反回根目錄位置
import os

def get_root():
    return os.path.dirname(os.path.abspath(__file__))