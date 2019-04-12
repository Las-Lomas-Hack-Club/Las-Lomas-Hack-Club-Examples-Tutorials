//php is a scripting language similiar to js but not as popular.  Before learning php I would reccommend some HTML/CSS experience
//This is a review sheet, this is not to learn php right out of the gate.
//First we need to setup php.  Go to https://www.jetbrains.com/phpstorm/ and download/setup phpstorm.  This will be your IDE.

//php works well with HTML, here is how to easily insert php code into an HTML file
<?php
//php code goes here in HTML file
?>
// Two slashes nullify any text on that line.  These are comments.
/*
php also has multi-line comments
Everything here will not execute
*/
//php ends all statements with a ;
//Here is a basic hello world function in php
echo "hello world";

//in php, no keywords are case sensitive.  The following statements all do the same thing.
ECHO "hello world";
echo "hello world";
EcHO "hello world"; //This is clearly not good programming practice, but it still works

//to declare a variable in php it uses odd syntax.  You must pu a $ before any variable.
$x = 10; //declares a variable named x with value of 10
//adding variables
$a = 5;
$b = 10;
echo $a + $b; //prints out 15
