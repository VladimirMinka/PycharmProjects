import  pytest
class Server:
    def __init__(self):
        self.running = False


    def start(self):
        self.running = True


    def stop(self):
        self.running = False
        #
        # @pytest.fixture
        # def db_session():
        #     connect = DB.connect()
        #     yield connect
        #     connect.close()
@pytest.fixture
def server():

    yield Server
    