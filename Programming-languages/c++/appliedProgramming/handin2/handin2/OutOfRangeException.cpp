#include "OutOfRangeException.hpp"

// Constructor
OutOfRangeException::OutOfRangeException(std::string prob)
    : Exception("OutOfRangeException", prob) {}
