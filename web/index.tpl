<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <p>
      bonjour
    </p>
  <form method="GET" action="/search">
    <select class="" name="activity">
      % for o in data:
        <option value="{{o}}">{{o}}</option>
      % end
    </select>
    <input type="submit" value="Rechercher">
  </form>
  </body>
</html>
