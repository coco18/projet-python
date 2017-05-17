<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Liste des activtées à {{city}}</h1>
    <ul>
      % for a in list_activity:
        <li><a href="/activity?activity={{a.id}}&city={{city}}">{{a.name_activity}}</a></li>
      % end
    </ul>
  </body>
</html>
