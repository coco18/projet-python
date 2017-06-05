<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Liste des equipment pour {{act}}</h1>
    <ul>
      % for e in list_equipment:
        <li><a href="/equipment?id={{e.id}}">{{e.name_equipment}}</a></li>
      % end
    </ul>
  </body>
</html>
