#----------------------------------------------------------------
# Generated CMake target import file for configuration "RELEASE".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Arrow::arrow_shared" for configuration "RELEASE"
set_property(TARGET Arrow::arrow_shared APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(Arrow::arrow_shared PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libarrow.1900.0.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libarrow.1900.dylib"
  )

list(APPEND _cmake_import_check_targets Arrow::arrow_shared )
list(APPEND _cmake_import_check_files_for_Arrow::arrow_shared "${_IMPORT_PREFIX}/lib/libarrow.1900.0.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
