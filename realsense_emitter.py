# https://forums.intel.com/s/question/0D70P0000069qxHSAQ/how-to-enabledisable-emitter-through-python-wrapper-pyrealsense2?language=en_US

import pyrealsense2 as rs

pipeline = rs.pipeline()
config = rs.config()
pipeline_profile = pipeline.start(config)
device = pipeline_profile.get_device()

depth_sensor = device.query_sensors()[0]
emitter = depth_sensor.get_option(rs.option.emitter_enabled)
print("emitter = ", emitter)

# Turns the point cloud laser on or off
set_emitter = 0 # 0 = off, 1 = on
depth_sensor.set_option(rs.option.emitter_enabled, set_emitter)
emitter1 = depth_sensor.get_option(rs.option.emitter_enabled)
print("new emitter = ", emitter1)