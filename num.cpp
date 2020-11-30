#include <iostream>
#include <cmath>
#include <iomanip>
#include "VariadicTable.h"
#include "bisection.h"
#include "false_position.h"
#include "fixed_point.h"


using namespace std;

int main() {
    fixed_point x(2, 0.01, 10);
    x.do_fixed_point();
    return 0;
}