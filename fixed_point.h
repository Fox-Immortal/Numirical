#include <iostream>
#include <cmath>
#include "VariadicTable.h"
#include "function.h"

using namespace std;

class fixed_point {
    public:
        //Atr
        double d = 3;
        double xi;
        double xi_1;
        double target_error;
        double error = -1;
        double G_x;
        int iteration = 0;
        int end;
        function Function;
        VariadicTable<int, double, double, double> vt;
        //Cont
        fixed_point() {}
        fixed_point(double _xi, double _target_error, int _end) {
            init(_xi, _target_error, _end);
        }
        //Methods
        void init(double _xi, double _target_error, int _end) {
            xi = _xi, target_error = _target_error, end = _end;
            vt = VariadicTable<int, double, double, double>({"Iteration", "Xi", "Xi+1", "Error"});
        }
        void do_fixed_point() {
            if(iteration == end || (error <= target_error && error != -1)) {
                print();
                return;
            }

            xi_1 = Function.G(xi);
            error = abs(xi - xi_1)/xi_1 * 100;
            round_to(xi, d);
            round_to(xi_1, d);
            round_to(error, d);
            vt.addRow(iteration++, xi, xi_1, error);
            xi = xi_1;
            if(error > 100) {
                cout << "Diverge there is no zeros" << endl;
                print();
                reset();
                return;
            }
            do_fixed_point();
        }
        void print() {
            vt.print(cout);
        }
        void reset() {
            vt = VariadicTable<int, double, double, double>({"Iteration", "Xi", "Xi+1", "Error"});
            error = -1;
            iteration = 0;
        }
        void round_to(double& x, int d) {
            x = round(x * pow(10, d))/ pow(10, d);
        }
};
