#include "PhdStudent.hpp"

PhdStudent::PhdStudent(std::string name, double fines, double fees, bool fullTime)
    : GraduateStudent(std::move(name), fines, fees, fullTime) {
    SetLibraryFines(0.0); 
}

double PhdStudent::MoneyOwed() const {
    return 0; 
}
