import sys

# David's
sys.path.insert(0, r'c:\users\david\projects\bobabuddy\cs348-boba-buddy\myproject\lib\site-package')

# Ariana's
<<<<<<< HEAD
#sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages")
=======
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages")
>>>>>>> 01d9d983853f60fe45e7aafa244956f96547eb42

import pymysql
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()