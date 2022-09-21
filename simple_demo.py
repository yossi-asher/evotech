import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python' 

import pkg_resources
protobuf_version = [i.version for i in pkg_resources.working_set if i.key == 'protobuf'][0]
print("Protobuf version: ", protobuf_version)

import simple_pb2 as simple_pb2
simple_message = simple_pb2.SimpleMessage()

print('Success')