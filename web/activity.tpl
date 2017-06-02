<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    % for e in list_equipment:
      <li><a href="/equipment?id={{e.id}}">{{e.name_equipment}}</a></li>
    % end
  </body>
</html>
