//----------------------------------//
// MuJoCo Visualizer                //
// Author Vikashplus@gmail.com      //
//----------------------------------//

#include "mj_viz.h"
#include <unistd.h>
#include "stdio.h"
#include "stdlib.h"
#include <math.h>


int main()
{
    // Get paths, google maps wont help here.
    char filePath[1000];
    char licensePath[100];
    char* homedir = getenv("HOME");
    if(homedir == NULL)
    {   printf("ERROR:: Environment variable 'HOME' not found.\n");
        exit(0);
    }   
    sprintf(filePath, "%s//.mujoco//mjpro150//model//humanoid.xml", homedir);
    sprintf(licensePath, "%s//.mujoco//mjkey.txt", homedir);

    // Fire up the viz, movie time
    printf("Staring Viz\n");
    viz_init(filePath, licensePath);

    // get model info
    vizModelInfo info;
    viz_model_info(&info);

    // use the model info the generate arrays
    double *qpos = (double *) malloc(info.nq*sizeof(double));
    double *qvel = (double *) malloc(info.nv*sizeof(double));

    // Get up, do a little dance and then close
    for(int i=0; i < 100; i++)
    {
        qpos[0] = 0.75*sin(i*0.1);
        qpos[1] = 0.25*cos(i*0.1);
        qpos[2] = 1.3;
        viz_update(double(i), qpos, qvel, info.nq, info.nv);
        usleep(100000);
    }

    // Close the viz, time to go home.
    viz_close();
    return 0;    
}