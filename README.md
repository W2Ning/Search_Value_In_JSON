# Search_Value_In_JSON


`pip3 install jsonpath`



```
python3 Search_Value_In_JSON.py -h


usage: Search_Value_In_JSON.py [-h] [--file FILE] [--key KEY]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  The json file you wanna to analysis
  --key KEY, -k KEY     The key you wanna to search
```

> 如果JSON文件为多层嵌套，且不同层存在相同的Key键值, 那么不同层的Value会混在一起
