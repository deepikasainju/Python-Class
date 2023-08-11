# dictionary ley has restriction that they must be immutable data types
# no restriction in dictionary values

d={"name":"jn","age":23} # valid
d={1:"hello",2:"world"} # valid
d={2.3:1,5.67:5} #valid
d={(1,2):"hello",(3,2):"world"} #valid
d={[1,2]:1, [3,1]:8} # invalid
d={([1,2],3):5, "name":"in"} # invalid

