# cmake version
cmake_minimum_required(VERSION 3.2)

# project name
project(makeDemo)

# head file path
# INCLUDE_DIRECTORIES(.)

# source path
# AUX_SOURCE_DIRECTORY(. DIR_SRCS)

file(GLOB SOURCES)

# add executable file 添加编译的可执行文件
add_executable(ChainList mylib.h mylib.c text.c)

# add link library
#TARGET_LINK_LIBRARIES(${PROJECT_NAME} m)

