#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "thrift::thrift" for configuration "Release"
set_property(TARGET thrift::thrift APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(thrift::thrift PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libthrift.0.21.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libthrift.0.21.0.dylib"
  )

list(APPEND _cmake_import_check_targets thrift::thrift )
list(APPEND _cmake_import_check_files_for_thrift::thrift "${_IMPORT_PREFIX}/lib/libthrift.0.21.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
