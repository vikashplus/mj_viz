# //----------------------------------//
# // MuJoCo Visualizer                //
# // Author Vikashplus@gmail.com      //
# // Copyright (c) 2018 Vikash Kumar  //
# //----------------------------------//

import mj_viz as viewer

# ============ Test the wrapper
if __name__ == "__main__":

    import numpy as np
    import time
    from pathlib import Path

    # Initialize the wrapper
    home = str(Path.home())
    viewer.viz_init(home+"//.mujoco//mujoco200_linux//model//humanoid.xml", home+"//.mujoco//mjkey.txt")

    # get model info
    info = viewer.viz_model_info()
    viewer.printStructure(info)

    # make updates to the state
    qpos = np.zeros(info.nq)
    qvel = np.zeros(info.nv)
    for t in range(100):
        qpos[0] = 0.75*np.sin(t*0.1)
        qpos[1] = 0.25*np.cos(t*0.1)
        qpos[2] = 1.3
        viewer.viz_update(float(t), qpos, qvel)
        time.sleep(.1)

    # Exit
    input("Press Enter to exit visualizer...")
    viewer.viz_close()