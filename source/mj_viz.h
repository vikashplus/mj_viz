//----------------------------------//
// MuJoCo Visualizer                //
// Author Vikashplus@gmail.com      //
//----------------------------------//

#ifndef MJ_VIS_H
#define MJ_VIS_H

	#if defined(__cplusplus)
	extern "C" {
	#endif

	// description of the robot
	typedef struct _vizModelInfo
	{
		// array sizes
		int nq;		// number of generalized coordinates = dim(qpos)
		int nv;		// number of degrees of freedom = dim(qvel)
		int nu;		// number of actuators/controls = dim(ctrl)
		int na;		// number of activation states = dim(act)
	
	}vizModelInfo;

	// close the viz
	void viz_close();

	// initialize the viz 
	void viz_init(char* modelPath, char* licensePath);

	// update the visualizer's state
	bool viz_update(double time, double *qpos, double *qvel, int nq, int nv);

	// get the model info
	bool viz_model_info(vizModelInfo *info);


	#endif

	#if defined(__cplusplus)
	}
#endif