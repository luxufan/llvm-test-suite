# Aggressive settings to produce fast code.
set(OPTFLAGS "${OPTFLAGS} -O3 -fomit-frame-pointer -fwhole-program-vtables -save-stats=obj -flto -DNDEBUG")
if(APPLE)
  set(OPTFLAGS "${OPTFLAGS} -mdynamic-no-pic")
endif()

set(CMAKE_C_FLAGS_RELEASE "${OPTFLAGS}" CACHE STRING "")
set(CMAKE_CXX_FLAGS_RELEASE "${OPTFLAGS}" CACHE STRING "")
set(CMAKE_BUILD_TYPE "Release" CACHE STRING "")
