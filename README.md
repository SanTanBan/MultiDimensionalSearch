# MultiDimensionalSearch

All these Multidimensional searches will generate Images in the same folder as well as an Excel Sheet showing the progress of the Search.

To tune each search program, you may change the starting values which are provided as (2,0)

Also to change the stopping criterias, just change the function which is being called. # Just need to interchnage the commented lines of the MultiDimensional Search Function which is being called

The Python File named "Cyclic CoOrdinate Search with Acceleration Steps" has a new Single Dimensional Search included {named SanBan} as well as the possibility of using multiple acceleration steps when the number of dimensions are high. In which case every possible combination of +ve and -ve direction is being accounted for.

Example:- If there are 3 dimensions of x1,x2,x3; then the possible acceleration dimensions are:-

[1,1,1] ; [1,1,-1] ; [1,-1,1] ; [-1,1,1] ; [1,-1,-1] ; [-1,1,-1] ; [-1,-1,1] ; [-1,-1,-1]

Here all these directions may be considered in the commented code. However only half of these directions may be considered since the other half is just the negative of the same directions.
