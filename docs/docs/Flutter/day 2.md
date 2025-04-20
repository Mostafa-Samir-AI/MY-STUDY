# private 
- private attributes cannot be accessed out of the class 
- assigning values the old way will cause an error
```dart
class user {
   String ? name ;
   int ? age ;
   int ? ID ;
   
  user(String name , int age , int ID){
  this.name = _name ;
  this.age = age ;
  this.ID = ID ;
  }
  
  void display_salary(){
    print("salary is 5000 EGP") ;
  }

  void setName(String name){
	  this._name = name ;
  }
  int getName(){
	  return this._name;
  } 
}
```

# abstraction
