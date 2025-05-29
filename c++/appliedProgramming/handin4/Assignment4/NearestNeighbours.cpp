#include "armadillo.hpp"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

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

int majorityVote(const std::vector<int>& labels) {
    std::map<int, int> count;
    for (int label : labels) {
        count[label]++;
    }
    // return the label with max count
    return (count[1] >= count[-1]) ? 1 : -1;
}

int main() {
    try {
        arma::mat trainX = readMatrix("dataX.dat");       // NxD
        arma::vec trainY = readVector("dataY.dat");       // Nx1
        arma::mat testX = readMatrix("dataXtest.dat");    // MxD

        int k = 5;
        int N = trainX.n_rows;
        int M = testX.n_rows;

        arma::vec predictions(M);

        for (int i = 0; i < M; ++i) {
            arma::rowvec testPoint = testX.row(i);

            // Compute distances to all training points
            std::vector<std::pair<double, int>> dist_label_pairs;
            for (int j = 0; j < N; ++j) {
                double dist = arma::norm(trainX.row(j) - testPoint, 2);
                int label = static_cast<int>(trainY(j));
                dist_label_pairs.push_back({dist, label});
            }

            // Sort by distance (smallest first)
            std::sort(dist_label_pairs.begin(), dist_label_pairs.end());

            // Take labels of k nearest neighbors
            std::vector<int> k_labels;
            for (int l = 0; l < k; ++l) {
                k_labels.push_back(dist_label_pairs[l].second);
            }

            // Majority vote
            predictions(i) = majorityVote(k_labels);
        }

        // Save predictions to file
        predictions.save("NN.dat", arma::raw_ascii);
        std::cout << "Predictions written to NN.dat\n";

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
