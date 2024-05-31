#!/bin/bash
# Create a Python script for the RTSP server
cat <<'EOF' > $HOME/rtsp_server.py
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GLib

Gst.init(None)

class RTSPMediaFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        super(RTSPMediaFactory, self).__init__()

    def do_create_element(self, url):
        pipeline_str = 'v4l2src device=/dev/video0 ! video/x-raw,width=640,height=480,framerate=30/1 ! videoconvert ! x264enc tune=zerolatency speed-preset=ultrafast key-int-max=30 ! rtph264pay name=pay0 pt=96'
        return Gst.parse_launch(pipeline_str)

class RTSPServer(GstRtspServer.RTSPServer):
    def __init__(self):
        super(RTSPServer, self).__init__()
        self.factory = RTSPMediaFactory()
        self.factory.set_shared(True)
        self.mount_points = self.get_mount_points()
        self.mount_points.add_factory("/stream", self.factory)
        self.attach(None)

if __name__ == '__main__':
    server = RTSPServer()
    print('RTSP server running at rtsp://192.168.4.1:8554/stream')
    loop = GLib.MainLoop()
    loop.run()
EOF

# Execute the RTSP server
python3 $HOME/rtsp_server.py &
echo "RTSP server started at rtsp://192.168.4.1:8554/stream"
