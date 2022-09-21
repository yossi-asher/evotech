# EvoTech
In this demo we will use 2 conda environments
* [environment-old.yml](environment-old.yml) name *old* with protobuf==3.20.0 
* [environment-new.yml](environment-new.yml) name *new* with protobuf==4.21.6

you can create the environment with the command

`conda env create --file environment.yml`

In this demo we will show that update protobuf from version 3.20.0 to 4.21.6 require also code change.

```
conda activate old
python simple_demo.py
```
works with output:
```
Protobuf version:  3.20.0
Success
```
but when we use the *new* env it failed
```
conda activate new
python simple_demo.py
```
output:
```
Protobuf version:  4.21.6
Traceback (most recent call last):
  File "/Users/yossiasher/workspace/evotech/simple_demo.py", line 8, in <module>
    import simple_pb2 as simple_pb2
  File "/Users/yossiasher/workspace/evotech/simple_pb2.py", line 35, in <module>
    _descriptor.FieldDescriptor(
  File "/Users/yossiasher/opt/miniconda3/envs/new/lib/python3.8/site-packages/google/protobuf/descriptor.py", line 560, in __new__
    _message.Message._CheckCalledFromGeneratedFile()
TypeError: Descriptors cannot not be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
```

in order to fix it we must add to the code
```
import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python' 
```
after adding the line:
```
Protobuf version:  4.21.6
Success
```