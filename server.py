import time
import hashlib

from proto import auth_pb2

_ONE_DAY_IN_SECONDS = 60*60*24

class Server(auth_pb2.BetaAuthenticationServicer):
  def Login(self, request, context):
    error = ""
    session = ""
    try:
      sha = hashlib.sha512()
      sha.update("{}:{}".format(request.username, request.password))
      session = sha.hexdigest()
    except Exception as e:
      error = "{}".format(e)
    return auth_pb2.LoginResponse(error=error, session=session)

def serve():
  server = auth_pb2.beta_create_Authentication_server(Server())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()