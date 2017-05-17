<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    % for e in list_equipement:
      <li><a href="/equipement?id={{e.id}}">{{e.name_equipement}}</a></li>
    % end
  </body>
</html>
