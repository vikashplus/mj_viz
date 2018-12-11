# mj_viz
Dependency-free utility library for visualization of MuJoCo Scenes. The library is written purely in C for speed and efficiency. Python bindings are also provided to facilitate usage.


## Build
1. Download MuJoCo binaries from the official [website](http://www.mujoco.org/) and also obtain the license key.
2. Unzip the downloaded mjpro150 directory into `~/.mujoco/mjpro150`, and place your license key (mjkey.txt) at `~/.mujoco/mjkey.txt`
3. Clone mj_viz repo 
4. `cd mj_viz`
5. `make all`. This builds two targets `viz` and `libviz`. `viz` is a visualizer executable and `vizlib` is a shared library
6. Add `mj_viz/source` to your pythonpath.


## Demo
1. Use `./bin/mj_viz` to check out the c visualizer demo 
1. Use `python demo/demo_mj_viz.py` to check out the python visualizer demo 


## Usage
1. Use `viz_init(model_xml_path, mujoco_license_path)` to initialize the visualizer
2. Use `viz_model_info( (*vizModelInfo) info)` to get information about the loaded model
3. Use `viz_update(time, qpos, qvel, nq, nv)` to update the state of the model loaded in the visualizer
4. Use `viz_close()` to close the visualizer

## Known Issues 
The library is developed on Linux. While the code is cross-platform, it has not been tested on other OS.
