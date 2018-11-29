# mj_viz
Utility library for visualization of MuJoCo Scenes

## Build
1. - Download MuJoCo binaries from the official [website](http://www.mujoco.org/) and also obtain the license key.
2. Unzip the downloaded mjpro150 directory into `~/.mujoco/mjpro150`, and place your license key (mjkey.txt) at `~/.mujoco/mjkey.txt`
3. Clone mj_viz repo 
4. `cd mj_viz`
5. `nmake all`. This builds two targets `viz` and `libviz`. `viz` is a visualizer executable and `vizlib` is a shared library
6. Add `mj_viz/source` to your pythonpath.


## demo
1. Use `./bin/mj_viz` to check out the c visualizer demo 
1. Use `python demo/demo_mj_viz.py` to check out the python visualizer demo 


## Usage
1. Use `viz_init` to initialize the visualizer
2. Use `viz_model_info` to get information about the loaded model
3. Use `viz_update` to update the state of the model loaded in the visualizer
4. Use `viz_close` to close the visualizer
