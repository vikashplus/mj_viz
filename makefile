MJ_PATH=$(HOME)/.mujoco/mjpro150
COMMON=-O2 -I$(MJ_PATH)/include/ -L$(MJ_PATH)/bin -std=c++11 -mavx

default:
	@echo Building ==============================
	g++ $(COMMON) source/viz.cpp source/user.cpp -lmujoco150 -lGL -lglew -lpthread $(MJ_PATH)/bin/libglfw.so.3 -o bin/viz


libmj_viz.so:
	$(CXX) $(COMMON) -Wno-write-strings -shared -Wl,-soname,libmj_viz -o bin/libmj_viz.so -fPIC source/viz.cpp -Isource/ -lmujoco150 -lGL -lglew -lpthread $(MJ_PATH)/bin/libglfw.so.3


clean:
	@echo Cleaning ==============================
	-rm bin//viz*
