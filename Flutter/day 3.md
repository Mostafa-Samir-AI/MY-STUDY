# widgets
- every thing in flutter is widget
- sizedbox --> give a space between any widgets
- icon --> adding an icon
- **overload pixles** --> error that caused by the overflow of widgets out of the container
- we solve this problem by using container
```dart
children: [

          Text('hello world') ,

          Text("AI",style: TextStyle(color: Colors.amberAccent),),

          Container(

            height: 350,

            width: 250,

            color: Colors.amber,

            // adding a child

            //* add padding

            child: Padding(

              padding: const EdgeInsets.all(8.0),

              child: Row(

                children: [

                  Text("User name"),

                  SizedBox(width: 16,),

                  Text("darsh"),

                  SizedBox(width: 16,),

                ],

              ),

            ),

  

          ),
```

# Buttons
- inkWell --> button
- when adding a decoration , we need to remove the color of the container 
# images
- create a folder called *assets*

- market place for flutter --> *Pub.dev*
- spalsh screen !

- satetless --> cannot design widgets interact with each other 
- statefull guarantees that
- but we need to handle the states -->**state management** (important)
- in our project we will create an UI folder and logic folder