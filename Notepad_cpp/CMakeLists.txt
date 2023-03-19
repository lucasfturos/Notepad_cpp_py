cmake_minimum_required(VERSION 3.5)

project(Notepad_cpp LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 COMPONENTS Widgets LinguistTools REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Widgets LinguistTools REQUIRED)

set(TS_FILES
    lib/ts/Notepad_cpp_pt_BR.ts
)

set(UI_FILES
    lib/ui/mainwindow.ui
)

set(PROJECT_HEADERS
    src/mainwindow/mainwindow.hpp
)

set(PROJECT_SOURCES
    src/mainwindow/mainwindow.cpp
    src/main.cpp
)

set(CMAKE_AUTOUIC_SEARCH_PATHS
    ${PROJECT_SOURCE_DIR}/lib/ui
)

add_executable(Notepad_cpp
    ${PROJECT_HEADER}
    ${PROJECT_SOURCES}
    ${TS_FILES}
    ${UI_FILES}
)

target_link_libraries(Notepad_cpp
    PRIVATE Qt${QT_VERSION_MAJOR}::Widgets
)
