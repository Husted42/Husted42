#include "FileNotOpenException.hpp"

// Constructor
FileNotOpenException::FileNotOpenException(std::string prob)
    : Exception("FileNotOpenException", prob) {}
