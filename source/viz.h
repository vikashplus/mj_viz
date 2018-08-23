//----------------------------------//
// MuJoCo Visualizer                //
// Author Vikashplus@gmail.com      //
//----------------------------------//

#ifndef VIS_H
#define VIS_H

// clsoe the viz
void viz_close();

// initialize the viz 
void viz_init(char* modelPath, char* licensePath);

// Callback for the users to update the visualizer
extern void update_viz(double *time, double *qpos, double *qvel, int nq, int nv);

#endif