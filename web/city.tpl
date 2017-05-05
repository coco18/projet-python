<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Liste des activtées à {{city}}</h1>
    <ul>
      % for o in list_activity:
        <li><a href="/activity?activity={{o[0]}}&city={{city}}">{{o[1]}}</a></li>
      % end
    </ul>
  </body>
</html>
