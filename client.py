from grpc.beta import implementations
import logging
import sys
from proto import auth_pb2

_TIMEOUT_SECONDS = 10
_DEFAULT_USERNAME = "user"
_DEFAULT_PASSWORD = "pass"

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, datefmt='%Y-%m-%dT%H:%M:%S%z')

def run(username, password):
  logger = logging.getLogger("com.ivanfoong.grpc.example")
  logger.setLevel(logging.DEBUG)
  channel = implementations.insecure_channel('localhost', 50051)
  stub = auth_pb2.beta_create_Authentication_stub(channel)
  response = stub.Login(auth_pb2.LoginRequest(username=username,password=password), _TIMEOUT_SECONDS)
  if response.error != "":
    logger.exception("could not login: %s", response.error)
  else:
    logger.info("Session: %s", response.session)

if __name__ == '__main__':
  username = _DEFAULT_USERNAME
  password = _DEFAULT_PASSWORD
  if len(sys.argv) > 2:
    username = sys.argv[1]
    password = sys.argv[2]
  run(username, password)