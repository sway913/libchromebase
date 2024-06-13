add_executable(stackTrace 
    "main.cc"
)
target_link_libraries(stackTrace
    PRIVATE
        chromium::base
)