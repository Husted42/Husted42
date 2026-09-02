#include "Exception.hpp"
#include <iostream>

// Constructor
Exception::Exception(std::string tagString, std::string probString)
    : mTag(tagString), mProblem(probString) {}

// Print debug information
void Exception::PrintDebug() const {
    std::cerr << "Exception in " << mTag << ": " << mProblem << std::endl;
}
