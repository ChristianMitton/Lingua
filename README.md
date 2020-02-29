# Lingua

Lingua is an original programming language meant to reflect the english language. The idea was to have a person write programming "sentences" instead of programming "statements". These sentences would be converted into runnable code, which would behave similarly to javascript or python.

Key differences between lingua and programming standard languages:
* Statements end in periods, not semi colons
* Some statements chain together. A sentence following a period indicates that it is a continuation of a pervious sentence.
* Function and variable delerations follow a grammatical flow, not a syntactic one (examples below)
* Certian words can be interchanged, enabling lingustic creativity.
* lingua files have .lg extensions

## Getting Started

You need python3, the files attached to the project, and a lingua file to run the project.

On your terminal, run **"python3 interpreter.py <your_lingua_file.lg>"** to compile and run the lingua program.

### Lingua Syntax examples

**Variable decleration**
```
    let var1 = 1.

    let var2 = 2.  

    let var3 = 7.  
    
    let result = var1 + var2 + var3.
    
    OR
    
    let var1 equal 1.

    let var2 equal 2.  

    let var3 equal 7.  
    
    let result equal var1 + var2 + var3.
```

**Function decleration**
```
create a function called foo. foo has 2 arguments (var1, var2){
  ...
}
```
Note: When creating the header for a function, words can be changed, however the following rules must be adhered to:
* The number of words must remain the same
* **create**, cannot be changed, and must be the first word in the sentence
* the eigth word in the sentence must contain the number of arguments being passed to the function

**Assigning function calls to variables**
```
let result = foo().

OR

let result equal foo().

```

**Creating a main function**
```
Start the program at this function. It will be called <main_function_name>.{
  let a equal 1.
  
  let b equal 2.

  let result equal a + b.
  
  return result.
}

OR

Start my program at this line. I will call it <main_function_name>.{
  let a = 1.
  
  let b = 2.

  let result = a + b.
  
  return result.
}
```
Note: When creating the header for the main function, words can be changed, however the following rules must be adhered to:
* The number of words must remain the same
* **Start** cannot be changed, and must be the first word in the sentence


**Return Statements**
```
return 5.
```


**Example Runnable file that prints 10 to the terminal:**
```
create a function called foo. foo has 0 arguments (){

    let x equal 1.

    let y equal 2. 
    
    let result equal x + y.
    
    return result.

}

Start the program at this function. It will be called main. {
    
    let a equal 3.

    let b equal 4.  

    let c equal foo().  
    
    let result equal a + b + c.

    print result.

}
```

## Built With

* Python3

## Authors

* **Christian Mitton**

