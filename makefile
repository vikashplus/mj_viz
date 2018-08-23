MJ_PATH=$(HOME)/.mujoco/mjpro150
COMMON=-O2 -I$(MJ_PATH)/include/ -L$(MJ_PATH)/bin -std=c++11 -mavx

default:
	@echo Building ==============================
	g++ $(COMMON) source/viz.cpp source/user.cpp -lmujoco150 -lGL -lglew -lpthread $(MJ_PATH)/bin/libglfw.so.3 -o bin/viz

clean:
	@echo Cleaning ==============================
	-rm bin//viz*