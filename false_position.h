#include <iostream>
#include <cmath>
#include "VariadicTable.h"
#include "function.h"

using namespace std;

class false_position {
    public:
        //Atr
        double d = 4;
        double lower;
        double upper;
        double target_error;
        double error = -1;
        double root;
        double F_lower;
        double F_upper;
        double F_root;
        int iteration = 0;
        int end;
        function Function;
        VariadicTable<int, double, double, double, double, double, double, string, string, double> vt;
        //Cont
        false_position() {}
        false_position(double _lower, double _upper, double _target_error, int _end = 0) {
            init(_lower, _upper, _target_error, _end);
        }
        //Methods
        void init(double _lower, double _upper, double _target_error, int _end = 0) {
            lower = _lower, upper = _upper, target_error = _target_error, end = _end, root = (lower + upper) / 2;
            vt = VariadicTable<int, double, double, double, double, double, double, string, string, double>({"Iteration", "Lower", "Upper", "Root", "F(Lower)", "F(Upper)", "F(Root)", "Intermediate L*R", "Intermediate U*R", "Error"});
        }
        void do_false_position() {
            if(iteration == end || (error <= target_error && error != -1)) {
                print();
                return;
            }

            double pre = root;
            F_lower = Function.F(lower), F_upper = Function.F(upper);
            root = upper - (F_upper * (lower - upper)) / (F_lower - F_upper);
            F_root = Function.F(root);
            string m1 = "+", m2 = "+";
            if(F_lower * F_root < 0)
                m1 = "-";
            if(F_upper * F_root < 0)
                m2 = "-";
            if(iteration > 0 )
                error = abs(pre - root)/root * 100;
            round_to(lower, d);
            round_to(upper, d);
            round_to(root, d);
            round_to(F_lower, d);
            round_to(F_upper, d);
            round_to(F_root, d);
            round_to(error, d);
            vt.addRow(iteration++, lower, upper, root, F_lower, F_upper, F_root, m1, m2, error);
            if(F_lower * F_root < 0)
                upper = root;
            else if(F_upper * F_root < 0) 
                lower = root;
            else {
                reset();
                cout << "There is no zeros between " << lower << " and " << upper << endl;
                return;
            }
            do_false_position();
        }
        void print() {
            vt.print(cout);
        }
        void reset() {
            vt = VariadicTable<int, double, double, double, double, double, double, string, string, double>({"Iteration", "Lower", "Upper", "Root", "F(Lower)", "F(Upper)", "F(Root)", "Intermediate L*R", "Intermediate U*R", "Error"});
            error = -1;
            iteration = 0;
        }
        void round_to(double& x, int d) {
            x = round(x * pow(10, d))/ pow(10, d);
        }
};
