#include "armadillo.hpp"
#include <iostream>
#include <fstream>
#include <cmath>

arma::mat readMatrix(const std::string& filename) {
    arma::mat data;
    if (!data.load(filename, arma::raw_ascii)) {
        throw std::runtime_error("Failed to load file: " + filename);
    }
    return data;
}

arma::vec readVector(const std::string& filename) {
    arma::vec data;
    if (!data.load(filename, arma::raw_ascii)) {
        throw std::runtime_error("Failed to load file: " + filename);
    }
    return data;
}

int main() {
    try {
        arma::mat X = readMatrix("dataX.dat");         // NxD
        arma::vec y = readVector("dataY.dat");         // Nx1
        arma::mat Xtest = readMatrix("dataXtest.dat"); // MxD

        int N = X.n_rows;
        int D = X.n_cols;

        arma::vec w = arma::zeros<arma::vec>(D);       // initialize w = 0
        double lr = 0.1;                               // learning rate
        double tol = 1e-7;                             // tolerance
        int max_iters = 100000;                        // safety cap

        for (int iter = 0; iter < max_iters; ++iter) {
            arma::vec grad = arma::zeros<arma::vec>(D);

            for (int i = 0; i < N; ++i) {
                double yi = y(i);
                double wx = arma::dot(w, X.row(i));
                double factor = yi / (1.0 + std::exp(yi * wx));
                grad -= factor * X.row(i).t();
            }

            grad /= N;

            if (arma::norm(grad, 2) < tol) {
                std::cout << "Converged after " << iter << " iterations.\n";
                break;
            }

            w = w - lr * grad;
        }

        // Classify test points
        int M = Xtest.n_rows;
        arma::vec predictions(M);

        for (int i = 0; i < M; ++i) {
            double score = arma::dot(w, Xtest.row(i));
            predictions(i) = (score >= 0) ? 1 : -1;
        }

        // Save predictions
        predictions.save("LogReg.dat", arma::raw_ascii);
        std::cout << "Predictions written to LogReg.dat\n";

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
