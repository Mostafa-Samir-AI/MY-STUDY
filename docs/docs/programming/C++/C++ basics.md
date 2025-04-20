# why C++ ?
- mid level language 
- very fast 
- work near to machine hardware

**IDE** : integrated development environments
**text Editor** : Notepad++ , VScode  

# C++ file structure 
- c++ code 
```cpp
#include <iostream>

int main()
{


return 0;
}
```
## lets break it into pieces
1. `#include <iostream>` : header file that have basic input and output operations 
2. `int main()` : main function of our code, <u>the compiler will execute the main as the first block of code</u>
3. `return 0;` : if *zero* returned <u>(no problems)</u> , else if *one* returned <u>problem</u>

# writing output in console 
```c++ 
std::cout << "hello world" << std::endl; 
```

## lets break it down
1. `std::cout` : std--> standard module , cout --> C output (for output)

# explain statements
---
- statement is the basic building unit of the code of C++ 
- every statement should end with `;`

```cpp
# include <iostream>

int main()
{
std::cout  << "this is a statement" ;

return 0 ;
}
```

# defining a function in C++
---
