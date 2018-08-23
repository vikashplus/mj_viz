//----------------------------------//
// MuJoCo Visualizer                //
// Author Vikashplus@gmail.com      //
//----------------------------------//

#include "viz.h"
#include <unistd.h>
#include "stdio.h"
#include "stdlib.h"

// update the viz using your sensor data stream
void update_viz(double *time, double *qpos, double *qvel, int nq, int nv)
{
    // dummy update 
    qpos[2] += 0.002;
}


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

    // Get up, do a little dance and then close
    usleep(5000000);

    // Close the viz, time to go home.
    viz_close();
    return 0;    
}