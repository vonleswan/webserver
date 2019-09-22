import os


class index(object):
    """builds index.html based on string:client_address and string:server_address"""
    def __init__(self, client_address, server_address):
        super(index, self).__init__()
        cwd = os.getcwd()
        f = open(cwd + "/html/index_template.html", 'rt')

        blob = f.read()
        client_index = blob.find("CLIENT_IP: ") + 11
        blob_end = blob[client_index:]
        blob = blob[:client_index] + client_address[0] + blob_end  # insert client_address

        server_index = blob.find("SERVER_IP: ") + 11
        blob_end = blob[server_index:]
        blob = blob[:server_index] + server_address + blob_end  # insert server_address

        f.close()
        f = open(cwd + "/html/index.html", 'w+')
        f.write(blob)
        f.close()
