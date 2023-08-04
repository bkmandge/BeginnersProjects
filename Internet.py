"""
                    # Internet Speed Test
Gives o/p like:-

Downloading speed is: 8.26085680670184Mb/sUploading speed is: 0.9396153415257912Mb/s
Ping speed is: 49.219

"""

import speedtest as st


# Set Best Server
server = st.Speedtest()
server.get_best_server()

# Test Downloading Speed
down = server.download()
down = down / 1000000

print(f"Downloading speed is: {down}Mb/s")


# Test Uploading Speed
up = server.upload()
up = up / 1000000

print(f"Uploading speed is: {up}Mb/s")


# Test Ping
ping = server.results.ping
print(f"Ping speed is: {ping}")
