
sets
    i 'Factories' /factory_1, factory_2, factory_3/ 
    j 'Markets' /market_1, market_2, market_3, market_4/;
    
Parameters
    a(i) 'Supplier_capacity' /factory_1 300, factory_2 450, factory_3 1000/
    b(j) 'Market_demand' /market_1 325, market_2 300, market_3 275, market_4 250/;

Table d(i,j) 'Distance'
                market_1    market_2    market_3    market_4
    factory_1   2.5         1.7         1.8         2.0
    factory_2   2.5         1.9         1.4         2.4
    factory_3   2.5         1.9         1.4         2.0;

Scalar
    c1 'transport_constatn' /90/
    c2 'fixed_cost' /1100/;


Parameter c(i,j) 'cost';
    c(i,j) = c2 + d(i,j) * c1;

Variables
    z 'Total transportation cost'
    x(i,j) 'Amount transported from i to j';
    
Free variables z;
Positive Variable x;

Equation
    cost 'Objective function'
    supply(i) 'Supply from factory i'
    demand(j) 'Demand from market i';
    
cost.. z =e= sum((i,j), c(i,j)*x(i,j));

supply(i).. sum(j, x(i,j)) =l= a(i);

demand(j).. sum(i, x(i,j)) =g= b(j);

model transport /cost, supply, demand/;

Solve transport using lp minimizing z;

Display z.l, x.l, supply.m, supply.m