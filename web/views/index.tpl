<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World!</title>
</head>
<body>
    <p>Welcome {{username}}</p>
    <ul>
        %for thing in things:
        <li>{{thing}}</li>
        %end
    </ul>
    <form action="/favorite_fruit" method="POST">
        What is your favorite fruit?
        <input type="text" name="fruit" size="40" value=""><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
