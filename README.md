# AirBnB clone - The console  
---  
This project is the first part of the AirBnB project at Holberton School. The intention of this is to use in a practical way all the concepts learned during the foundations segment so far, specially the higher level programming with python, to deploy a copy of the AirBnB webside.  

You can find a command interpeter as the first step of this HBnB project.  

## Index:  

* [Installation](#Installation)  
* [Commands and functions](#commands-and-functions)  
* [Descriptions](#descriptions)  
* [Examples](#examples)  
* [Bugs](#bugs)  
* [Contributors](#contributors)
* [License & Copyright](#licence-&-copyright)

## Installation:  
---  
- Clone this repository: git clone "https://github.com/JRodriguez9510/AirBnB_clone"
- Access AirBnb directory: cd AirBnB_clone
- Run hbnb(interactively): ./console and enter command
- Run hbnb(non-interactively): echo "<command>" | ./console.py
## Commands:  
---  
This current version of [console.py](console.py) allows to use the follwing commands:    
- `EOF` - exits the console  
- `quit` - exits the console  
- `<emptyline>` - overwrites default emptyline method to do nothing.  
- `create` - Creates a new instance of the class BaseModel, and prints the id.  
- `destroy` - Deletes an instance by using the class name and the id.  
- `show` - Prints the string representation of an instance based on the class name and id.  
- `all` - Prints all string representation of all instances based or not on the class name.  
- `update` - Updates an instance based on the class name and id, this command can change and add atributes to the objects  
## Descriptions:  
---  
### `models/` this folder contains all the classes for this project:  
[base_model.py](/models/base_model.py) - This is the base model class and other classes inherit from it.  
#### Methods:  
- `def __init__(self, *args, **kwargs)`  
- `def __str__(self)`  
- `def save(self)`  
- `def to_dict(self)`  
#### Aditional classes:  
(All this classes inherit from BaseModel)  
* [amenity.py](/models/amenity.py)  
* [city.py](/models/city.py)  
* [place.py](/models/place.py)  
* [review.py](/models/review.py)  
* [state.py](/models/state.py)  
* [user.py](/models/user.py)  
### `models/engine` the file storage is contain in this folder, also the serialization and deserialization of the JSON files:  
[file_storage.py](/models/engine/file_storage.py) - erializes and deserializes 
### `test/:`

## Examples:  
---  

## Bugs:  
---  
- No bugs known so far.  
## Contributors:   
---  
- Jorge Rodriguez <jrodriguez9510@outlook.com>  
- Laura Valencia <lauraliliana@gmail.com>
  
## License & Copyright:  
---  
© Jorge Rodriguez 2021  
Licensed under the [MIT Licence](LICENSE)
