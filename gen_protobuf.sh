protoc -I . auth.proto --python_out=proto --grpc_out=proto --plugin=protoc-gen-grpc=`which grpc_python_plugin`
