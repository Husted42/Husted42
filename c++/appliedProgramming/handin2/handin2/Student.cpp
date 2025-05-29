#include "Student.hpp"
#include <numeric>  // for std::accumulate
#include <initializer_list>

Student::Student()
    : name(), tuition_fees(0.0), library_fines(0.0) {}

Student::Student(std::string name, double fines, double fees)
    : name(std::move(name)), tuition_fees(fees), library_fines(0.0) {
    SetLibraryFines(fines);
}

double Student::MoneyOwed() const {
    std::initializer_list<double> amounts{tuition_fees, library_fines};
    return std::accumulate(amounts.begin(), amounts.end(), 0.0);
}

void Student::SetLibraryFines(double amount) {
    if (amount >= 0.0) {
        library_fines = amount;
    }
}

double Student::GetLibraryFines() const {
    return library_fines;
}
