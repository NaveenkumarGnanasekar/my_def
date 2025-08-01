import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/naveengnanasekar/dev_ws/install/nav2_simple_commander'
