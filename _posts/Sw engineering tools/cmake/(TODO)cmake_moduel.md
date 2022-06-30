[CMake] 10. 모듈
글쓴이 keunjun 날짜 2018-10-07

CMake에서는 코드의 재사용성을 높히기 위하여, 모듈이라는 개념을 제공한다. 쉽게 말하면 CMakeLists 파일에서 다른 CMake 파일을 실행한다고 보면 된다. 이러한 기능을 사용자에게 제공하므로서 사용자는 필요한 모든 기능을 필요할때마다 구현할 필요가 없이 이미 구현된 CMake 파일을 불러다 쓰므로서 개발이 빨라지고 코드의 신뢰성이 상승하는 효과를 얻을 수 있다.

모듈을 이용하는 가장 쉬운 방법은 include() (doc)를 이용하는 것이다. 아래 예제를 살펴보자.

include(CheckTypeSize)
check_type_size(long SIZEOF_LONG)
미리 구현되어진 CheckTypeSize.cmake라는 파일을 읽어와 그 안에 정의되어있는 매크로를 사용할 수 있게 해준다. 실제로 CheckTypeSize.cmake 파일에 가서 확인해보면 check_type_size 이라는 매크로가 이미 정의되어 있는 것을 확인 할 수 있다. 그렇다면 CMake는 어떻게 CheckTypeSize.cmake를 찾을 수 있었을까? CMake는 모듈을 찾을 때 CMAKE_MODULE_PATH에 있는 폴더들에서 원하는 모듈이 있는지 찾아본다. 그 안에 없다면 Module이 설치된 곳을 확인해본다.

set(CMAKE_MODULE_PATH 
    ${CMAKE_MODULE_PATH} 
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
만약에 새롭게 CMake 파일을 만들고 다른 CMake 파일에서 include 하고 싶다면 CMAKE_MODULE_PATH에 경로를 추가하면 된다.

Find_package()
find_package() (doc)는 include()처럼 이미 정의된 CMake 파일을 읽어서 그 안에 정의된 함수, 매크로 그리고 변수를 사용 할 수 있게 해준다. include()와 함께 모듈을 읽어드린다는 공통점을 갖고 있지만 좀 더 특수한 상황에서 쓰인다. 바로, 외부 라이브러리를 사용하기 위해 만들어진 모듈들을 부르는데 사용된다는 점인데 모듈을 찾는 규칙이 include()와 조금 다르다.

find_package(${PACKAGE_NAME})
위의 예제 경우 CMAKE_MODULE_PATH 폴더에서 Find${PACKAGE_NAME}.cmake 파일을 찾거나 CMAKE_INSTALL_PREFIX/lib/${PACKAGE_NAME} 폴더에서 ${PACKAGE_NAME}Config.cmake 파일을 찾아서 읽는다.

MyCMakeProject
├── CMakeLists.txt
├── cmake
│   ├── FindA.cmake
│   └── B.cmake
├── include
└── src
위와 같은 폴더 구조를 갖는 프로젝트에서 상위 폴더에 있는 CMakeLists 파일은 다음과 같다면

set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
find_package(A)
include(B)
두번째 줄은 FindA.cmake를, 세번째 줄에서는 B.cmake를 불러온다. find_package()의 더 자세한 내용은 나중에 라이브러리를 다루는 파트에서 다루도록 한다.

https://keunjun.blog/2018/10/07/cmake-10-%EB%AA%A8%EB%93%88/

find_package 및 찾기 사용 .cmake 모듈
CMake로 설치된 패키지를 찾는 기본 방법은 find_package 함수를 Find<package>.cmake 파일과 함께 사용하는 것입니다. 이 파일의 목적은 패키지에 대한 검색 규칙을 정의하고 <package>_FOUND , <package>_INCLUDE_DIRS 및 <package>_LIBRARIES 와 같은 다른 변수를 설정하는 <package>_LIBRARIES 입니다.

많은 Find<package>.cmake 파일은 CMake에서 이미 기본적으로 정의되어 있습니다. 그러나 필요한 패키지 파일이 없으면 자신의 파일을 직접 작성하여 ${CMAKE_SOURCE_DIR}/cmake/modules (또는 CMAKE_MODULE_PATH 가 무시 된 경우 다른 디렉토리)에 CMAKE_MODULE_PATH

기본 모듈 목록은 매뉴얼 (v3.6) 에서 찾을 수 있습니다. 프로젝트에서 사용 된 CMake의 버전에 따라 매뉴얼을 확인하는 것이 중요합니다. 그렇지 않으면 모듈이 누락되었을 수 있습니다. cmake --help-module-list 사용하여 설치된 모듈을 찾을 수도 있습니다.

Github 의 FindSDL2.cmake 에 대한 좋은 예가 있습니다.

다음은 SDL2가 필요한 기본 CMakeLists.txt 입니다.

cmake_minimum_required(2.8 FATAL_ERROR)
project("SDL2Test")

set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH} ${CMAKE_SOURCE_DIR}/cmake/modules")
find_package(SDL2 REQUIRED)

include_directories(${SDL2_INCLUDE_DIRS})
add_executable(${PROJECT_NAME} main.c)
target_link_libraries(${PROJECT_NAME} ${SDL2_LIBRARIES})
pkg_search_module 및 pkg_check_modules 사용
유닉스 계열 운영 체제에서는 pkg-config 프로그램을 사용하여 <package>.pc 파일을 제공하는 패키지를 찾고 구성 할 수 있습니다.

사용하기 위해서는 pkg-config , 그 호출 할 필요가있다 include(FindPkgConfig) A의 CMakeLists.txt . 다음과 같은 두 가지 기능이 있습니다.

pkg_search_module 패키지를 확인하고 사용 가능한 첫 번째 패키지를 사용합니다.
pkg_check_modules 는 모든 해당 패키지를 검사합니다.
다음은 pkg-config 를 사용하여 2.0.1 이상 버전의 SDL2를 찾는 기본 CMakeLists.txt 입니다.

cmake_minimum_required(2.8 FATAL_ERROR)
project("SDL2Test")

include(FindPkgConfig)
pkg_search_module(SDL2 REQUIRED sdl2>=2.0.1)

include_directories(${SDL2_INCLUDE_DIRS})
add_executable(${PROJECT_NAME} main.c)
target_link_libraries(${PROJECT_NAME} ${SDL2_LIBRARIES})

https://gist.github.com/graykode/5972396e8c00ff7b704938643f95fd72#package%EC%9D%98-%EA%B5%AC%EC%84%B1

