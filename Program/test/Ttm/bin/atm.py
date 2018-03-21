Author = 'Liu Lei'
import os,sys
BASIC_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#os.path.abspath(__file__)获取当前文件路径，os.path.abspath():获取当前文件夹
sys.path.append(BASIC_DIR)
from conf import setting
from core import main
main.login()