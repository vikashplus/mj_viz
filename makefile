MJ_PATH=$(HOME)/.mujoco/mujoco200_linux
COMMON=-O2 -I$(MJ_PATH)/include/ -L$(MJ_PATH)/bin -std=c++11 -mavx

all: viz libviz

viz:
	@echo Building ==============================
	g++ $(COMMON) source/mj_viz.cpp demo/demo_mj_viz.cpp -Isource/ -lmujoco200 -lGL -lglew -lpthread $(MJ_PATH)/bin/libglfw.so.3 -o bin/mj_viz

libviz:
	$(CXX) $(COMMON) -Wno-write-strings -shared -Wl,-soname,libmj_viz -o bin/libmj_viz.so -fPIC source/mj_viz.cpp -Isource/ -lmujoco200 -lGL -lglew -lpthread $(MJ_PATH)/bin/libglfw.so.3


clean:
	@echo Cleaning ==============================
	-rm bin//mj_viz*
	-rm bin//libmj_viz*
