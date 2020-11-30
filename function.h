#pragma once
#include <cmath>
class function {
    public:
        double F(double x) {
            double answer = x * x - 3;
            return answer;
        }
        double G(double x) {
            double answer = pow(x + 10, 1.0/4.0);
            return answer;
        }
};
